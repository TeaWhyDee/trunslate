import sys

from trunslate.Translator.trunic import TrunicTranslator


def main():
    text = " ".join(sys.argv[1:])
    # words = " ".join(text).split(" ")
    translators = [TrunicTranslator()]

    trunslator = translators[0]
    trunslator.process_text(text)


if __name__ == "__main__":
    main()
