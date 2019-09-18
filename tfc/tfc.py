from .notify import Notify
from .translate import Translate

from json import loads
from time import sleep
from xerox import paste

class Translation():
    def __init__(self, config):
        self.config = config

        self.translate = Translate(self.config)
        self.notify = Notify()

    def start(self):
        temp_value = ''

        while True:
            recent_value = paste()
            if recent_value != temp_value:
                result = self.translate.send_request(recent_value)
                if result['status'] == True:
                    self.notify.send(recent_value, result['response'])
                else:
                    print('Error: ' + str(result['response']))

            temp_value = recent_value
            sleep(2)
