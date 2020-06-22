import requests


class WhatTheWeatherToday:
    """
    Get the weather to day for HaNoi, VN
    """
    __default_api_key = '9d5107745868c31431c395157bbd986a'
    __default_city_name = 'Hanoi'
    __base_url = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key=None, city_name=None):
        """
        :param api_key:
        :param city_name:
        """
        self.api_key = self.__default_api_key
        if api_key:
            self.api_key = api_key
        self.city_name = self.__default_city_name
        if city_name:
            self.city_name = city_name

    def get_the_weather_info(self):
        """
        Get the weather information
        :return:
        """
        url = f'{self.__base_url}?appid={self.__default_api_key}&q={self.city_name}'
        respond = requests.get(url)
        data = respond.json()
        if data['cod'] == '404':
            return 'Do not get the weather, please check your internet connection.', None
        weather_data = data['main']
        # Get temperature, convert Kevil to Celsius
        current_temperature = weather_data['temp'] - 273.15
        # store the value corresponding
        current_humidiy = weather_data["humidity"]
        return current_temperature, current_humidiy

    @staticmethod
    def analysis_the_temperature(temperature):
        """
        temperature
        :return:
        """
        temperature = int(temperature)
        if 34 > temperature > 30:
            return 'hot'
        elif 30 > temperature > 20:
            return 'cool'
        elif temperature < 20:
            return 'cold'
        else:
            return 'very hot'

    @staticmethod
    def analysis_the_humidity(humidity):
        """
        Analysis the humidity
        :param humidity:
        :return:
        """
        if humidity > 80:
            return 'It may rain, you should take the umbrella!'
        else:
            return 'Hot and Dry weather, you should be careful when going out!'

    def get_the_weather_today(self):
        """

        :return:
        """
        current_temp, current_humidiy = self.get_the_weather_info()
        temperature = self.analysis_the_temperature(current_temp)
        rain_analysis = self.analysis_the_humidity(current_humidiy)
        weather_text = f"The weather today is {temperature}, " \
                       f"Temperature is {int(current_temp)}, {rain_analysis}, Humidity is {current_humidiy} percent"
        print(weather_text)
        return weather_text
