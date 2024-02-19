# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"broker"


from .objects import Object, keys, values


def __dir__():
    return (
        "Broker",
        'all',
        'first',
        'give',
        'remove',
        'take'
    )


__all__ = __dir__()


rpr = object.__repr__


class Broker(Object):

    objs = Object()


def all():
    return values(Broker.objs)


def first(self):
    for key in keys(Broker.objs):
        return getattr(Broker.objs, key)


def give(orig):
    return getattr(Broker.objs, orig, None)


def remove(self, obj):
    delattr(Broker.objs, rpr(obj))


def take(obj):
    setattr(Broker.objs, rpr(obj), obj)
