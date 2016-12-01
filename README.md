# pyhoojs
Python program that uses, webdriver to read from a table with username and passwords, and retrieve `access  &amp; refresh tokens`


# feature

 * [x] Ignore print, move them to logger
 * [ ] Refactor exception handling on PhantomJS page load
 * [x] Make sure `yahoo mail is present` when granting access (permission filter, when loading authorization_code)
 * [x] Test `rake test`
 * [ ] Dockerize tests


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
u'access_token': u'iPUd46Wev1G2odQrMFnKz.kAduwjVa_yGUgg71Ce239SRdoVg.q3YV01QpZoHQAY_t6wtttilClLlndYlIl.f.5c_wwHKtaC2z7_Qc1GoILXC.1t3z_3xzpsNsnbW4q6FVqg8Hm10OAyIi48QyRhKEYFRi5c6NuUW0y6YsZMQOKZAq.IEE_HpxQ6CKqF7nN.Jt1zM14ZMkcl3MdRZx0.EKhwo0QaF8D_bY_Vk97f3EpfMykYxMkQu__bKi_zo_8ZNpGqcjT_H7Q1LxspflTq6evsjQpYm3odKRiGNK4qAv4kf56FSuKQBD1tcO5Wb5B5TzE3EuywkC1jkv_HLbRTmQwdEW14IxYqO.IcbSNW4X2yaLYn3hz4unX0DHori6nra7DM.6Q6oIHCroXqYEYYYOXT5oW2N9MXnae3ej9Q7v_JtUbLA1Qn77gIwOXZ0larujQgY3ytbplb7Z0ajrjEyI7Zs.7lM936Hed8yw.CiIKYiREEuqpFTxoTectq6j9quylnqHp9kk5QdT5j2KDd60WtCWhVPKIcor0CbGtgY2OP4ExUCxkFuxvdxiJAUCJ.43rmzthnLTQQ40ZnfiXaptsIhtWBtLhbPbn88cuE93CUQ1mW.WTiCf6BdMicWNIQj3t5Q6Jrm9nv3Bv98M6Nh7uyj2AHLpOQ1TJ_kT4e8gigKaupq5d2250FNuW.LSrFuVnSHSQ6Gv9tblukWbtIihCcth7cZjbHSFKfZASYZG7Z8WvZKlc91qmxASYaQmkesLsQX6TMhmX_ZLDNwjWXYxnTbgBwtgbC_TQSPHkfVxIFfRo5LXexQEB3eSrzroCbVcNLtLwNNkNaz8ewT4h78GqgBF4nN3n1m8RVbgZz65X2HfqO0KfCKdwtF5jfeWGokio.nMvbDhKEHnJz4WWc_a.SDbrDQVlc9RIdovd32nGd4f1cwlHwu_36O02vQZa54XS8dhsicKSzAAaKF9zX3lsGF2A.7Kv5VGJu.7d5MFRdomM3Y3KwanEY', 
u'token_type': u'bearer', 
u'expires_in': 3600, 
u'xoauth_yahoo_guid': u'PP73UFM7LPCI4SK75SJMELNZ5A', 
u'refresh_token': u'AF5FQFj0NRHJ_qSAjN0zgyDsqC7ynMbW_KZFgkGdO0u_wcS4UeZd'
}
"""
client.authorization_url
"""
'https://api.login.yahoo.com/oauth2/request_auth?language=en-us&redirect_uri=oob&response_type=code&client_id=dj0yJmk9NWlSb3VXbDlZTWFYJmQ9WVdrOVJrMXZlakpPTlRBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00NA--'
"""



```
 


# requirements

```
pip install -r requirements.txt

npm install # -g phantomjs-prebuilt 

# append add the phantomjs-prebuilt to your $PYTHONPATH
./node_modules/phantomjs-prebuilt/bin/phantomjs
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

