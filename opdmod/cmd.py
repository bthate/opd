# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"list of commands"


from opd.utility import getmain


k = getmain("k")


def cmd(event):
    if k:
        event.reply(",".join(sorted(k.command.cmds)))
