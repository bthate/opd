# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212,W0613,E0402


"clients"


import inspect
import time
import _thread


from .brokers import Broker
from .command import Command
from .handler import Event, Handler
from .objects import Object
from .parsers import spl
from .storage import Storage
from .threads import launch


def __dir__():
    return (
        "Client",
    )


__all__ = __dir__()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.register("command", Command.handle)
        Broker.add(self)

    def announce(self, txt):
        self.raw(txt)

    def say(self, channel, txt):
        self.raw(txt)

    def raw(self, txt):
        pass
