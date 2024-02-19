# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"locate"


from opd import fmt, getmain


k = getmain("k")


def fnd(event):
    k.skel()
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in k.types()])
        if res:
            event.reply(",".join(res))
        return
    otype = event.args[0]
    clz = k.long(otype)
    if "." not in clz:
        for fnm in k.types():
            claz = fnm.split(".")[-1]
            if otype == claz.lower():
                clz = fnm
    nmr = 0
    for fnm, obj in k.find(clz, event.gets):
        event.reply(f"{nmr} {fmt(obj)}")
        nmr += 1
    if not nmr:
        event.reply("no result")
