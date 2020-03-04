# bot.py

# speechrecognition, pyaudio, brew install portaudio
import sys
sys.path.append("./")

import requests
import datetime
import dateutil.parser
import json
import traceback
from nlg_us import NLG
from speech_us import Speech
from knowledge_us import Knowledge
from vision_us import Vision

my_name = "Ali"
launch_phrase = "سلام"
use_launch_phrase = True
weather_api_token = "abb58408ed4cc40ac3e456f9c5c0b44c"
debugger_enabled = True
camera = 0


class Bot(object):
    def __init__(self):
        self.nlg = NLG(user_name=my_name)
        self.speech = Speech(launch_phrase=launch_phrase, debugger_enabled=debugger_enabled)
        self.knowledge = Knowledge(weather_api_token)
        self.vision = Vision(camera=camera)

    def start(self):
        while True:
            requests.get("http://localhost:8080/tosan_center/face")
            if self.vision.recognize_face():
                print ("Found face")
                if use_launch_phrase:
                    speech_res = self.speech.listen_for_audio()
                    if self.speech.is_call_to_action(speech_res):
                        self.__acknowledge_action()
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
            else: # No recognized speech
                self.__text_action("I'm sorry, I don't know about that yet.")
                return

            self.decide_action()

    def __acknowledge_action(self):
        self.__text_action(self.nlg.acknowledge())

    def __text_action(self, text=None):
        if text is not None:
            requests.get("http://localhost:8080/statement?text=%s" % text)
            self.speech.synthesize_text(text)

if __name__ == "__main__":
    bot = Bot()
    bot.start()
