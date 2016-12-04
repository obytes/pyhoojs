# pyhoojs
Python program that uses, webdriver to read from a table with username and passwords, and retrieve `access  &amp; refresh tokens`


# feature

 * [x] Ignore print, move them to logger
 * [ ] Refactor exception handling on PhantomJS page load
 * [x] Make sure `yahoo mail is present` when granting access (permission filter, when loading authorization_code)
 * [x] Test `rake test`
 * [x] Dockerize tests
 * [ ] Validate test fetching emails from context.io


# usage

 1. rename secret.example.py into secret.py
 2. fill with you credentials
 3. install requirements ...
 4. run

```
# fill your secrets
from secret import *
from pyhoojs import Pyhoojs

client = Pyhoojs(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="oob")
client.set_authorization_url()
session_token = client.get_session_token(email=YAHOO_EMAIL, password=YAHOO_PASS)

session_token
"""
{
 u'access_token':
 u'uKN0hCWev1GN0I0FOe9X0JHwiQnsBbV_KvaBVLMiU779jkD0tKohDifOz8NjRfzdAUtE_wIAC0eUxRt4AV9RRjUcj5AREDw2t6b.PwsE15fiQvX9iqFhVR72TJcRqMucfYgAPUND..rUr5DC4l6DC_lUEkpfVspQBwR5aRiWi74mCEc3F0m8jWtxOKo.pT6LL8fA.6ilN_0gUShndDS9aylaGLeNCpVjf2Fyp1XlN9zIxEXdr8bK19pHsmNAhTSDuweR9Ap66Kghj_JR9YDj.oIUMRt7b4ITmY8k.mQLxr0Trzcj.92xK6yvl8KFNTOHAU3AfAmeIx5LkO9mlnsC7Nvpe4CGisH6_5Z2wb3HynnB7VtHELxEV3hLavgjMxo3DEd1ucGMES34IbJPYr6QXd2JJydE0igXs0qT0XRfIluzJ6Gs9zWOygBoEjzKpchaWKZEsww6vFS3QuRaRQWIAAMZFmEv6LupGK7qmvbwvieGXfk4UgCPak4UQdokBGimPa2f3r3LkEtH0VtAxU6xbLyluYYoFQ1XulcGZVDS3t6W.IGBWyo08vRUjDoc_ENlh8nr8ukxKxOqx7oPijNzLiiNVHAzvtJUzl_22wX88F1vWIpA9PSVCgjZCc6T3hqsqbximuZ5xXkonTYoBhfQWEkxw5cIkr3OB_yos1VKxNff1Pr1nmOVX7t0SRhVQTnW.FtjQWR1gTwrnPDuCx.9Bsxbuc1gxQtYh2VEk50O48wW.IdjEk2AtVlqqjP0TkNF_bajf_zbWCdGYT1ccUuS0UZzYDldvEELhGk5EjaLUfDC9rF4j5ughPD10Xis2pLvYgToOQ9xFCOciJspCFJMJYGBGKLiGATWTVPkoWJiYzcSwyUpv_BPNNtQMjh0qD96BkOu8SVoel5I_zujyGRqph0c5Y.nisXHU594lrknUmLqY2widkHmEKetvYxLuAITLk5Hgz59RwhXQQEPXMK_a2hZ7q8QxVcEWI5Yjg.VUyXicMWKv3LGsmK5', 
 u'token_type': u'bearer', 
 u'expires_in': 3600, 
 u'xoauth_yahoo_guid': u'PP73UFM7LPCI4SK75SJMELNZ5A', 
 u'refresh_token': u'ANSKQFhtD98_.TWE3O9zpZVAuas4nMbW_KZFgkGdO0u_wcS4UeZd'
}
"""
client.authorization_url
"""
'https://api.login.yahoo.com/oauth2/request_auth?language=en-us&redirect_uri=oob&response_type=code&client_id=dj0yJmk9NWlSb3VXbDlZTWFYJmQ9WVdrOVJrMXZlakpPTlRBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00NA--'
"""



```
 
# run tests

```bash
# with docker
git pull https://github.com/obytes/pyhoojs
rake build --trace
rake dtest
# locally
rake test
```


# requirements

```
pip install -r requirements/test.txt
npm install 

```


# testing && developing with gui webkit


```
wget https://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip
unizp chromedriver_linux64.zip
# add it to your binary path, example: /usr/bin/
chromedriver

```



# issues

 * If redirects are not to 80/443 app api (credentials instead of page) 
 * Bind yahoo mail with context.io && [allow yahoo connection from none secure source](https://login.yahoo.com/account/security) 


# resources

* [selenium + phantomjs](https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/)
* [yahoo-oauth guide](https://developer.yahoo.com/oauth2/guide/)
* [oauth flow diagram](https://s.yimg.com/oo/cms/products/oauth2/flows_authcode/images/yahoo_auth_flow_04974dd18.png)
* [webdrivers](https://chromedriver.storage.googleapis.com/index.html?path=2.25/)
* [contex.io](http://blog.context.io/2015/07/adding-a-user-with-context-io/)

