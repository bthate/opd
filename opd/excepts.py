# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0125,W0622,E0402


"deferred exception handling"


import io
import traceback


from .objects import Object


def __dir__():
    return (
        'Error',
        'debug',
        'defer',
        'printall'
    )


__all__ = __dir__()


class Error(Object):

    errors = []
    filter = []
    output = print
    shown  = []


def debug(txt):
    if Error.output and not skip(txt):
        Error.output(txt)


def defer(exc):
    excp = exc.with_traceback(exc.__traceback__)
    Error.errors.append(excp)


def format(exc):
    res = ""
    stream = io.StringIO(
                         traceback.print_exception(
                                                   type(exc),
                                                   exc,
                                                   exc.__traceback__
                                                  )
                        )
    for line in stream.readlines():
        res += line + "\n"
    return res


def printexc(exc):
    if Error.output:
        txt = str(format(exc))
        Error.output(txt)


def printall():
    for exc in Error.errors:
        printexc(exc)


def skip(txt):
    for skp in Error.filter:
        if skp in str(txt):
            return True
    return False
