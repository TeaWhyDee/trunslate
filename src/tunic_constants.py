from enum import Enum, auto


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


phoneme_to_enum = {
    # Vowels
    'æ'   : TUNIC_PHONEMES.A,   # back, sad
    'ɑːr' : TUNIC_PHONEMES.AR,  # arm, large
    'ɑːɹ' : TUNIC_PHONEMES.AH,  # swan, box
    'eɪ'  : TUNIC_PHONEMES.AY,  # bay, game
    'ɛ'   : TUNIC_PHONEMES.E,   # end, pet
    'iː'  : TUNIC_PHONEMES.EE,  # bee, team
    'ɪɹ'  : TUNIC_PHONEMES.EER, # near, here
    'ə'   : TUNIC_PHONEMES.EH,  # the, about
    'ɐ'   : TUNIC_PHONEMES.EH,
    'ɛɹ'  : TUNIC_PHONEMES.ERE, # air, vary
    'ɪ'   : TUNIC_PHONEMES.I,   # bit rich
    'aɪ'  : TUNIC_PHONEMES.IE,  # guy life
    'ɜː'  : TUNIC_PHONEMES.IR,  # bird work
    'oʊ'  : TUNIC_PHONEMES.OH,  # toe over
    'ɔɪ'  : TUNIC_PHONEMES.OI,  # toy avoid
    'uː'  : TUNIC_PHONEMES.OO,  # too june
    'ʊ'   : TUNIC_PHONEMES.OU,  # wolf good
    'aʊ'  : TUNIC_PHONEMES.OW,  # how hour
    'ʊɹ'  : TUNIC_PHONEMES.ORE, # your cure
    # Consonants
    '': TUNIC_PHONEMES.B,
    '': TUNIC_PHONEMES.CH,
    '': TUNIC_PHONEMES.D,
    '': TUNIC_PHONEMES.F,
    '': TUNIC_PHONEMES.G,
    '': TUNIC_PHONEMES.H,
    '': TUNIC_PHONEMES.J,
    '': TUNIC_PHONEMES.K,
    '': TUNIC_PHONEMES.L,
    '': TUNIC_PHONEMES.M,
    '': TUNIC_PHONEMES.N,
    '': TUNIC_PHONEMES.NG,
    '': TUNIC_PHONEMES.P,
    '': TUNIC_PHONEMES.R,
    '': TUNIC_PHONEMES.S,
    '': TUNIC_PHONEMES.SH,
    '': TUNIC_PHONEMES.T,
    '': TUNIC_PHONEMES.TH,
    '': TUNIC_PHONEMES.TH_HARD,
    '': TUNIC_PHONEMES.V,
    '': TUNIC_PHONEMES.W,
    '': TUNIC_PHONEMES.Y,
    '': TUNIC_PHONEMES.Z,
    '': TUNIC_PHONEMES.ZH,
}
