# This file is placed in the Public Domain.
# pylint: disable=C,R,W0105,W0212,W0718


"errors,reactor,threads,timers"


import inspect
import os
import queue
import threading
import time
import traceback
import types
import _thread


class Errors:

    errors = []

    @staticmethod
    def format(exc):
        return traceback.format_exception(
                                   type(exc),
                                   exc,
                                   exc.__traceback__
                                  )

def errors():
    for err in Errors.errors:
        for line in err:
            yield line


def later(exc):
    excp = exc.with_traceback(exc.__traceback__)
    fmt = Errors.format(excp)
    if fmt not in Errors.errors:
        Errors.errors.append(fmt)


class Commands:

    cmds = {}

    @staticmethod
    def add(func):
        Commands.cmds[func.__name__] = func

    @staticmethod
    def scan(mod):
        for key, cmdz in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmdz.__code__.co_varnames:
                Commands.add(cmdz)


def modloop(*pkgs, disable=""):
    for pkg in pkgs:
        for modname in dir(pkg):
            if modname in spl(disable):
                continue
            if modname.startswith("__"):
                continue
            yield getattr(pkg, modname)


def privileges():
    import pwd
    import getpass
    pwnam2 = pwd.getpwnam(getpass.getuser())
    os.setgid(pwnam2.pw_gid)
    os.setuid(pwnam2.pw_uid)


def scan(*pkgs, init=False, disable=""):
    result = []
    for mod in modloop(*pkgs, disable=disable):
        if type(mod) != types.ModuleType:
            continue
        Commands.scan(mod)
        thr = None
        if init and "init" in dir(mod):
            thr = launch(mod.init)
        result.append((mod, thr))
    return result


class Output:

    cache = {}

    def __init__(self):
        self.oqueue = queue.Queue()

    def dosay(self, channel, txt):
        raise NotImplementedError

    def oput(self, channel, txt):
        self.oqueue.put((channel, txt))

    def output(self):
        while True:
            (channel, txt) = self.oqueue.get()
            if channel is None and txt is None:
                self.oqueue.task_done()
                break
            self.dosay(channel, txt)
            self.oqueue.task_done()

    def start(self):
        launch(self.output)

    def stop(self):
        self.oqueue.put((None, None))

    def wait(self):
        self.oqueue.join()
 

class Reactor:

    def __init__(self):
        self.cbs      = {}
        self.queue    = queue.Queue()
        self.stopped  = threading.Event()

    def callback(self, evt):
        func = self.cbs.get(evt.type, None)
        if func:
            try:
                evt._thr = launch(func, self, evt)
            except Exception as ex:
                evt._ex = ex
                later(ex)

    def loop(self):
        while not self.stopped.is_set():
            try:
                evt = self.poll()
                if not self.stopped.is_set():
                    self.callback(evt)
            except (KeyboardInterrupt, EOFError):
                if "ready" in dir(evt):
                    evt.ready()
                _thread.interrupt_main()
                
    def poll(self):
        if not self.stopped.is_set():
            return self.queue.get()

    def put(self, evt):
        self.queue.put(evt)

    def register(self, typ, cbs):
        self.cbs[typ] = cbs

    def start(self):
        launch(self.loop)

    def stop(self):
        self.stopped.set()


class Client(Reactor):

    def display(self, evt):
        for txt in evt.result:
            self.raw(txt)

    def raw(self, txt):
        raise NotImplementedError


class BufferedClient(Client, Output):

    def __init__(self):
        Client.__init__(self)
        Output.__init__(self)

    def display(self, evt):
        for txt in evt.result:
            self.oput(evt.channel, txt)

    def dosay(self, channel, txt):
        self.raw(txt)

    def raw(self, txt):
        raise NotImplementedError

    def start(self):
        Client.start(self)
        Output.start(self)

    def stop(self):
        Client.stop(self)
        Output.stop(self)


class Event:

    def __init__(self):
        self._ready = threading.Event()
        self._thr   = None
        self.result = []
        self.type   = "event"
        self.txt    = ""

    def __getattr__(self, key):
        return self.__dict__.get(key, "")

    def __str__(self):
        return str(self.__dict__)

    def ready(self):
        self._ready.set()

    def reply(self, txt):
        self.result.append(txt)

    def wait(self):
        self._ready.wait()
        #if self._thr:
        #    self._thr.join()


class Thread(threading.Thread):

    def __init__(self, func, thrname, *args, daemon=True, **kwargs):
        super().__init__(None, self.run, thrname, (), {}, daemon=daemon)
        self.name      = thrname or name(func)
        self.queue     = queue.Queue()
        self.result    = None
        self.starttime = time.time()
        self.queue.put_nowait((func, args))

    def __contains__(self, key):
        return key in self.__dict__

    def __iter__(self):
        return self

    def __next__(self):
        yield from dir(self)

    def size(self):
        return self.queue.qsize()

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

    def run(self):
        try:
            func, args = self.queue.get()
            self.result = func(*args)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()
        except Exception as ex:
            later(ex)


def launch(func, *args, **kwargs):
    nme = kwargs.get("name", name(func))
    thread = Thread(func, nme, *args, **kwargs)
    thread.start()
    return thread


def name(obj):
    typ = type(obj)
    if '__builtins__' in dir(typ):
        return obj.__name__
    if '__self__' in dir(obj):
        return f'{obj.__self__.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj) and '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj):
        return f"{obj.__class__.__module__}.{obj.__class__.__name__}"
    if '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    return None


class Timer:

    def __init__(self, sleep, func, *args, thrname=None, **kwargs):
        self.args  = args
        self.func  = func
        self.kwargs = kwargs
        self.sleep = sleep
        self.name  = thrname or kwargs.get("name", name(func))
        self.state = {}
        self.timer = None

    def run(self):
        self.state["latest"] = time.time()
        launch(self.func, *self.args)

    def start(self):
        timer = threading.Timer(self.sleep, self.run)
        timer.name   = self.name
        timer.sleep  = self.sleep
        timer.state  = self.state
        timer.func   = self.func
        timer.state["starttime"] = time.time()
        timer.state["latest"]    = time.time()
        timer.start()
        self.timer   = timer

    def stop(self):
        if self.timer:
            self.timer.cancel()


class Repeater(Timer):

    def run(self):
        launch(self.start)
        super().run()


"utilities"


def forever():
    while True:
        try:
            time.sleep(0.1)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def spl(txt):
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]


def wrap(func):
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        pass
    except Exception as ex:
        later(ex)


def __dir__():
    return (
        'BufferedClient',
        'Client',
        'Commands',
        'Errors',
        'Event',
        'Reactor',
        'Repeater',
        'Thread',
        'Timer',
        'errors',
        'forever',
        'later',
        'launch',
        'name',
        'privileges',
        'scan',
        'spl',
        'wrap'
    )
