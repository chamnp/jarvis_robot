from robot_features.the_weather.weather_today import WhatTheWeatherToday
from robot_features.date_time.what_time_is_it import WhatTimeIsIt
from robot_features.jarvis import Jarvis


class JarvisRobot(Jarvis):
    """
    Call Jarvis
    """
    def __init__(self):
        super(JarvisRobot, self).__init__()

    def run(self):
        robot_ear = None
        self.speak('Hello Cham, Can I help you?')
        weather = WhatTheWeatherToday().get_the_weather_today()
        self.speak(weather)
        while not robot_ear:
            robot_ear = self.listen()
        if 'weather' in robot_ear.lower():
            weather = WhatTheWeatherToday().get_the_weather_today()
            self.speak(weather)
        elif 'time is it' in robot_ear:
            now = WhatTimeIsIt().get_the_date_time()
            self.speak(now)
        self.speak('Goodbye Cham!')


if __name__ == '__main__':
    jarvis = JarvisRobot()
    jarvis.run()
