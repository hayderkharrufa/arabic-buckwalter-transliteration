def buckwalter_to_arabic(buckwalter):
    # Buckwalter to Arabic character map
    b2a = {
        "'": '\u0621', # Hamza
        "|": '\u0622', # Maddah
        ">": '\u0623', # Alef with Hamza above
        "&": '\u0624', # Waw with Hamza above
        "<": '\u0625', # Alef with Hamza below
        "}": '\u0626', # Yeh with Hamza above
        "A": '\u0627', # Alef
        "b": '\u0628', # Beh
        "p": '\u0629', # Teh Marbuta
        "t": '\u062A', # Teh
        "^": '\u062B', # Theh
        "j": '\u062C', # Jeem
        "H": '\u062D', # Hah
        "x": '\u062E', # Khah
        "d": '\u062F', # Dal
        "*": '\u0630', # Thal
        "r": '\u0631', # Reh
        "z": '\u0632', # Zain
        "s": '\u0633', # Seen
        "$": '\u0634', # Sheen
        "S": '\u0635', # Sad
        "D": '\u0636', # Dad
        "T": '\u0637', # Tah
        "Z": '\u0638', # Zah
        "E": '\u0639', # Ain
        "g": '\u063A', # Ghain
        "_": '\u0640', # Tatweel
        "f": '\u0641', # Feh
        "q": '\u0642', # Qaf
        "k": '\u0643', # Kaf
        "l": '\u0644', # Lam
        "m": '\u0645', # Meem
        "n": '\u0646', # Noon
        "h": '\u0647', # Heh
        "w": '\u0648', # Waw
        "Y": '\u0649', # Alef Maksura
        "y": '\u064A',  # Yeh
        "F": '\u064B', # Fathatan
        "N": '\u064C', # Dammatan
        "K": '\u064D', # Kasratan
        "a": '\u064E', # Fatha
        "u": '\u064F', # Damma
        "i": '\u0650', # Kasra
        "~": '\u0651', # Shadda
        "o": '\u0652', # Sukun
    }

    return ''.join(b2a.get(char, char) for char in buckwalter)


def arabic_to_buckwalter(arabic):
    # Arabic to Buckwalter character map
    a2b = {
        '\u0621': "'", # Hamza
        '\u0622': "|", # Maddah
        '\u0623': ">", # Alef with Hamza above
        '\u0624': "&", # Waw with Hamza above
        '\u0625': "<", # Alef with Hamza below
        '\u0626': "}", # Yeh with Hamza above
        '\u0627': "A", # Alef
        '\u0628': "b", # Beh
        '\u0629': "p", # Teh Marbuta
        '\u062A': "t", # Teh
        '\u062B': "^", # Theh
        '\u062C': "j", # Jeem
        '\u062D': "H", # Hah
        '\u062E': "x", # Khah
        '\u062F': "d", # Dal
        '\u0630': "*", # Thal
        '\u0631': "r", # Reh
        '\u0632': "z", # Zain
        '\u0633': "s", # Seen
        '\u0634': "$", # Sheen
        '\u0635': "S", # Sad
        '\u0636': "D", # Dad
        '\u0637': "T", # Tah
        '\u0638': "Z", # Zah
        '\u0639': "E", # Ain
        '\u063A': "g", # Ghain
        '\u0640': "_", # Tatweel
        '\u0641': "f", # Feh
        '\u0642': "q", # Qaf
        '\u0643': "k", # Kaf
        '\u0644': "l", # Lam
        '\u0645': "m", # Meem
        '\u0646': "n", # Noon
        '\u0647': "h", # Heh
        '\u0648': "w", # Waw
        '\u0649': "Y", # Alef Maksura
        '\u064A': "y",  # Yeh
        '\u064B': "F", # Fathatan
        '\u064C': "N", # Dammatan
        '\u064D': "K", # Kasratan
        '\u064E': "a", # Fatha
        '\u064F': "u", # Damma
        '\u0650': "i", # Kasra
        '\u0651': "~", # Shadda
        '\u0652': "o", # Sukun
    }

    return ''.join(a2b.get(char, char) for char in arabic)