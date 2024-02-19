# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"broker"


from .objects import Object, keys, values


def __dir__():
    return (
        "Broker",
    )


__all__ = __dir__()


rpr = object.__repr__


class Broker(Object):

    objs = Object()

    def all(self):
        return values(self.objs)

    def first(self):
        for key in keys(self.objs):
            return getattr(self.objs, key)

    def give(self, orig):
        return getattr(self.objs, orig, None)

    def remove(self, obj):
        delattr(self.objs, rpr(obj))

    def take(self, obj):
        setattr(self.objs, rpr(obj), obj)
