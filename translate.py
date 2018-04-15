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


##googletrans
##The MIT License (MIT)
##
##Copyright (c) 2015 SuHun Han
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.