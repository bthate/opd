# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0201,W0613,W0212


"runtime"


import inspect
import time
import _thread


from .brokers import Broker
from .command import Command
from .configs import Config
from .excepts import Error
from .handler import Handler
from .objects import Object
from .parsers import spl
from .storage import Storage
from .threads import launch


class Cfg(Config):

    pass


class Kernel(Broker, Command, Error, Handler, Storage):

    def __init__(self, *args, **kwargs):
        Broker.__init__(self)
        Command.__init__(self)
        Error.__init__(self)
        Handler.__init__(self)
        Storage.__init__(self)
        self.cfg = Cfg()

    def forever(self):
        while 1:
            try:
                time.sleep(1.0)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def scan(self, pkg, modstr, initer=False, disable="", wait=True):
        mds = []
        for modname in spl(modstr):
            if modname in spl(disable):
                continue
            module = getattr(pkg, modname, None)
            if not module:
                continue
            for _key, cmd in inspect.getmembers(module, inspect.isfunction):
                if 'event' in cmd.__code__.co_varnames:
                    self.add(cmd)
            for _key, clz in inspect.getmembers(module, inspect.isclass):
                if not issubclass(clz, Object):
                    continue
                self.append(clz)
            if initer and "init" in dir(module):
                module._thr = launch(module.init, name=f"init {modname}")
                mds.append(module)
        if wait and initer:
            for mod in mds:
                mod._thr.join()
        return mds
