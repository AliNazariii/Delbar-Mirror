# speech.py
# speechrecognition, pyaudio, brew install portaudio
import speech_recognition as sr
import os
import requests
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import json
import arabic_reshaper
from bidi.algorithm import get_display

class Speech(object):
    def __init__(self, launch_phrase="آینه آینه", debugger_enabled=False):
        self.launch_phrase = launch_phrase
        self.debugger_enabled = debugger_enabled
        self.__debugger_microphone(enable=False)

    def listen_for_audio(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
            self.__debugger_microphone(enable=True)
            print(get_display(arabic_reshaper.reshape('در حال گوش دادن به صدای شما')))
            audio = r.listen(source)

        open('temp-wav.wav', 'wb').write(audio.get_wav_data())

        self.__debugger_microphone(enable=False)
        print(get_display(arabic_reshaper.reshape('صدای شما دریافت شد')))

        proxies1 = {'http': 'http://81.171.29.251:11495'}
        addr1 = 'http://5.202.178.217:8025/ASR/DoASRAnyWave'
        headers1 = {  'accept': 'application/json' }
        ftmp = open('temp-wav.wav', 'rb')
        data1 = { 'item' : ('temp-wav.wav', ftmp.read(), 'audio/wav') }
        res = requests.post(addr1, files = data1, proxies=proxies1, headers = headers1)
        speech = json.loads(res.json())['data'][0]['text']
        print(get_display(arabic_reshaper.reshape(speech)))
        return speech

    def is_call_to_action(self, speech):
        if speech is not None and self.launch_phrase in speech:
            print(get_display(arabic_reshaper.reshape('آینه فعال شد')))
            return True
        return False

    def synthesize_text(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("tmp.mp3")
        song = AudioSegment.from_mp3("tmp.mp3")
        play(song)
        os.remove("tmp.mp3")

    def __debugger_microphone(self, enable=True):
        if self.debugger_enabled:
            try:
                r = requests.get("http://localhost:8080/microphone?enabled=%s" % str(enable))
                if r.status_code != 200:
                    print("Used wrong endpoint for microphone debugging")
            except Exception as e:
                print(e)
