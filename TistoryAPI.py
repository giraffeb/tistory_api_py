import myOAuth
import urllib
import codecs
import json
import pprint

class TistoryAPI:

    oauth = None
    access_token = None

    def __init__(self, oauth):
        self.oauth = oauth
        self.access_token = oauth.configFileManager.config['tistory_access_token']


    def getList(self):
        '''
        GET
        :return:
        '''
        target_url = 'https://www.tistory.com/apis/post/list'

        parameter = {'access_token' : self.access_token,
                     'blogName' : 'giraffeb',
                     'output': 'json'}

        data = urllib.parse.urlencode(parameter)
        req = target_url + '?' + data

        print(req)
        response = urllib.request.urlopen(req)
        output = response.read().decode('utf-8')

        jsonObj = json.loads(output)
        print(isinstance(jsonObj, dict))
        pprint.pprint(jsonObj['tistory']['item'])


    def writePost(self,title, content):
        '''
        post
        :param str:
        :return:
        '''
        target_url = 'https://www.tistory.com/apis/post/write'
        parameter = {'access_token': self.access_token,
                     'blogName': 'giraffeb',
                     'title' : title,
                     'content': content,
                     'output': 'json'}
        data = urllib.parse.urlencode(parameter).encode('utf-8')
        req = urllib.request.Request(target_url)
        res = urllib.request.urlopen(req, data=data)

        responseStr = res.read().decode('utf-8')

        print(responseStr)


