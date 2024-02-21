# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,W0622,E0402,E0603


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
# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,W0622,E0402


from .brokers import *
from .clients import *
from .command import *
from .default import *
from .excepts import *
from .handler import *
from .locates import *
from .message import *
from .objects import *
from .parsers import *
from .persist import *
from .repeats import *
from .scanner import *
from .threads import *
from .utility import *
from .workdir import *


def __dir__():
    return (
            'Broker',
            'Client',
            'Command',
            'Default',
            'Error',
            'Event',
            'Handler',
            'NoDate',
            'Object',
            'Repeater',
            'Thread',
            'Timer',
            'Workdir',
            'add',
            'cdir',
            'checkpid',
            'construct',
            'daemon',
            'dump',
            'dumps',
            'edit',
            'fetch',
            'first',
            'fmt',
            'fntime',
            'forever',
            'fqn',
            'getpid',
            'give',
            'ident',
            'items',
            'keys',
            'laps',
            'launch',
            'load',
            'loads',
            'name',
            'parse_cmd',
            'parse_time',
            'printall',
            'privileges',
            'remove',
            'scan',
            'search',
            'skel',
            'spl',
            'sync',
            'take',
            'update',
            'values',
            'wrap'
     )


__all__ = __dir__()
