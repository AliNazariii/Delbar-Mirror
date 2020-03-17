# bot.py

# speechrecognition, pyaudio, brew install portaudio
import sys
sys.path.append("./")

import requests
import datetime
import dateutil.parser
import json
import traceback
from speech_us import Speech
from vision_us import Vision
import arabic_reshaper
from bidi.algorithm import get_display

my_name = "Ali"
launch_phrase = "سلام"
use_launch_phrase = True
weather_api_token = "abb58408ed4cc40ac3e456f9c5c0b44c"
debugger_enabled = True
camera = 0


class Bot(object):
    def __init__(self):
        self.speech = Speech(launch_phrase=launch_phrase, debugger_enabled=debugger_enabled)
        self.vision = Vision(camera=camera)

    def start(self):
        while True:
            requests.get("http://localhost:8080/tosan_center/face")
            if self.vision.recognize_face():
                print(get_display(arabic_reshaper.reshape('چهره تشخیص داده شد')))
                if use_launch_phrase:
                    speech_res = self.speech.listen_for_audio()
                    if self.speech.is_call_to_action(speech_res):
                        self.decide_action()
                else:
                    self.decide_action()

    def decide_action(self):
        speech_res = self.speech.listen_for_audio()

        if speech_res is not None:
            if 'اخبار' in speech_res:
                print(get_display(arabic_reshaper.reshape('اخبار')))
                requests.get("http://localhost:8080/tosan_center/news")
            elif 'جوک' in speech_res:
                print(get_display(arabic_reshaper.reshape('جوک')))
                requests.get("http://localhost:8080/tosan_center/news")
            elif 'هوا' in speech_res:
                print(get_display(arabic_reshaper.reshape('هوا')))
                requests.get("http://localhost:8080/tosan_center/news")
            elif 'خوب' in speech_res:
                print(get_display(arabic_reshaper.reshape('خوب')))
                proxies1 = {'http': 'http://81.171.29.251:11495'}
                addr1 = 'http://5.202.178.217:8025/TTS/DoTTS'
                headers1 = {  'accept': 'application/json' }
                data1 = "{\"Text\":\"123\",\"Username\":\"test\",\"Password\":\"test\"}"
                res = requests.post(addr1, data=data1, proxies=proxies1, headers=headers1)
                open('temp2-wav.wav', 'wb').write(res.content)
            else: # No recognized speech
                self.__text_action("I'm sorry.")
                return

            self.decide_action()

    def __text_action(self, text=None):
        if text is not None:
            self.speech.synthesize_text(text)

if __name__ == "__main__":
    bot = Bot()
    bot.start()