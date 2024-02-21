# This file is placed in the Public Domain.
#
#


"enable/disable"


import sys


from ..excepts import Error
from ..scanner import scan


from .. import modules


def __dir__():
    return (
       'dis',
       'ena'
    ) 


def dis(event):
    if not event.args:
        mods = ",".join(dir(modules))
        event.reply(f"disable {mods}")
        return
    what = event.args[0]
    mod = getattr(modules, what, None)
    print(mod)
    if mod:
        func = getattr(mod, "shutdown")
        if func:
            try:
                func()
            except Exception as ex:
               Error.add(mod)


def ena(event):
    if not event.args:
        mods = ",".join(dir(modules))
        event.reply(f"enable {mods}")
        return
    what = event.args[0]
    try:
        init = event.args[1]
    except IndexError:
        init = False
    scan(modules, what, init)
