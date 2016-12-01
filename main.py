# fake a server to handle redirect
from pyhoojs import Pyhoojs
from secret import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, YAHOO_EMAIL, YAHOO_PASS

client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                 redirect_uri="oob", driver="other")

client.set_authorization_url()
session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)
print session_token
