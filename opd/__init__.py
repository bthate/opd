# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,W0622,E0402


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
            'Storage',
            'Thread',
            'Timer',
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
            'getall',
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
