from googletrans import Translator
import re

regex = r"(?<=text=)(.*)(?=, pronunciation)"


def translate(string, lang1, lang2, lang3):
    language_list = ['en', lang1, lang2, lang3, 'en']
    translator = Translator()
    cleaned_translation = string
    for i in range(4):
        trans_string = str(translator.translate(cleaned_translation, language_list[i + 1], language_list[i]))
        cleaned_translation = (re.search(regex, trans_string)).group(0)
    return cleaned_translation