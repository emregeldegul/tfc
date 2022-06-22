from time import sleep

from .notify import Notify

from googletrans import Translator
from xerox import paste


class Translation:
    def __init__(self, dest, src):
        self.translate = Translator()
        self.notify = Notify()
        self.dest = dest
        self.src = src

    def start(self):
        temp_value = ""

        while True:
            recent_value = paste()
            if recent_value != temp_value:
                try:
                    result = self.translate.translate(recent_value, dest=self.dest, src=self.src)
                    self.notify.send(recent_value, result.text)
                except Exception as e:
                    self.notify.send("A Problem Occurred", str(e))

            temp_value = recent_value
            sleep(2)
