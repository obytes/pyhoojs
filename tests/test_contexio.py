import unittest
import contextio
from contextio.contextio import ContextIO
from contextio.lib.v2_0 import V2_0
from contextio.lib.lite import Lite

from secret import *


#
# class TestContextIOFactory(unittest.TestCase):
#     def test_ContextIOFactory_returns_v2_0_instance_by_default(self):
#         context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)
#         accounts = context_io.get_accounts(email=CONTEXTIO_EMAIL)
#         self.assertIsInstance(context_io, V2_0)
#
#         params = {
#             'id': CONTEXTIO_EMAIL_ID
#         }
#         account = contextio.Account(context_io, params)
#
#         self.assertTrue(account.get())
#
#
#     def test_ContextIOFactory_returns_Lite_instance(self):
#         contextio = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CLIENT_SECRET, api_version="lite")
#
#         self.assertIsInstance(contextio, Lite)
#
#     def test_add_a_user(self):
#         c = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CLIENT_SECRET, api_version="2.0")
#

if __name__ == "__main__":
    pass
    context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)
    accounts = context_io.get_accounts(email=CONTEXTIO_EMAIL)

    params = {
        'id': CONTEXTIO_EMAIL_ID
    }
    account = contextio.Account(context_io, params)
    pass
