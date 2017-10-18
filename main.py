import myOAuth
import ConfigFileManager
import TistoryAPI

def main():
    configFilePath = 'configFile.txt'

    # print('start')
    configFileManager = ConfigFileManager.ConfigFileManager(configFilePath)
    tistroy = myOAuth.Tistory_OAuth(configFileManager)
    tistroy.requestCode()

    api = TistoryAPI.TistoryAPI(tistroy)
    api.getList()
    api.writePost("hello", "test for api")


if __name__ == '__main__':
    main()