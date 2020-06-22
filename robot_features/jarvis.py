# user/bin/python
import speech_recognition
import pyttsx3
from enum import Enum
from gtts import gTTS
from logging import getLogger
import os
import sys
from exceptions import JarvisLanguageInvalid

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


class JarvisLanguageSupport(Enum):
    """
    Defined languages support for Jarvis
    """
    en = 'en-EN'
    vi = 'vi-VN'


class JarvisSpeak:
    """
    Jarvis Speak
    """

    @staticmethod
    def __speak_english(say, speed=JarvisSpeakSpeed.fast.value):
        """
        Speak from text
        :return:
        """
        # Init engine speak
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)
        engine.say(say)
        engine.runAndWait()
        return True

    @staticmethod
    def __speak_vietnamese(say):
        """
        Speak Vietnamese
        :param say:
        :return:
        """
        tts = gTTS(text=say, lang=JarvisLanguageSupport.vi.name)
        tts.save("jarvis.mp3")
        _app = 'afplay'
        if sys.platform == 'linux' or sys.platform == 'linux2':
            _app = ''
        elif sys.platform == "darwin":
            _app = 'afplay'
        elif sys.platform == "win32":
            _app = 'call'
        os.system(f"{_app} jarvis.mp3")
        return True

    @staticmethod
    def _speak(say, language=JarvisLanguageSupport.en.name, speed=JarvisSpeakSpeed.fast.value):
        """
        Speak
        :param say:
        :param language:
        :param speed
        :return:
        """
        if language != JarvisLanguageSupport.en.name and language != JarvisLanguageSupport.vi.name:
            logger.error('Jarvis does not support your language yet.')
            raise JarvisLanguageInvalid
        if language == JarvisLanguageSupport.vi.name:
            logger.info('Jarvis speaks Vietnamese')
            return JarvisSpeak().__speak_vietnamese(say=say)
        else:
            logger.info('Jarvis speaks English')
            return JarvisSpeak().__speak_english(say=say, speed=speed)


class JarvisListen:
    """
    Jarvis Listen
    """

    @staticmethod
    def _listen(duration=5, language=JarvisLanguageSupport.en.value):
        """
        Jarvis listen, support English and Vietnamese only
        :return: string which the Jarvis listen from you
        """
        if language != JarvisLanguageSupport.en.value and language != JarvisLanguageSupport.vi.value:
            logger.error('Jarvis does not support your language yet.')
            raise JarvisLanguageInvalid
        if language == JarvisLanguageSupport.vi.value:
            logger.info('Jarvis listen Vietnamese')
        else:
            logger.info('Jarvis listen English')
        return JarvisListen().__listen(duration=duration, language=language)

    @staticmethod
    def __listen(duration=5, language=JarvisLanguageSupport.en.value):
        """
        Listen English
        :param duration:
        :param language
        :return:
        """
        with speech_recognition.Microphone() as mic:
            logger.info("Jarvis: I'm listening")
            bot_ear = speech_recognition.Recognizer()
            audio = bot_ear.record(mic, duration=duration)
        try:
            you_say = bot_ear.recognize_google(audio, language=language)
            logger.info("You say: " + you_say)
        except speech_recognition.UnknownValueError:
            logger.error("I don't know what do you say. Please try again")
            return None


class Jarvis(JarvisListen, JarvisSpeak):
    """
    Javis robot
    """

    @staticmethod
    def speak(say="hello", speed=JarvisSpeakSpeed.fast.value, language=JarvisLanguageSupport.en.name):
        """
        Speak from text
        :return:
        """
        return JarvisSpeak._speak(say=say, speed=speed, language=language)

    @staticmethod
    def listen(duration=5, language=JarvisLanguageSupport.en.value):
        """
        Jarvis listen, support English and Vietnamese only
        :return: string which the Jarvis listen from you
        """
        return JarvisListen._listen(duration=duration, language=language)
