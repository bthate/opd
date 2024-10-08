# This file is placed in the Public Domain.


"list of bots."


from .object import Object


rpr = object.__repr__


class Fleet(Object):

    "Fleet"

    bots = []

    @staticmethod
    def all():
        "return all objects."
        return Fleet.bots

    @staticmethod
    def announce(txt):
        "announce on all bots."
        for bot in Fleet.bots:
            try:
                bot.announce(txt)
            except AttributeError:
                pass

    @staticmethod
    def say(channel, txt):
        "announce on all bots."
        for bot in Fleet.bots:
            try:
                bot.say(channel, txt)
            except AttributeError:
                pass

    @staticmethod
    def get(orig):
        "return bot."
        res = None
        for bot in Fleet.bots:
            if rpr(bot) == orig:
                res = bot
                break
        return res

    @staticmethod
    def register(obj):
        "add bot."
        Fleet.bots.append(obj)


def __dir__():
    return (
        'Fleet',
    )
