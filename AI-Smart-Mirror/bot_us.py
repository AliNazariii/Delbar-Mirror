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
            elif speech_res == 'greeting':
                self.__text_action(self.nlg.greet())
            elif speech_res == 'snow white':
                self.__text_action(self.nlg.snow_white())
            # elif speech == 'maps':
            #     self.__maps_action(entities)
            # elif speech == 'holidays':
            #     self.__holidays_action()
            # elif speech == 'appearance':
            #     self.__appearance_action()
            # elif speech == 'user status':
            #     self.__user_status_action(entities)
            # elif speech == 'user name':
            #     self.__user_name_action()
            # elif speech == 'personal status':
            #     self.__personal_status_action()
            # elif speech == 'insult':
            #     self.__insult_action()
            #     return
            # elif speech == 'appreciation':
            #     self.__appreciation_action()
            #     return
            else: # No recognized speech
                self.__text_action("I'm sorry, I don't know about that yet.")
                return

            self.decide_action()

    def __user_status_action(self, nlu_entities=None):
        attribute = None

        if (nlu_entities is not None) and ("Status_Type" in nlu_entities):
            attribute = nlu_entities['Status_Type'][0]['value']

        self.__text_action(self.nlg.user_status(attribute=attribute))

    def __user_name_action(self):
        if self.nlg.user_name is None:
            self.__text_action("I don't know your name. You can configure it in bot.py")

        self.__text_action(self.nlg.user_name)

    def __appearance_action(self):
        requests.get("http://localhost:8080/face")

    def __appreciation_action(self):
        self.__text_action(self.nlg.appreciation())

    def __acknowledge_action(self):
        self.__text_action(self.nlg.acknowledge())

    def __insult_action(self):
        self.__text_action(self.nlg.insult())

    def __personal_status_action(self):
        self.__text_action(self.nlg.personal_status())

    def __text_action(self, text=None):
        if text is not None:
            requests.get("http://localhost:8080/statement?text=%s" % text)
            self.speech.synthesize_text(text)

    def __maps_action(self, nlu_entities=None):

        location = None
        map_type = None
        if nlu_entities is not None:
            if 'location' in nlu_entities:
                location = nlu_entities['location'][0]["value"]
            if "Map_Type" in nlu_entities:
                map_type = nlu_entities['Map_Type'][0]["value"]

        if location is not None:
            maps_url = self.knowledge.get_map_url(location, map_type)
            maps_action = "Sure. Here's a map of %s." % location
            body = {'url': maps_url}
            requests.post("http://localhost:8080/image", data=json.dumps(body))
            self.speech.synthesize_text(maps_action)
        else:
            self.__text_action("I'm sorry, I couldn't understand what location you wanted.")

    def __holidays_action(self):
        holidays = self.knowledge.get_holidays()
        next_holiday = self.__find_next_holiday(holidays)
        requests.post("http://localhost:8080/holidays", json.dumps({"holiday": next_holiday}))
        self.speech.synthesize_text(self.nlg.holiday(next_holiday['localName']))

    def __find_next_holiday(self, holidays):
        today = datetime.datetime.now()
        for holiday in holidays:
            date = holiday['date']
            if (date['day'] > today.day) and (date['month'] > today.month):
                return holiday

        # next year
        return holidays[0]

if __name__ == "__main__":
    bot = Bot()
    bot.start()
