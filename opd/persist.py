# This file is placed in the Public Domain.
#
#


"eternity"


import datetime
import os
import _thread


from opd.objects import Object, dump, fqn, load, update
from opd.utility import cdir, strip
from opd.workdir import Workdir, store, types


def __dir__():
    return (
        'Persist',
        'ident',
        'fetch',
        'last',
        'read',
        'sync',
        'write'
    )


__all__ = __dir__()


lock = _thread.allocate_lock()


class Persist(Object):

    classes = Object()

    @staticmethod
    def add(clz):
        if not clz:
            return
        name = str(clz).split()[1][1:-2]
        setattr(Persist.classes, name, clz)

    @staticmethod
    def fns(mtc=""):
        dname = ''
        pth = store(mtc)
        for rootdir, dirs, _files in os.walk(pth, topdown=False):
            if dirs:
                for dname in sorted(dirs):
                    if dname.count('-') == 2:
                        ddd = os.path.join(rootdir, dname)
                        fls = sorted(os.listdir(ddd))
                        for fll in fls:
                            yield strip(os.path.join(ddd, fll))


def long(name):
    split = name.split(".")[-1].lower()
    res = name
    for named in Persist.classes:
        if split in named.split(".")[-1].lower():
            res = named
            break
    if "." not in res:
        for fnm in types():
            claz = fnm.split(".")[-1]
            if fnm == claz.lower():
                res = fnm
    return res


def ident(obj):
    return os.path.join(
                        fqn(obj),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )


def fetch(obj, pth):
    pth2 = store(pth)
    read(obj, pth2)
    return strip(pth)


def read(obj, pth):
    with lock:
        with open(pth, 'r', encoding='utf-8') as ofile:
            update(obj, load(ofile))


def sync(obj, pth=None):
    if pth is None:
        pth = ident(obj)
    pth2 = store(pth)
    write(obj, pth2)
    return pth


def write(obj, pth):
    with lock:
        cdir(os.path.dirname(pth))
        with open(pth, 'w', encoding='utf-8') as ofile:
            dump(obj, ofile, indent=4)
