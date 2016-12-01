# pyhoojs
Python program that uses, webdriver to read from a table with username and passwords, and retrieve `access  &amp; refresh tokens`



# usage

1. rename secret.example.py into secret.py
2. fill with you credentials
3. install requirements ...
4. run
```
rake run
```






# feature

 [x] Ignore print, move them to logger
 [ ] Refactor exception handling on PhantomJS page load
 [x] Integration test with contextio
 [ ] Dockerize tests


# requirements

```
pip install -r requirements.txt

npm install -g phantomjs-prebuilt
```


# testing && developing with gui webkit


```
wget https://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip
unizp chromedriver_linux64.zip
# add it to your binary path, example: /usr/bin/
chromedriver

```


# resources

[selenium + phantomjs](https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/)
[yahoo-oauth guide](https://developer.yahoo.com/oauth2/guide/)
[oauth flow diagram](https://s.yimg.com/oo/cms/products/oauth2/flows_authcode/images/yahoo_auth_flow_04974dd18.png)
[webdrivers](https://chromedriver.storage.googleapis.com/index.html?path=2.25/)
[contex.io](http://blog.context.io/2015/07/adding-a-user-with-context-io/)

