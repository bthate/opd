# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"fleet"


from opd import getmain, name


k = getmain("k")


def flt(event):
    try:
        event.reply(k.all()[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in k.all()]))
