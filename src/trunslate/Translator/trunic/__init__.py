from enum import Enum, auto
from typing import List

from phonemizer import phonemize
from phonemizer.separator import Separator

from trunslate.Translator import Translator


# def trunic_split_function(text) -> List[str]:

err = {}


class TrunicTranslator(Translator):
    def split_function(self, text) -> List[List[str]]:
        """ 
        Returns List of words.
        Each word is a list of 
        """
        words = text.split()
        self.original_words = words

        phonemes = phonemize(
            words,
            language='en-us',
            separator=Separator(phone='|', word='='),
            preserve_punctuation=True,
            njobs=4)
        
        split_words = []
        for word in phonemes:
            split_words.append(word.split("|")[0:-1])

        # SPLIT MUTI PHONEME WORDS BY =
        # for word in phonemes:
        #     for real_word in word[0:-1].split("="):
        #         split_words.append(real_word.split("|")[0:-1])

        return split_words

    def symbols_to_enum(self, words: List[List[str]]):
        enums = []
        for i in range(len(words)):
            word = words[i]
            for sym in word:
                try:
                    enums.append(phoneme_to_enum[sym])
                except KeyError as e:
                    to_append = f"{''.join(word)} | {self.original_words[i]}"
                    if not sym in err:
                        err[sym] = [to_append]
                    else:
                        err[sym].append(to_append)
                    # print(e)
        
        for i in err:
            comb = []
            for j in range(len(err[i])):
                comb.append("".join(err[i][j]))

            print(f"{i}\t:\t {',     '.join(comb[:3])}")
        return enums




class TUNIC_PHONEMES(Enum):
    A       = auto()
    AR      = auto()
    AH      = auto()
    AY      = auto()
    E       = auto()
    EE      = auto()
    EER     = auto()
    EH      = auto()
    ERE     = auto()
    I       = auto()
    IE      = auto()
    IR      = auto()
    OH      = auto()
    OI      = auto()
    OO      = auto()
    OU      = auto()
    OW      = auto()
    ORE     = auto()
    B       = auto()
    CH      = auto()
    D       = auto()
    F       = auto()
    G       = auto()
    H       = auto()
    J       = auto()
    K       = auto()
    L       = auto()
    M       = auto()
    N       = auto()
    NG      = auto()
    P       = auto()
    R       = auto()
    S       = auto()
    SH      = auto()
    T       = auto()
    TH      = auto()
    TH_HARD = auto()
    V       = auto()
    W       = auto()
    Y       = auto()
    Z       = auto()
    ZH      = auto()

# iə	:	 ɛɹiə | area,     ɹiəli | really,     ɛkspiəɹɪəns | experience
# oː	:	 foːɹəm | forum,     foːɹəmz | forums,     stoːɹi | story
# aɪʊɹ	:	 aɪʊɹz | hours,     aɪʊɹ | hour,     aɪʊɹsɛlvz | ourselves
# aɪə	:	 saɪəns | science,     səsaɪəɾi | society,     klaɪənt | client
# aɪɚ	:	 ɹɪkwaɪɚd | required,     ɹɪkwaɪɚmənts | requirements,     waɪɚləs | wireless
# =t	:	 ɹoʊmən=tuː | ii,     ɹoʊmən=twɛnti | xx
# ʔ	:	 ɹɪʔn̩ | written,     bʌʔn̩ | button,     kɑːʔn̩ | cotton
# n̩	:	 ɹɪʔn̩ | written,     bʌʔn̩ | button,     kɑːʔn̩ | cotton
# 	:	 aɪiː | ie,     lə | le
# =θ	:	 ɹoʊmən=θɹiː | iii
# =f	:	 ɹoʊmən=foːɹ | iv
# =s	:	 ɹoʊmən=sɪks | vi,     ɹoʊmən=sɛvən | vii
# r	:	 ʌrwə | urw,     bɹoʊʃʊɹr | brochure,     vɔɪjuːrwɛb | voyeurweb
# =ɪ	:	 ɹoʊmən=ɪlɛvən | xi
# =n	:	 ɹoʊmən=naɪn | ix
# =eɪ	:	 ɹoʊmən=eɪt | viii
# x	:	 lɪxtənstaɪn | liechtenstein

