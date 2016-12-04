import unittest

import time

from contextio import ContextIO
from contextio.lib.lite import Lite
from contextio.lib.resources.user import User

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

    def test_generate_session_token_with_phantomjs_driver(self):
        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)
        write_to_file('output/access_token_{}_phantomjs_{}.json'.format(int(time.time()), YAHOO_EMAIL), session_token)

    def test_generate_session_token_with_phantomjs_driver_and_fetch_emails(self):
        client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri="oob")

        client.set_authorization_url()
        session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
        self.assertTrue('access_token' in session_token)
        write_to_file('output/access_token_{}_phantomjs_{}.json'.format(int(time.time()), YAHOO_EMAIL), session_token)

        # add a new user
        context_io = ContextIO(consumer_key=CONTEXTIO_KEY, consumer_secret=CONTEXTIO_SECRET, api_version="lite")
        self.assertIsInstance(context_io, Lite)

        # user = context_io.post_user(
        #     provider_refresh_token=session_token["refresh_token"],
        #     provider_consumer_key=CLIENT_ID,
        #     email=YAHOO_EMAIL,
        #     username=YAHOO_EMAIL,
        #     server=YAHOO_IMAP_SERVER,
        #     use_ssl=YAHOO_IMAP_SSL,
        #     port=YAHOO_IMAP_PORT,
        #     type="IMAP")

        # import pdb; pdb.set_trace()
        # self.assertEqual(user, User)
        # def post_user(self, **kwargs):
        #     req_args = ["email", "server", "username", "use_ssl", "port", "type"]
        #
        #     if check_for_account_credentials(kwargs):
        #         all_args = [
        #                        "password", "provider_refresh_token", "provider_consumer_key", "migrate_account_id",
        #                        "first_name", "last_name"
        #                    ] + req_args
        #
        #         params = sanitize_params(kwargs, all_args, req_args)
        #
        #         return User(self, self._request_uri("users", method="POST", params=params))
