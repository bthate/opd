# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212,W0613,E0402


"clients"


from .command import Command
from .handler import Handler


def __dir__():
    return (
        "Client",
    )


__all__ = __dir__()


class Client(Command, Handler):

    def __init__(self):
        Command.__init__(self)
        Handler.__init__(self)
        self.register("command", Command.handle)

    def announce(self, txt):
        self.raw(txt)

    def say(self, channel, txt):
        self.raw(txt)

    def raw(self, txt):
        pass
