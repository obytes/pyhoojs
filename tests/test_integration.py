import SocketServer
import threading
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler

from pyhoojs import Pyhoojs
from secret import SERVICE_LOCATION, SERVICE_PORT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, YAHOO_PASS, YAHOO_EMAIL


def write_to_file(file_name, json_data):
    import json
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile)


def test_generate_session_token():
    # fake a server to handle redirect
    client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URL, driver="other")
    client.set_authorization_url()
    session_token = client.get_session_token(username=YAHOO_EMAIL, password=YAHOO_PASS)
    print session_token
