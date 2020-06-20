import speech_recognition
from process_data.the_weather.weather_today import WhatTheWeatherToday
from process_data.date_time.what_time_is_it import WhatTimeIsIt
import pyttsx3


JAVIS_READ_SPEED = {
    'very slow': 120,
    'slow': 150,
    'medium': 175,
    'fast': 190,
    'very fast': 200
}


class JavisRobot:
    """
    Call Javis
    """
    def __init__(self, javis_brain=''):
        self.javis_brain = javis_brain

    @staticmethod
    def javis_speak(javis_say="hello", speed=JAVIS_READ_SPEED['slow']):
        """
        Speak from text
        :return:
        """
        # Init engine speak
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)
        engine.say(javis_say)
        engine.runAndWait()

    def javis_listen(self):
        """

        :return:
        """
        with speech_recognition.Microphone() as mic:
            print("Javis: I'm listening")
            bot_ear = speech_recognition.Recognizer()
            audio = bot_ear.record(mic, duration=5)
        try:
            you = bot_ear.recognize_google(audio)
            print("\nYou say: " + you)
        except:
            you = "I don't know what do you say. Please try again"
            self.javis_speak(you, speed=JAVIS_READ_SPEED['very fast'])
            return None
        return you

    def run(self):
        robot_ear = None
        self.javis_speak('Hello Cham, Can I help you?', speed=JAVIS_READ_SPEED['fast'])
        while not robot_ear:
            robot_ear = self.javis_listen()
        if 'weather' in robot_ear.lower():
            weather = WhatTheWeatherToday().get_the_weather_today()
            self.javis_speak(weather)
        elif 'time is it' in robot_ear:
            now = WhatTimeIsIt().get_the_date_time()
            self.javis_speak(now, speed=JAVIS_READ_SPEED['fast'])
        self.javis_speak('Goodbye Cham!', speed=JAVIS_READ_SPEED['fast'])


if __name__ == '__main__':
    javis = JavisRobot()
    javis.run()
