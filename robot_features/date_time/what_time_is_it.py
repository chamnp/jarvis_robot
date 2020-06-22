from datetime import datetime


class WhatTimeIsIt:
    """
    Read the date time now
    """
    @staticmethod
    def get_the_date_time():
        """

        :return:
        """
        now = datetime.now()
        datetime_text = f"It's {now.hour}: {now.minute}"
        print(datetime_text)
        return datetime_text
