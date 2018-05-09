from googletrans import Translator
import re

regex = r"(?<=text=)(.*)(?=, pronunciation)"


def translate(input_string, lang1, lang2, lang3):
    language_list = ['en', lang1, lang2, lang3, 'en']
    translator = Translator()
    cleaned_translation = input_string
    for i in range(4):
        soiled_translation = str(translator.translate(cleaned_translation, language_list[i + 1], language_list[i]))
        cleaned_translation = (re.search(regex, soiled_translation)).group(0)
    return cleaned_translation
