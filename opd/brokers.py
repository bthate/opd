# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"broker"


from .objects import Object, keys, values


def __dir__():
    return (
        'Broker',
        'add',
        'get',
        'getall',
        'first',
        'remove'
    )


__all__ = __dir__()


rpr = object.__repr__


class Broker(Object):

    objs = Object()


def add(obj):
    setattr(Broker.objs, rpr(obj), obj)


def getall():
    return values(Broker.objs)


def first():
    for key in keys(Broker.objs):
        return getattr(Broker.objs, key)


def get(orig):
    return getattr(Broker.objs, orig, None)


def remove(obj):
    delattr(Broker.objs, rpr(obj))
