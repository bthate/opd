# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"fleet"


from opd.brokers import getall
from opd.utility import name


def flt(event):
    try:
        event.reply(getall()[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in getall()]))
