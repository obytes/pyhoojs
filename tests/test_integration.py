import unittest
from pyhoojs import Pyhoojs
from secret import \
    SERVICE_LOCATION, SERVICE_PORT, \
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, \
    YAHOO_PASS, YAHOO_EMAIL


class TestRetrieveSessionToken(unittest.TestCase):
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
