# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,E0402


"""Original Programmer Daemon

opd <cmd> [key=val] [key==val] [mod=n1,n2]
opd [-a] [-c] [-d] [-h] [-v]

commands:

cmd - commands
mod - show available modules

modules:

$ opd mod
cmd,flt,irc,log,mod,mre,pwd,req,rss,tdo,thr

options:

-a     load all modules
-c     start console
-d     start daemon
-h     display help
-v     use verbose
"""


from .brokers import *
from .clients import *
from .command import *
from .configs import *
from .default import *
from .excepts import *
from .handler import *
from .objects import *
from .parsers import *
from .runtime import *
from .storage import *
from .threads import *
from .utility import *


def __dir__():
    return (
            'Broker',
            'Cfg',
            'Client',
            'Command',
            'Config',
            'Default',
            'Error',
            'Event',
            'Handler',
            'Kernel',
            'NoDate',
            'Object',
            'Repeater',
            'Storage',
            'Thread',
            'Timer',
            'cdir',
            'checkpid',
            'construct',
            'daemon',
            'dump',
            'dumps',
            'edit',
            'fetch',
            'find',
            'fmt',
            'fntime',
            'forever',
            'fqn',
            'getpid',
            'ident',
            'items',
            'keys',
            'laps',
            'last',
            'launch',
            'load',
            'loads',
            'name',
            'parse_cmd',
            'parse_time',
            'privileges',
            'read',
            'search',
            'spl',
            'sync',
            'update',
            'values',
            'wrap',
            'write'
     )


__all__ = __dir__()
