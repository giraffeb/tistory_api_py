import myOAuth
import codecs
import json

class ConfigFileManager:
    filePath = ''
    config = None

    def __init__(self, filePath):
        self.filePath = filePath

        try:
            self.loadConficFile()
        except Exception as e:
            print(e)
            if isinstance(e, FileNotFoundError):
                self.initConficFile()


    def initConficFile(self):
        initconfig = {'tistory_access_token':'',
                      'github_access_token':''}

        self.config = initconfig

        with codecs.open(self.filePath, 'w', 'utf-8') as f:
            json.dump(initconfig, f)

    def loadConficFile(self):

        with codecs.open(self.filePath, 'r', 'utf-8') as f:
            self.config = json.load(f)


    def saveAccessToken(self, caller, token):
        if isinstance(caller, myOAuth.Tistory_OAuth) == True:
            self.config['tistory_access_token'] = token
            with codecs.open(self.filePath, 'w+', 'utf-8') as f:
                json.dump(self.config, f)

        # if isinstance(caller, myOAuth.Tistory_OAuth) == True:

'''
상태
1) 파일이 최소 생성됨
2) 이전에 파일에 생성한 적이 있음
3) 파일은 생성되었지만 엑세스토큰이 저장되어 있지 않음
4) 엑세스 토큰이 저장되어 있지만, expire되었음

해결
1) 초기화로 파일을 저장함.
1-1) 파일이 최초 생성인지 알아야 함 : file exist로 확인가능
2, 3) file을 json.loads()해서 값이 존재하는지 확인
4) expire는 요청해봐야 알 수 잇음 ( 차후 구현 )

'''

