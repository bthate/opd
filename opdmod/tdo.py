# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"todo list"


import time


from opd import Object, fntime, laps


class NoDate(Exception):

    pass


class Todo(Object):

    def __init__(self):
        Object.__init__(self)
        self.txt = ''


def dne(event):
    if not event.args:
        event.reply("dne <txt>")
        return
    selector = {'txt': event.args[0]}
    nmr = 0
    for fnm, obj in k.find('todo', selector):
        nmr += 1
        obj.__deleted__ = True
        k.sync(obj, fnm)
        event.reply('ok')
        break
    if not nmr:
        event.reply("nothing todo")


def tdo(event):
    if not event.rest:
        nmr = 0
        for fnm, obj in k.find('todo'):
            lap = laps(time.time()-fntime(fnm))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply("no todo")
        return
    obj = Todo()
    obj.txt = event.rest
    k.sync(obj)
    event.reply('ok')