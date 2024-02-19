# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"status of bots"


from opd import getmain


k = getmain("k")


def err(event):
    nmr = 0
    for bot in k.all():
        if 'state' in dir(bot):
            event.reply(str(bot.state))
            nmr += 1
    event.reply(f"status: {nmr} errors: {len(k.errors)}")
    for exc in k.errors:
        txt = k.format(exc)
        for line in txt.split():
            event.reply(line)
