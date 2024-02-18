# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"list of commands"


from opd.utility import getmain




def cmd(event):
    k = getmain("k")
    if not k:
        return
    event.reply(",".join(sorted(list(k.cmds))))
