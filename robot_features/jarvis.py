# user/bin/python
import speech_recognition
import pyttsx3
from enum import Enum
from gtts import gTTS
from logging import getLogger
import os
import sys

logger = getLogger(__name__)


class JarvisSpeakSpeed(Enum):
    """
    Define speed speak for Javis
    """
    very_slow = 120
    slow = 150
    medium = 175
    fast = 190
    very_fast = 200


class Jarvis:
    """
    Javis robot
    """

    @staticmethod
    def speak(say="hello", speed=JarvisSpeakSpeed.fast.value):
        """
        Speak from text
        :return:
        """
        # Init engine speak
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)
        engine.say(say)
        engine.runAndWait()

    @staticmethod
    def speak_vietnamese(say="Xin Chao", speed=JarvisSpeakSpeed.fast.value):
        """
        Speak Vietnamese
        :param say:
        :param speed:
        :return:
        """
        tts = gTTS(text=say, lang='vi')
        tts.save("jarvis.mp3")
        _app = 'afplay'
        if sys.platform == 'linux' or sys.platform == 'linux2':
            _app = ''
        elif sys.platform == "darwin":
            _app = 'afplay'
        elif sys.platform == "win32":
            _app = 'call'
        os.system(f"{_app} jarvis.mp3")

    def listen(self, duration=5, language=None):
        """
        Jarvis listen
        :return: string which the Jarvis listen from you
        """
        with speech_recognition.Microphone() as mic:
            logger.info("Jarvis: I'm listening")
            bot_ear = speech_recognition.Recognizer()
            audio = bot_ear.record(mic, duration=duration)
        if audio:
            you_say = bot_ear.recognize_google(audio)
            logger.info("You say: " + you_say)
        else:
            you_say = "I don't know what do you say. Please try again"
            self.speak(you_say)
            return None
