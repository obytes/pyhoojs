import unittest

import time

from contextio import ContextIO
from contextio.lib.lite import Lite
from contextio.lib.v2_0 import V2_0

from pdb import set_trace
from pprint import pprint

from pyhoojs import Pyhoojs, write_to_file
from secret import \
    SERVICE_LOCATION, SERVICE_PORT, \
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, \
    YAHOO_PASS, YAHOO_EMAIL, YAHOO_IMAP_PORT, YAHOO_IMAP_SERVER, YAHOO_IMAP_SSL, \
    CONTEXTIO_KEY, CONTEXTIO_EMAIL_ID, CONTEXTIO_EMAIL, CONTEXTIO_SECRET


class TestRetrieveSessionToken(unittest.TestCase):

    @unittest.skip
    def test_generate_session_token_with_chrome_driver(self):
        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob", driver="other")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)

    @unittest.skip
    def test_generate_session_token_with_phantomjs_driver(self):
        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)
        write_to_file('output/access_token_{}_phantomjs_{}.json'.format(int(time.time()), YAHOO_EMAIL), session_token)

    @unittest.skip
    def test_generate_session_token_with_phantomjs_driver_and_create_lite_account(self):
        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)
        write_to_file('output/access_token_{}_phantomjs_{}.json'.format(int(time.time()), YAHOO_EMAIL), session_token)

        # add a new user
        context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET, api_version="lite")
        self.assertIsInstance(context_io, Lite)

        user = context_io.post_user(
            provider_refresh_token=session_token["refresh_token"],
            provider_consumer_key=CLIENT_ID,
            email=YAHOO_EMAIL,
            username=YAHOO_EMAIL,
            server=YAHOO_IMAP_SERVER,
            use_ssl=YAHOO_IMAP_SSL,
            port=YAHOO_IMAP_PORT,
            type="IMAP")

    def test_generate_session_token_with_phantomjs_driver_and_create_v2_0_fetch_email(self):

        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)
        write_to_file('output/access_token_{}_phantomjs_{}.json'.format(int(time.time()), YAHOO_EMAIL), session_token)

        # add a new user
        context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET)
        self.assertIsInstance(context_io, V2_0)

        account = context_io.post_account(
            email=YAHOO_EMAIL,  # required
            server=YAHOO_IMAP_SERVER,  # adding a source in the same call
            username=YAHOO_EMAIL,
            use_ssl=YAHOO_IMAP_SSL,
            port=YAHOO_IMAP_PORT,
            provider_refresh_token=session_token["refresh_token"],
            provider_consumer_key=CLIENT_ID,
            type="IMAP")

        response = account.get_sync()
        """
        {u'pyhoojs@yahoo.com::yahoo': {
            u'Archive': {
            u'last_sync_start': 1480959044,
                u'last_sync_stop': 1480959045,
                u'last_expunge': 0,
                u'initial_import_finished': True},
            u'Sent': {
                u'last_sync_start': 1480959046,
                u'last_sync_stop': 1480959047,
                u'last_expunge': 0,
                u'initial_import_finished': True},
            u'INBOX': {
                u'last_sync_start': 1480959045,
                u'last_sync_stop': 1480959046,
                u'last_expunge': 0,
                u'initial_import_finished': True}}}
        """
        self.assertIsInstance(response, dict)
        response = account.get_messages()
        """
        [<contextio.lib.resources.message.Message object at 0x7fa8d356f890>,
         <contextio.lib.resources.message.Message object at 0x7fa8d356fa10>,
         ...
         ]
        """
        self.assertIsInstance(response, list)
        # this call add an account to  `https://console.context.io/#accounts/`

