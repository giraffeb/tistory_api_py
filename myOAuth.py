import abc
from urllib import parse, request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import ConfigFileManager



class OAuth(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def requestCode(self):
        return

class Tistory_OAuth(OAuth):

    configFileManager = None

    client_id = '78b206b9a17689c52f1749c3b6db2c6f'
    redirect_uri = 'oob'

    def __init__(self, conficFileManager):
        self.configFileManager = conficFileManager

    def requestCode(self):
        '''
        METHOD : GET
        :parameter
            client_id : 등록시 발급받은 client_id
            redirect_uri : 등록시 등록한 redirect_uri
            response_type : "code" 라고 입력
            state : Cross-site Request Forgery 공격을 보호하기 위한 임의의 고유한 문자열. 리다이렉트시 해당 값이 전달됨. (필수아님)
        '''

        #request url
        target_url = 'https://www.tistory.com/oauth/authorize'

        #paramter generate
        parameter = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'token'
        }

        #data -> urlencode
        data = parse.urlencode(parameter)

        #request url+data generate
        req = target_url +'/?'+data

        #useing selenium + google chrome : request to url
        driver = webdriver.Chrome('chromedriver')

        #setting to wait
        wait = WebDriverWait(driver, 3)
        #send request
        driver.get(req)
        current_url = driver.current_url

        #loop until get aceess token
        while True:
            if current_url == driver.current_url:
                sleep(1)
            else:
                break


        #after get access token
        #parsing
        res = driver.current_url
        start = res.find('#') + 1
        end = res.find('&')

        access_token_str = res[start:end]
        start = access_token_str.find('=') + 1
        access_token = access_token_str[start:]

        print(res)
        print(access_token)
        self.configFileManager.saveAccessToken(self, access_token)


class Github_OAuth:
    conficFileManager = None

    def __init__(self, conficFileManager):
        self.configFileManager = conficFileManager

