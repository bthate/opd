# This file is placed in the Public Domain.
#
# pylint: disable=C,R


import sys


from .clients import cmnd
from .default import Default
from .scanner import scan


from . import modules


Cfg = Default()
Cfg.mod = ",".join(modules.__dir__())


if __name__ == "__main__":
    scan(modules, Cfg.mod)
    cmnd(" ".join(sys.argv[1:]), print)
