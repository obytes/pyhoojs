import SocketServer
import base64
import threading
import time
import urlparse
import requests
from BaseHTTPServer import BaseHTTPRequestHandler
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException, \
    InvalidElementStateException, NoSuchElementException, NoSuchWindowException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# LOGGING
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('pyhoojs.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Start reading database {}'.format("pyhoojs"))


class ExchangeAuthorizationCodeHandler(BaseHTTPRequestHandler):
    authorization_code = None

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        for key, value in urlparse.parse_qsl(parsed_path.query):
            if key == "code":
                self.authorization_code = value
                self.send_response(200)
                self.end_headers()
                self.wfile.write(value)


class Pyhoojs(ExchangeAuthorizationCodeHandler, ):
    def __init__(self, client_id, client_secret, service_location=None, service_port=None, redirect_uri="oob",
                 driver="phantomjs"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.driver = driver
        self.session_token = None
        self.authorization_url = None
        if redirect_uri == "oob":
            pass
        elif redirect_uri != "oob" and service_location is not None and service_port is not None:
            try:
                server_address = (service_location, service_port)
                httpd = SocketServer.TCPServer(server_address=server_address, RequestHandlerClass=self)
                server_thread = threading.Thread(target=httpd.serve_forever)
                server_thread.daemon = True
                server_thread.start()
            except Exception as ex:
                print ex.message
                exit(1)
        else:
            pass  # handle by your application

    def set_authorization_url(self, client_id=None, redirect_uri=None, response_type="code", state=None,
                              language="en-us"):
        """
        Use the Consumer Key we provide as the client_id to request a redirect URL.
        Also include the redirect_url so that Yahoo knows where to redirect users
        after they authorize access to their data.
            {
            u'relationships': u'read/write_public/private',
            u'yahoo_messenger': u'read_and_write',
            u'gemini_advertising': u'read_and_write',
            u'profiles': u'read_public',
            u'yahoo_fantasy_sports': u'read',
            u'yahoo_contacts': u'read'
            }


            example:
                https://api.login.yahoo.com/oauth2/request_auth?
            client_id=dj0yJmk9ak5IZ2x5WmNsaHp6JmQ9WVdrOVNqQkJUMnRYTjJrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hYQ--&
            redirect_uri=oob&
            response_type=code&
            language=en-us

        :param client_id:  Consumer Key provided to you when you signed up.
        :param redirect_uri: Yahoo redirects Users to this URL after they authorize access to their private data. If the user should not be redirected to your server, you should specify the callback as oob (out of band).
        :param response_type: Must constraint the string code
        :param state: Optional. Your client can insert state information that will be appended to the redirect_uri upon success user authorization.
        :param language: Optional. Language identifier. Default value is en-us.
        :return:

        """
        self.authorization_url = None
        payload = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
        }
        if client_id is not None:
            payload['client_id'] = client_id
            self.client_id = client_id
        if redirect_uri is not None:
            payload['redirect_uri'] = redirect_uri
            self.redirect_uri = redirect_uri
        if response_type is not None:
            payload['response_type'] = response_type
        if language is not None:
            payload['language'] = language
        if state is not None:
            payload['state'] = state

        auth_url = "https://api.login.yahoo.com/oauth2/request_auth"
        response = requests.get(url=auth_url, data=payload)
        assert response.status_code == 200
        self.authorization_url = "{}?{}".format(response.request.url, response.request.body)
        # try:
        #     assert response.status_code == 302
        # except:
        #     pass

    def load_authorization_code(self, username, password, auth_url=None, timeout=3, required_permission_list={}):
        """
        
        :param username: yahoo email
        :param password: yahoo password
        :param auth_url: yahoo auth url
        :param timeout: wait page load timeout
        :param required_permission_list: a list of required permissions
        :return: 
        """
        self.authorization_code = None
        if auth_url is not None:
            self.authorization_url = auth_url
        elif self.authorization_url is None:
            self.set_authorization_url()

        login = username
        passwd = password

        if self.driver == "phantomjs":
            user_agent = (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
            )

            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = user_agent

            driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
        else:
            driver = webdriver.Chrome()

        driver.get(self.authorization_url)

        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, "login-username"))
            )
            logger.info("login-username Page is ready!")
        except TimeoutException:
            logger.error("login-username timeout!")
        finally:
            while True:
                try:
                    login_field = driver.find_element_by_id("login-username")
                    login_field.clear()
                    login_field.send_keys(login)
                    login_field.send_keys(Keys.RETURN)
                    break
                except (InvalidElementStateException, ElementNotVisibleException, StaleElementReferenceException) as ex:
                    time.sleep(1)
                    logger.error("{},{}".format("login_field", ex))
                    pass

        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, "login-passwd"))
            )
            logger.info("login-passwd Page is ready!")
        except TimeoutException:
            logger.error("login-passwd timeout!")
        finally:
            while True:
                try:
                    passwd_field = driver.find_element_by_id("login-passwd")
                    passwd_field.clear()
                    passwd_field.send_keys(passwd)
                    passwd_field.send_keys(Keys.RETURN)
                    break
                except (InvalidElementStateException, ElementNotVisibleException, StaleElementReferenceException) as ex:
                    time.sleep(1)
                    logger.error("{},{}".format("passwd_field", ex))
                    pass
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, "oauth2-agree"))
            )
            logger.info("oauth2-agree Page is ready!")
        except TimeoutException:
            logger.error("oauth2-agree timeout!")
        finally:
            while True:
                try:
                    oauth_agree = driver.find_element_by_id("oauth2-agree")
                    required_permission_list = {}
                    permissions = driver.find_elements_by_class_name("oauth2-scope-name-wrapper")
                    for permission in permissions:
                        key = permission.find_element_by_class_name("oauth2-scope-name").get_attribute(
                            "innerHTML").lower().replace(' ', '_')
                        value = permission.find_element_by_class_name("oauth2-scope-allow").get_attribute(
                            "innerHTML").lower().replace(' ', '_')
                        required_permission_list[key] = value
                    print required_permission_list
                    import pdb;
                    pdb.set_trace()
                    oauth_agree.click()
                    break
                except NoSuchWindowException as ex:
                    logger.error("{},{}".format("oauth-agree", ex))
                    exit(0)
                except (NoSuchElementException, InvalidElementStateException, ElementNotVisibleException,
                        StaleElementReferenceException) as ex:
                    time.sleep(1)
                    logger.error("{},{}".format("oauth_agree", ex))
                    pass
            pass
        # // *[ @ id = "Stencil"] / body / div[1] / div[2] / div / div / div / div[1] / code
        if self.redirect_uri == "oob":  # handle within the same request
            try:
                WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, "//code[@class='oauth2-code']"))

                )
                logger.info("oauth2-code Page is ready!")
            except TimeoutException:
                logger.error("oauth2-code timeout!")
            finally:
                retry = 0
                while True:
                    retry += 1
                    try:
                        logger.info("{}, try {}".format("get_oauth_code", retry))
                        oauth_code = driver.find_element_by_xpath("//code[@class='oauth2-code']")
                        oauth = oauth_code.get_attribute("innerHTML")
                        self.authorization_code = oauth
                        logger.info("{}: {}".format("oauth_code", oauth_code))
                        oauth_close = driver.find_element_by_id("oauth2-close")
                        oauth_close.click()
                        break
                    except (NoSuchElementException, InvalidElementStateException, ElementNotVisibleException,
                            StaleElementReferenceException) as ex:
                        time.sleep(1)
                        logger.error("{},{}".format("oauth_code", ex))
                        driver.save_screenshot('screenshot/{}_{}.png'.format(int(time.time()), "oauth_code"))
                        pass
        else:  # the code is redirected to redirect_uri, must be handled by the application
            pass
        try:
            driver.close()
        except NoSuchWindowException as ex:
            logger.error("{},{}".format("driver_close", ex))

    def exchange_authorization_code(self, code, client_id=None, client_secret=None, redirect_uri=None,
                                    grant_type="authorization_code"):
        """
        POST: https://api.login.yahoo.com/oauth2/get_token
        Header:
        Authorization: Basic ZGoweUptazlhazVJWjJ4NVdtTnNhSHA2Sm1ROVdWZHJPVk5xUWtKVU1uUllUakpyYldOSGJ6bE5RUzB0Sm5NOVkyOXVjM1Z0WlhKelpXTnlaWFFtZUQxaFlRLS06NmYzYjI5NjllYzUwOTkxNDM4MDdiNDU4ZTU5MTc5MzFmYmEzMWUwOA ==
        Content - Type: application / x - www - form - urlencoded
        Method: POST
        :param code: Authorization code appended to redirect_uri in previous call. 
        :param client_id: Consumer Key provided to you when you signed up.
        :param client_secret: The Consumer Secret provided to you when you signed up.
        :param redirect_uri: Yahoo redirects Users to this URL after they authorize access to their private data. If your application does not have access to a browser, you must specify the callback as oob (out of band).
        :param grant_type: Must contain the string authorization_code grant type.
        :return: OK 200
        {
           "access_token":"Jzxbkqqcvjqik2IMxGFEE1cuaos--",
           "token_type":"bearer",
           "expires_in":3600,
           "refresh_token":"AOiRUlJn_qOmByVGTmUpwcMKW3XDcipToOoHx2wRoyLgJC_RFlA-",
           "xoauth_yahoo_guid":"JT4FACLQZI2OCE"
        }
        """
        payload = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
        }
        if client_id is not None:
            payload['client_id'] = client_id
            self.client_id = client_id
        if redirect_uri is not None:
            payload['redirect_uri'] = redirect_uri
            self.redirect_uri = redirect_uri
        if client_secret is not None:
            payload['client_secret'] = client_secret
            self.client_secret = client_secret
        if redirect_uri is not None:
            payload['redirect_uri'] = redirect_uri
        if grant_type is not None:
            payload['grant_type'] = grant_type
        if code is not None:
            payload['code'] = code

        credentials = '%s:%s' % (self.client_id, self.client_secret)
        authorization = 'Basic %s' % (base64.b64encode(credentials),)

        header = {
            "Authorization": "Basic {}".format(authorization),
            "Content-Type": "application/x-www-form-urlencoded"
        }

        get_token_url = "https://api.login.yahoo.com/oauth2/get_token"

        response = requests.post(url=get_token_url, data=payload, headers=header)
        assert response.status_code == 200
        self.session_token = response.json()

    def exchange_refresh_token(self, refresh_token, client_id=None, client_secret=None, redirect_uri=None,
                               grant_type="refresh_token"):
        """
        POST: https://api.login.yahoo.com/oauth2/get_token
        After the access token expires, you can use the refresh token, which has a long lifetime, to get a new access token.
        :param refresh_token: Consumer Key provided to you when you signed up.
        :param client_id: The Consumer Secret provided to you when you signed up.
        :param client_secret: Yahoo redirects Users to this URL after they authorize access to their private data. If your application does not have access to a browser, you must specify the callback as oob (out of band)
        :param redirect_uri: The refresh token that you originally received along with the an access token.
        :param grant_type: Must contain the refresh_token grant type.
        :return: 200 OK 
        {
           "access_token":"Jzxbkqqcvjqik2IMxGFEE1cuaos--",
           "token_type":"bearer",
           "expires_in":3600,
           "refresh_token":"AOiRUlJn_qOmByVGTmUpwcMKW3XDcipToOoHx2wRoyLgJC_RFlA-",
           "xoauth_yahoo_guid":"JT4FACLQZI2OCE"
        }
        """
        self.session_token = None
        payload = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
        }
        if client_id is not None:
            payload['client_id'] = client_id
            self.client_id = client_id
        if redirect_uri is not None:
            payload['redirect_uri'] = redirect_uri
            self.redirect_uri = redirect_uri
        if client_secret is not None:
            payload['client_secret'] = client_secret
            self.client_secret = client_secret
        if redirect_uri is not None:
            payload['redirect_uri'] = redirect_uri
        if grant_type is not None:
            payload['grant_type'] = grant_type
        if refresh_token is not None:
            payload['refresh_token'] = refresh_token

        credentials = '%s:%s' % (self.client_id, self.client_secret)
        authorization = 'Basic %s' % (base64.b64encode(credentials),)

        header = {
            "Authorization": "Basic {}".format(authorization),
            "Content-Type": "application/x-www-form-urlencoded"
        }

        get_token_url = "https://api.login.yahoo.com/oauth2/get_token"

        response = requests.post(url=get_token_url, data=payload, headers=header)
        assert response.status_code == 200
        self.session_token = response.json()

    def get_session_token(self, email, password, timeout=60):
        """
        Check if token exists if exists request with refresh_token else get_token
        :param email:
        :param password:
        :param timeout:
        :return:
        """
        self.authorization_code = None  # set to none
        self.load_authorization_code(username=email, password=password)
        while self.authorization_code is None:
            if timeout >= 0:
                time.sleep(1)
                timeout -= 1
            else:
                raise TimeoutException
        self.exchange_authorization_code(code=self.authorization_code)
        return self.session_token

# print url.request.boxy
# https://api.login.yahoo.com/oauth2/request_auth?client_id=dj0yJmk9ak5IZ2x5WmNsaHp6JmQ9WVdrOVNqQkJUMnRYTjJrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hYQ--&redirect_uri=oob&response_type=code&language=en-us
# https://api.login.yahoo.com/oauth2/request_auth/redirect_uri=oob&response_type=code&client_id=dj0yJmk9NjNDNWw0MzlLV21zJmQ9WVdrOWRHaFhORWd4TnpJbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Nw--
