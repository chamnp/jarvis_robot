# bin/python3

from googletrans import Translator
from untils.logger import init_logger
import logging
from robot_features.jarvis import Jarvis

logger = logging.getLogger(__name__)


class GoogleTranslate(Jarvis):
    """
    Translate English to Vietnam
    """
    def __init__(self, src_language='en', des_language='vi'):
        self.src_language = src_language
        self.des_language = des_language

    def translate(self, text='Hello'):
        """
        Translate text
        :param text:
        :return:
        """
        trans = Translator().translate(text=text, dest=self.des_language, src=self.src_language)
        logger.debug(trans.text)
        Jarvis.speak(trans.text)
        return trans.text


if __name__ == '__main__':
    init_logger()
    text = 'Speak'
    translate = GoogleTranslate().translate(text)
    logger.debug(translate)
