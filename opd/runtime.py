# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0201


"runtime"


import os


from .configs import Config


Cfg         = Config()
Cfg.mod     = "cmd,mod"
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
