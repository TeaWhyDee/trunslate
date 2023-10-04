import sys
from phonemizer import phonemize
from phonemizer.separator import Separator

from tunic_constants import phoneme_to_enum, TUNIC_PHONEMES

text = sys.argv[1:]
words = " ".join(text).split(" ")

phonemes = phonemize(
    words,
    language='en-us',
    separator=Separator(phone='|', word='='),
    preserve_punctuation=True,
    njobs=4)

# print(phonemes)

for word in phonemes:
    print(word.split("|")[0:-1])

