# pyhoojs
Python program that uses, webdriver to read from a table with username and passwords, and retrieve `access  &amp; refresh tokens`


Seems like I have to provision it with a local web server







# feature

 [ ] Ignore print, move them to logger
 [ ] Refactor exception handling on PhantomJS page load
 [ ] 


# requirements

```
pip install -r requirements.txt

npm install -g phantomjs-prebuilt
```


# testing && developing with gui webkit

[webdrivers](https://chromedriver.storage.googleapis.com/index.html?path=2.25/)

```
wget https://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip
unizp chromedriver_linux64.zip
# add it to your binary path, example: /usr/bin/
chromedriver

```

[diagram](https://s.yimg.com/oo/cms/products/oauth2/flows_authcode/images/yahoo_auth_flow_04974dd18.png)

# resources

https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/
https://developer.yahoo.com/oauth2/guide/
