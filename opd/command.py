# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0718,W0611,E0402


"commands"


from .excepts import Error
from .objects import Object
from .parsers import parse_cmd
from .threads import launch
from .utility import getmain


def __dir__():
    return (
        "Command",
    )


__all__ = __dir__()


class Command(Object):

    def __init__(self):
        Object.__init__(self)
        self.cmds = Object()

    def add(self, func):
        setattr(self.cmds, func.__name__, func)

    def command(self, evt):
        parse_cmd(evt)
        func = getattr(self.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
                evt.show()
            except Exception as exc:
                k = getmain("k")
                k.defer(exc)
        evt.ready()