phoneme_to_enum = {
    # Vowels
    'æ'   : TUNIC_PHONEMES.A,   # back sad
    'ɑːr' : TUNIC_PHONEMES.AR,  # arm large
    'ɑːɹ' : TUNIC_PHONEMES.AH,  # swan box
    'eɪ'  : TUNIC_PHONEMES.AY,  # bay game
    'ɛ'   : TUNIC_PHONEMES.E,   # end pet
    'iː'  : TUNIC_PHONEMES.EE,  # bee team
    'ɪɹ'  : TUNIC_PHONEMES.EER, # near here
    'ə'   : TUNIC_PHONEMES.EH,  # the about
    'ɐ'   : TUNIC_PHONEMES.EH,  # an than       =
    'ɚ'   : TUNIC_PHONEMES.EH,  # our other     =
    'ɛɹ'  : TUNIC_PHONEMES.ERE, # air vary
    'ɪ'   : TUNIC_PHONEMES.I,   # bit rich
    'i'   : TUNIC_PHONEMES.I,   # any only city =
    'ᵻ'   : TUNIC_PHONEMES.I,   # unit>e<d servic>e<s =
    'aɪ'  : TUNIC_PHONEMES.IE,  # guy life
    'ɜː'  : TUNIC_PHONEMES.IR,  # bird work
    'oʊ'  : TUNIC_PHONEMES.OH,  # toe over
    'ʌ'   : TUNIC_PHONEMES.OH,  # of from was   =
    'ɑː'  : TUNIC_PHONEMES.OH,  # all law water =
    'ɔː'  : TUNIC_PHONEMES.OH,  # all law water
    'ɔ'   : TUNIC_PHONEMES.OH,  # off cost      =
    'ɔɪ'  : TUNIC_PHONEMES.OI,  # toy avoid
    'uː'  : TUNIC_PHONEMES.OO,  # too june
    'ʊ'   : TUNIC_PHONEMES.OU,  # wolf good
    'aʊ'  : TUNIC_PHONEMES.OW,  # how hour
    'ʊɹ'  : TUNIC_PHONEMES.ORE, # your cure
    'ɔːɹ' : TUNIC_PHONEMES.ORE, # for or order  =
    'oːɹ' : TUNIC_PHONEMES.ORE, # more store
    
    'əl'  : [TUNIC_PHONEMES.EH, TUNIC_PHONEMES.L], # peop>le<
    # Consonants
    'b': TUNIC_PHONEMES.B,
    'tʃ': TUNIC_PHONEMES.CH,
    'd': TUNIC_PHONEMES.D,
    'f': TUNIC_PHONEMES.F,
    'ɡ': TUNIC_PHONEMES.G,
    'h': TUNIC_PHONEMES.H,
    'dʒ': TUNIC_PHONEMES.J,
    'k': TUNIC_PHONEMES.K,
    'l': TUNIC_PHONEMES.L,
    'm': TUNIC_PHONEMES.M,
    'n': TUNIC_PHONEMES.N,
    'ŋ': TUNIC_PHONEMES.NG,
    'p': TUNIC_PHONEMES.P,
    'ɹ': TUNIC_PHONEMES.R,
    's': TUNIC_PHONEMES.S,
    'ʃ': TUNIC_PHONEMES.SH,
    't': TUNIC_PHONEMES.T,
    'ɾ': TUNIC_PHONEMES.T,  # da>t<a ci>t<y   =
    'θ': TUNIC_PHONEMES.TH,
    'ð': TUNIC_PHONEMES.TH_HARD,
    'v': TUNIC_PHONEMES.V,
    'w': TUNIC_PHONEMES.W,
    'j': TUNIC_PHONEMES.Y,
    'z': TUNIC_PHONEMES.Z,
    'ʒ': TUNIC_PHONEMES.ZH,
}

