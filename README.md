# pyhoojs
Python program that uses, webdriver to read from a table with username and passwords, and retrieve `access  &amp; refresh tokens`




# usage

 1. rename secret.example.py into secret.py
 2. fill with you credentials
 3. install requirements ...
 4. run
```
rake run


x@x:pyhoojs$ rake run
python pyhoojs.py

https://api.login.yahoo.com/oauth2/request_auth?language=en-us&redirect_uri=oob&response_type=code&client_id=dj0yJmk9NjNDNWw0MzlLV21zJmQ9WVdrOWRHaFhORWd4TnpJbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Nw--
ypjh3zv

{u'access_token': u'HWmCFguev1FFJG3X.fiXHOoRtAG20O_S1qNpkuAoLAVBgDtP_tWZpDSgCVZZLkXx2zG0kYpohdGskWmDQ2269CLz65MNqzemXA24uBIbfJKZboHKHYS57QyzDCNXauRQSH9xyBsRmT5LdUOCw94UrNgd10tI9sUqW5z18Ee1aYAfsIB9nNjlx934EYzpLDfClB7KU7TixJvXalNiXzJt2R65zga9arFGMkbMo8Zml4FVRY9bcxX.7evs58NFraQ9y4AMHqv7stOfi2QZXxWzab4Dx7Czy8_W1QFMYVjplkunXDk_PrRqWYNUCjqKKA52P3EQuWgVaMM81w0jXspZFPCCqCiiiT.ZCkXOuUWVNgWALNGU.naG5uMEON2I.oBX2lZVRQgajpDcOdTbafCHfvq97IYFCpln2ikCNkvm5vCgNV3wNX9YHHopm3DACKOsbYcUyGkib8kNU2xQwcPRYc26mE7popenRApyCra.sI.anupFPt1auR_YXun6GD2thFQKaMacH4VdFpRT9G73mY5TBNiLbkoMGKl9T8f_2HlkFryijN9xB0OGMkk1tfNjpmMVCNi8uIlwtM6KtNyc_.A9cPpdCBSD3MQu405pU4YEr4htzVt.STYnDQ_mXtpiBicEHrgQrNvXxUT1aeSuJdYfIOrrISQkaU2XBbyTrC0PN8zIgIC45X2euaN3s31h5tZ15IM7AHFUbYi5Z8LN0VvpMd8nDOJQTxcORl0ZutpuKdgOhXXVpPAR9IbeaSGjrJkpwwobKKh2N6U6Ki59ypONyfqVLLiQ0DI9Haa6GE8Xoi9k32lhj.GSRhRR0qK3ke7tcw6t6U6dwLcB0JzjvvPrN.8OymdhNSeXJ.iwX8tivmEnV1nDWh8xeb_YFjqMW_S_zl1o46IITnEG8V_BLGAv0uNS6.ka_cDCR8CRekfGiI10YsxEAAUm.Cr_RAwHiFavqzUXcpoenDfVw3_bOVx926WnRNmZcvgOAhLoTrQiGw0as587X4C7',
 u'expires_in': 3600,
 u'refresh_token': u'AMbkP1jDtCHnNdw3lr4b9C1DI7iCcvOWPW6IRaIwyg0I9YuXon0f',
 u'token_type': u'bearer',
 u'xoauth_yahoo_guid': u'PP73UFM7LPCI4SK75SJMELNZ5A'}

{u'access_token': u'nEQiM1eev1HP9qpl5kRMRbWVjGSqcBRDyvV_Bj9adUSDoD0mgVxvS..t86RKUpVtSpDgypfSMH1Pl.w34Jek5I0SL8BHXRgeoGRcHSe7pkEFrT_aqBFOc_4QV_z1iituKSqt6263._PAVtN6kQEfQeeR3HlwDCCqTatRSVHqw5Kt1BLUKJ8XafQrr32kndF48rvkH0QMyZ3clTK9Ttjo6ukgjUqOrZqdIhaNiEpPVHnbz9IPEJ9mtZlqyhS_G1AKpY4nClhobIjq3BcZT4nHiMqNa_0TALsDgYBLXsVUoeZfMl0yFhVEuY0sLL0aBFnQ9yAWb2r33HT0wbPRwUXY2DtIN28_BfDRL7z.NMnAlEFYLm3WxqKmjMIn_4WSa1CDcWPeyiJbrapIr6YFdVBhCP1SQE1sQy6zAl61yHZSW9_Jm.LnyKGgHOvRWuRsfYuV1xBN9rKX2VwexfO5mIwpQBwzYDdDYNbGKyz6vBRYXoEiAnmmf6m_dloLbSEfxyleptQXSVNtgPwRZ0L2AAWW8mnHmuuowTjGlJCfx2P3.3aonxdedm0zgpTPVKGsfR_j2_YKBkxrtlE4jTyMaNEAp1RIjz5Hi5LEmQQcJY_hsZCrTSA.sZvJiuTrzlmJPs0BuExejDIMPn17RjD7L7qnZX53alQi9uYqCTcUgt4_SLQ2HBB5DlOQQ58TfTws__uk2BlaHBUrnxH8.VF1ccdm9S3ehx5o4eYiUbtMB7gRGEwDmwenfXg7V.kcz1YcLZkBPMLXU4LI39OPGRlIL_ENU5mmGx7V34GDOp7ihYwuD3zcRHEsSBoIbtK_l9TeHyXAi4J9rkztvPfGWrc6RjozXZ5l0o4dGzSy4NaPW3zNzcoBUsMZWw2jWJDcgOx7x.2hHteEAisRZL2CpVYYi7t6r3Qt47eUPuMoK6GYMDO4R.zFepmjPlCP9S_hF2D3RKaMi0cs6rF0qHrKaCdMIJFqkr4JPpk264VWgYk73AUj3ILuXCg_0p8U6q9t',
 u'expires_in': 3600,
 u'refresh_token': u'AMbkP1jDtCHnNdw3lr4b9C1DI7iCcvOWPW6IRaIwyg0I9YuXon0f',
 u'token_type': u'bearer',
 u'xoauth_yahoo_guid': u'PP73UFM7LPCI4SK75SJMELNZ5A'}

```






# feature

 * [x] Ignore print, move them to logger
 * [ ] Refactor exception handling on PhantomJS page load
 * [ ] Make sure `yahoo messenger is present` when granting access 
 * [x] Integration test with contextio
 * [ ] Dockerize tests


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

# issues


 * Bind yahoo mail with context.io && [allow yahoo connection from none secure source](https://login.yahoo.com/account/security) 


# resources

* [selenium + phantomjs](https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/)
* [yahoo-oauth guide](https://developer.yahoo.com/oauth2/guide/)
* [oauth flow diagram](https://s.yimg.com/oo/cms/products/oauth2/flows_authcode/images/yahoo_auth_flow_04974dd18.png)
* [webdrivers](https://chromedriver.storage.googleapis.com/index.html?path=2.25/)
* [contex.io](http://blog.context.io/2015/07/adding-a-user-with-context-io/)

