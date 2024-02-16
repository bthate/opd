# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212,W0611,W0613,E0401


"main"


import getpass
import inspect
import os
import pwd
import readline
import sys
import termios
import time
import _thread


from . import Cfg, Client, Command, Config, Default, Error, Event, Object, Storage
from . import cdir, launch, modules, parse_cmd, spl, scan, update
from . import checkpid, forever, getpid, privileges, wrap


def __dir__():
    return (
        'Cfg',
        'Console',
        'cmnd',
        'daemon',
        'forever',
        'main',
        'privileges',
        'wrap',
        'wrapped'
    )


__all__ = __dir__()


class Console(Client):

    def announce(self, txt):
        pass

    def callback(self, evt):
        Client.callback(self, evt)
        evt.wait()

    def poll(self):
        evt = Event()
        evt.orig = object.__repr__(self)
        evt.txt = input("> ")
        evt.type = "command"
        return evt

    def say(self, channel, txt):
        txt = txt.encode('utf-8', 'replace').decode()
        print(txt)


def cmnd(txt, out):
    clt = Client()
    clt.raw = out
    evn = Event()
    evn.orig = object.__repr__(clt)
    evn.txt = txt
    Command.handle(evn)
    evn.wait()
    return evn


def main():
    Storage.skel()
    parse_cmd(Cfg, " ".join(sys.argv[1:]))
    update(Cfg, Cfg.sets)
    if 'a' in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
    if "v" in Cfg.opts:
        dte = time.ctime(time.time()).replace("  ", " ")
        Error.debug(f"{Cfg.name.upper()} {Cfg.opts.upper()} started {dte}")
    if "h" in Cfg.opts:
        from . import __doc__ as txt
        print(txt)
        return
    if "c" in Cfg.opts:
        scan(modules, Cfg.mod, True, Cfg.dis, True)
        csl = Console()
        csl.start()
        forever()
        return
    if Cfg.otxt:
        Cfg.mod = ",".join(modules.__dir__())
        scan(modules, Cfg.mod, False, Cfg.sets.dis, False)
        return cmnd(Cfg.otxt, print)
    if checkpid(getpid(Cfg.pidfile)):
        print("daemon is already running.")
        return
    Cfg.mod = ",".join(modules.__dir__())
    Cfg.user = getpass.getuser()
    daemon(Cfg.pidfile, "v" in Cfg.opts)
    privileges(Cfg.user)
    scan(modules, Cfg.mod, True, Cfg.dis, True)
    forever()


def wrapped():
    wrap(main)
    Error.show()


if __name__ == "__main__":
    wrapped()
