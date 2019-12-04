"""
Get translate from Google Translate
author: "Peng Huang"
USAGE:
    python3 googleTranslate.py <text to be translated>
eg:
    python3 googleTranslate.py "hello word"
"""
"""
version 1.0
2019.11.30
The default output is English
"""

from googletrans import Translator
import sys

class GoogleTranslate(object):
    def __init__(self, query_string=sys.argv[1]):
        self.query_string = query_string.replace("\n", " ")
        self.result = ""
    def get_translation(self):
        translator = Translator()
        self.result += translator.translate(self.query_string, dest='zh-CN').text

if __name__ == '__main__':
    translation = GoogleTranslate()
    translation.get_translation()
    print(translation.query_string)
    print("\n")
    print(translation.result)
