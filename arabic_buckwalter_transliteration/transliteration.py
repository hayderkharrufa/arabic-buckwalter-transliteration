def buckwalter_to_arabic(buckwalter):
    # Buckwalter to Arabic character map
    b2a = {  # mapping from Buckwalter to Arabic script
    u'b': u'\u0628', u'*': u'\u0630', u'T': u'\u0637', u'm': u'\u0645',
    u't': u'\u062a', u'r': u'\u0631', u'Z': u'\u0638', u'n': u'\u0646',
    u'^': u'\u062b', u'z': u'\u0632', u'E': u'\u0639', u'h': u'\u0647',
    u'j': u'\u062c', u's': u'\u0633', u'g': u'\u063a', u'H': u'\u062d',
    u'q': u'\u0642', u'f': u'\u0641', u'x': u'\u062e', u'S': u'\u0635',
    u'$': u'\u0634', u'd': u'\u062f', u'D': u'\u0636', u'k': u'\u0643',
    u'>': u'\u0623', u'\'': u'\u0621', u'}': u'\u0626', u'&': u'\u0624',
    u'<': u'\u0625', u'|': u'\u0622', u'A': u'\u0627', u'Y': u'\u0649',
    u'p': u'\u0629', u'y': u'\u064a', u'l': u'\u0644', u'w': u'\u0648',
    u'F': u'\u064b', u'N': u'\u064c', u'K': u'\u064d', u'a': u'\u064e',
    u'u': u'\u064f', u'i': u'\u0650', u'~': u'\u0651', u'o': u'\u0652'
}

    return ''.join(b2a.get(char, char) for char in buckwalter)


def arabic_to_buckwalter(arabic):
    # Arabic to Buckwalter character map
    a2b = {  # mapping from Arabic script to Buckwalter
    u'\u0628': u'b', u'\u0630': u'*', u'\u0637': u'T', u'\u0645': u'm',
    u'\u062a': u't', u'\u0631': u'r', u'\u0638': u'Z', u'\u0646': u'n',
    u'\u062b': u'^', u'\u0632': u'z', u'\u0639': u'E', u'\u0647': u'h',
    u'\u062c': u'j', u'\u0633': u's', u'\u063a': u'g', u'\u062d': u'H',
    u'\u0642': u'q', u'\u0641': u'f', u'\u062e': u'x', u'\u0635': u'S',
    u'\u0634': u'$', u'\u062f': u'd', u'\u0636': u'D', u'\u0643': u'k',
    u'\u0623': u'>', u'\u0621': u'\'', u'\u0626': u'}', u'\u0624': u'&',
    u'\u0625': u'<', u'\u0622': u'|', u'\u0627': u'A', u'\u0649': u'Y',
    u'\u0629': u'p', u'\u064a': u'y', u'\u0644': u'l', u'\u0648': u'w',
    u'\u064b': u'F', u'\u064c': u'N', u'\u064d': u'K', u'\u064e': u'a',
    u'\u064f': u'u', u'\u0650': u'i', u'\u0651': u'~', u'\u0652': u'o'
}

    return ''.join(a2b.get(char, char) for char in arabic)