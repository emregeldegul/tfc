from json import loads
from time import sleep
from xerox import paste
from requests import get
from subprocess import Popen
from os.path import join, expanduser, exists

class Translation():
    def __init__(self, config):
        self.key = config['key']
        self.lang = config['lang']

    def send_request(self, text):
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        param = {"key": self.key, "text": text, "lang": self.lang, "format": "plain"}

        try:
            request = get(url, param)
            payload = {'status': True, 'response': request}
        except Exception as e:
            payload = {'status': False, 'response': str(e)}
        finally:
            return payload

    def start(self):
        temp_value = ''

        while True:
            recent_value = paste()
            if recent_value != temp_value:
                result = self.send_request(recent_value)
                if result['status']:
                    response = result['response']
                    if response.ok:
                        text = loads(response.text)['text'][0]
                        Popen(["notify-send", "TFC Result:", f"{recent_value}: {text}"])
                        print(recent_value, ":", text)
                        print('='*50)
                    else:
                        print('Error: {}'.format(response.status_code))
                        print('='*50)
                else:
                    print('Error: {}'.format(result['response']))
                    print('='*50)

            temp_value = recent_value
            sleep(3)


if __name__ == '__main__':
    if not exists(join(expanduser("~"), '.tfc.config.json')):
        print('TFC Could Not Find The Configuration File.')
        exit(1)

    with open(join(expanduser("~"), '.tfc.config.json'), 'r') as configFile:
        config = loads(configFile.read())

    print('TFC listens To Your Clipboard For Translation.')
    print('='*50)

    translation = Translation(config)
    translation.start()
