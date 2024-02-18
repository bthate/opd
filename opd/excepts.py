# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0125,E0402


"deferred exception handling"


import io
import traceback


from .objects import Object


def __dir__():
    return (
        'Error',
    )


__all__ = __dir__()


class Error(Object):

    def __init__(self):
        Object.__init__(self)
        self.errors = []
        self.filter = []
        self.output = print
        self.shown  = []

    def all(self):
        for exc in self.errors:
            self.handle(exc)

    def debug(self, txt):
        if self.output and not self.skip(txt):
            self.output(txt)

    def defer(self, exc):
        excp = exc.with_traceback(exc.__traceback__)
        self.errors.append(excp)

    def format(self, exc):
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

    def handle(self, exc):
        if self.output:
            txt = str(self.format(exc))
            self.output(txt)

    def skip(self, txt):
        for skp in self.filter:
            if skp in str(txt):
                return True
        return False
