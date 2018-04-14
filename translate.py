from googletrans import Translator
import re

# Definitely shouldn't repeat the translate block 4 times, could condense with a function


def translate(string, lang1, lang2, lang3):
    translator = Translator()
    trans_string = str(translator.translate(string, lang1, 'en'))  # First translation, english to lang1
    regex = r"(?<=text=)(.*)(?=, pronunciation)"  # Looks only for text between "text=" and ", pronunciation"
    matches = re.search(regex, trans_string)  # Matches the regex pattern to the output of googleTrans
    cleaned_translation = matches.group(0)  # String with just the translated text

    trans_string = str(translator.translate(cleaned_translation, lang2, lang1))  # Second trans, lang1 > lang2
    regex = r"(?<=text=)(.*)(?=, pronunciation)"
    matches = re.search(regex, trans_string)
    cleaned_translation = matches.group(0)

    trans_string = str(translator.translate(cleaned_translation, lang3, lang2))  # Third trans, lang2 > lang3
    regex = r"(?<=text=)(.*)(?=, pronunciation)"
    matches = re.search(regex, trans_string)
    cleaned_translation = matches.group(0)

    trans_string = str(translator.translate(cleaned_translation, 'en', lang3))  # Second trans, lang3 > english
    regex = r"(?<=text=)(.*)(?=, pronunciation)"
    matches = re.search(regex, trans_string)
    cleaned_translation = matches.group(0)

    return cleaned_translation

