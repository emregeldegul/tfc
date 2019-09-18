from requests import get
from json import loads

class Translate():
    def __init__(self, config):
        self.key = config['key']
        self.lang = config['lang']

    # TODO: Language detection feature will be added

    def send_request(self, text):
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        param = {"key": self.key, "text": text, "lang": self.lang, "format": "plain"}

        try:
            request = get(url, param)
            if request.ok:
                response = loads(request.text)['text'][0]
                payload = {'status': True, 'response': response}
            else:
                response = loads(request.text)['message']
                payload = {'status': False, 'response': response}

        except Exception as e:
            payload = {'status': False, 'response': str(e)}

        finally:
            return payload
