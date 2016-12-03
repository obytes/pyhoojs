import unittest
from pyhoojs import Pyhoojs, write_to_file
from secret import \
    SERVICE_LOCATION, SERVICE_PORT, \
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, \
    YAHOO_PASS, YAHOO_EMAIL


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
        write_to_file('output/access_token_phantomjs_{}.json'.format(YAHOO_EMAIL), session_token)
