import unittest
import contextio
from contextio.contextio import ContextIO
from contextio.lib.v2_0 import V2_0
from contextio.lib.lite import Lite

from secret import *


@unittest.skip
class TestContextIOFactory(unittest.TestCase):
    def test_ContextIOFactory_returns_v2_0_instance_by_default(self):
        context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)
        self.assertIsInstance(context_io, V2_0)
        params = {
            'id': CONTEXTIO_EMAIL_ID
        }
        account = contextio.Account(context_io, params)
        self.assertTrue(account.get())

    def test_ContextIOFactory_returns_Lite_instance(self):
        context_io = ContextIO(consumer_key="foo", consumer_secret="bar", api_version="lite")
        self.assertIsInstance(context_io, Lite)
