import unittest

from contextio.contextio import ContextIO
from contextio.lib.v2_0 import V2_0
from contextio.lib.lite import Lite

import pytest
from secret import *


class TestContextIOFactory(unittest.TestCase):
    def test_ContextIOFactory_returns_v2_0_instance_by_default(self):
        contextio = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)

        self.assertIsInstance(contextio, V2_0)

    def test_ContextIOFactory_returns_Lite_instance(self):
        contextio = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CLIENT_SECRET, api_version="lite")

        self.assertIsInstance(contextio, Lite)

    def test_add_a_user(self):
        contextio = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CLIENT_SECRET, api_version="lite")
        contextio.post_user({

        })


if __name__ == "__main__":
    pass
