# This file is placed in the Public Domain.


"json"


import unittest


from opd.object  import Object
from opd.encoder import dumps
from opd.decoder import loads


VALIDJSON = "{'test': 'bla'}"
VALIDPYTHON = '{"test": "bla"}'


class TestDecoder(unittest.TestCase):

    "TestDecoder"

    def test_loads(self):
        "test loading."
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")


class TestEncoder(unittest.TestCase):


    "TestEncoder"

    def test_dumps(self):
        "test dumping."
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDPYTHON)
