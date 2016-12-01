import unittest
import contextio
from contextio.contextio import ContextIO
from contextio.lib.v2_0 import V2_0

from secret import *


class TestContextIOFactory(unittest.TestCase):
    def test_ContextIOFactory_returns_v2_0_instance_by_default(self):
        context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)
        self.assertIsInstance(context_io, V2_0)
        params = {
            'id': CONTEXTIO_EMAIL_ID
        }
        account = contextio.Account(context_io, params)
        self.assertTrue(account.get())
