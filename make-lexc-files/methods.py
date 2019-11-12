'''
:author: Emily Chen
:date:   2019

Methods for the Python script that classifies Yupik roots
into their respective inflection classes.

'''
def tokenize(word):
    '''
    :param word: the word to tokenize into graphemes
    :type word: str

    :return: list

    Tokenizes a given Yupik word into its respective graphemes

    '''
    GRAPHEMES = ['Ngngw', 'ngngw', 'Ghhw', 'ghhw', 'Ngng', 'ngng',
                 'Ghh', 'gh', 'Ghw', 'ghw', 'Ngw', 'ngw',
                 'Gg', 'gg', 'Gh', 'gh', 'Kw', 'kw', 'Ll', 'll',
                 'Mm', 'mm', 'Ng', 'ng', 'Nn', 'nn', 'Qw', 'qw',
                 'Rr', 'rr', 'Wh', 'wh',
                 'Aa', 'aa', 'Ii', 'ii', 'Uu', 'uu',
                 'A', 'a', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                 'I', 'i', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
                 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                 'U', 'u', 'V', 'v', 'W', 'w', 'Y', 'y', 'Z', 'z']

    result = []

    end = len(word)
    while end > 0:
        foundGrapheme = False

        # attempts to greedy match graphemes starting
        # from the end of the word
        for grapheme in GRAPHEMES:
            if word.endswith(grapheme, 0, end):
                result.insert(0, grapheme)
                end -= len(grapheme)
                foundGrapheme = True
                break

        # if a grapheme was not found, just prepend
        # the character to the final result
        if not foundGrapheme:
            result.insert(0, word[end-1:end])
            end -= 1

    return result


def convert_to_c_v(word):
    '''
    :param word: the word to convert
    :type word: str

    :return: list

    Converts the given word into C(onsonant)'s and V(owel)'s

    '''
    CONSONANTS = ['Ngngw', 'ngngw', 'Ghhw', 'ghhw', 'Ngng', 'ngng',
                 'Ghh', 'gh', 'Ghw', 'ghw', 'Ngw', 'ngw',
                 'Gg', 'gg', 'Gh', 'gh', 'Kw', 'kw', 'Ll', 'll',
                 'Mm', 'mm', 'Ng', 'ng', 'Nn', 'nn', 'Qw', 'qw',
                 'Rr', 'rr', 'Wh', 'wh',
                 'F', 'f', 'G', 'g', 'H', 'h', 'K', 'k', 'L', 'l',
                 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r',
                 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'Y', 'y', 'Z', 'z']

    VOWELS = ['Aa', 'aa', 'Ii', 'ii', 'Uu', 'uu',
              'A', 'a', 'I', 'i', 'U', 'u', 'E', 'e']

    tokenized = tokenize(word)

    result = []

    for grapheme in tokenized:
        if grapheme in CONSONANTS:
            result.append("C")
        elif grapheme in VOWELS:
            result.append("V")
        else:
            result.append(grapheme)

    return result


def classify_verb_root(root):
    '''
    :param root: verb root
    :type root: str

    :return: int

    Classifies the given verb root into one
    of seven inflectional classes for verbs.

    '''
    cv = convert_to_c_v(root)

    # root ends in -a, -i, -u
    if (root[-1] == "a" or
        root[-1] == "i" or
        root[-1] == "u"):
        return 1

    # root ends in -e
    elif (root[-2] != "t" and
          root[-1] == "e"):
        return 2

    # root ends in -w or -ghw
    elif (root[-1] == "w" or
          root[-3:] == "ghw"):
        return 3

    # root ends in -g
    elif root[-1] == "g":

        # root ends in -eg
        if root[-2] == "e":

            # root is of the form VCeg
            if (len(cv) == 4 and cv[0] == "V"):
                # eCeg -> -e can drop but not hop
                if root[0] == "e":
                    return 7
                # [aa|ii|uu]Ceg -> -e can drop but not hop
                elif (''.join(root[0:2]) == "aa" or
                      ''.join(root[0:2]) == "ii" or
                      ''.join(root[0:2]) == "uu"):
                    return 7
                else:
                    return 6

            # root is of the form CVCeg
            elif (len(cv) == 5 and cv[0] == "C"):
                # CeCeg -> -e can drop but not hop
                if root[1] == "e":
                    return 7
                # [aa|ii|uu]Ceg -> -e can drop but not hop
                elif (''.join(root[1:3]) == "aa" or
                      ''.join(root[1:3]) == "ii" or
                      ''.join(root[1:3]) == "uu"):
                    return 7
                else:
                    return 6

            # root is too short or ends with CCeg
            # -e cannot drop or hop
            elif (len(cv) < 4 or ''.join(cv[-4:-2]) == "CC"):
                return 3

            # root does not end with CCeg and is longer than (C)VCeg
            # -e can drop but not hop
            elif (len(cv) > 5 and ''.join(cv[-4:-2]) != "CC"):
                return 7

        # root ends in -ag, -ig, -ug,
        else:
            return 3

    # root ends in -agh, -igh, -ugh
    elif (root[-3:] == "agh" or
          root[-3:] == "igh" or
          root[-3:] == "ugh"):
        return 4

    # root ends in -te
    elif root[-2:] == "te":
        return 5

    # root ends in semi-final -e
    #    -e hops if the word is of
    #    the form "(C) V C e g h" where
    #    V is not -e
    elif (root[-3:] == "egh"):

        # root is of the form VCegh
        if (len(cv) == 4 and cv[0] == "V"):
            # eCegh -> -e can drop but not hop
            if root[0] == "e":
                return 7
            # [aa|ii|uu]Cegh -> -e can drop but not hop
            elif (''.join(root[0:2]) == "aa" or
                  ''.join(root[0:2]) == "ii" or
                  ''.join(root[0:2]) == "uu"):
                return 7
            else:
                return 6

        # root is of the form CVCegh
        elif (len(cv) == 5 and cv[0] == "C"):
            # CeCegh -> -e can drop but not hop
            if root[1] == "e":
                return 7
            # [aa|ii|uu]Cegh -> -e can drop but not hop
            elif (''.join(root[1:3]) == "aa" or
                  ''.join(root[1:3]) == "ii" or
                  ''.join(root[1:3]) == "uu"):
                return 7
            else:
                return 6

        # root is too short or ends with CCegh
        # -e cannot drop or hop
        elif (len(cv) < 4 or ''.join(cv[-4:-2]) == "CC"):
            return 4

        # root does not end with CCegh and is longer than (C)VCegh
        # -e can drop but not hop
        elif (len(cv) > 5 and ''.join(cv[-4:-2]) != "CC"):
            return 7

        # root is of the form (C)VCegh
        # -e can drop and hop
        else:
            return 6

    return -1


def convert_to_base_form(root):
    '''
    :param root: noun inflected for the
                 absolutive singular
    :type root: str

    :return: str

    Converts the given noun, inflected for the
    absolutive singular, to its base form as
    defined on Jacobson (2001) pg. 12.

    '''
    if root[-2:] == "ae":
        return (root[:-2] + "e")

    elif root[-2:] == "ta":
        return (root[:-2] + "te")

    elif root[-1] == "n":
        return (root[:-1] + "te")

    elif root[-2:] == "q*":
        return (root[:-2] + "gh*")

    elif root[-1] == "q":
        return (root[:-1] + "gh")

    elif root[-1] == "k":
        return (root[:-1] + "g")

    elif root[-2:] == "kw":
        return (root[:-2] + "w")

    elif root[-2:] == "qw":
        return (root[:-2] + "ghw")

    return root


def classify_noun_root(root):
    '''
    :param root: noun root
    :type root: str

    :return: int
             representing the appropriate
             nominal inflection class

    Classifies the given noun root into one
    of 10 inflectional classes for nouns.

    '''
    cv = convert_to_c_v(root)

    # root ends in -a, -i, -u
    if (root[-1] == "a" or
        root[-1] == "i" or
        root[-1] == "u"):
        return 1

    # root ends in -w or -ghw
    elif (root[-1] == "w" or
          root[-3:] == "ghw"):
        return 2

    # root ends in -g
    elif root[-1] == "g":

        # root ends in -eg
        if root[-2] == "e":

            # root is of the form VCeg
            if (len(cv) == 4 and cv[0] == "V"):
                # eCeg -> -e can drop but not hop
                if root[0] == "e":
                    return 7
                # [aa|ii|uu]Ceg -> -e can drop but not hop
                elif (''.join(root[0:2]) == "aa" or
                      ''.join(root[0:2]) == "ii" or
                      ''.join(root[0:2]) == "uu"):
                    return 8
                else:
                    return 7

            # root is of the form CVCeg
            elif (len(cv) == 5 and cv[0] == "C"):
                # CeCeg -> -e can drop but not hop
                if root[1] == "e":
                    return 8
                # [aa|ii|uu]Ceg -> -e can drop but not hop
                elif (''.join(root[1:3]) == "aa" or
                      ''.join(root[1:3]) == "ii" or
                      ''.join(root[1:3]) == "uu"):
                    return 8
                else:
                    return 7

            # root is too short or ends with CCeg
            # -e cannot drop or hop
            elif (len(cv) < 4 or ''.join(cv[-4:-2]) == "CC"):
                return 2

            # root does not end with CCeg and is longer than (C)VCeg
            # -e can drop but not hop
            elif (len(cv) > 5 and ''.join(cv[-4:-2]) != "CC"):
                return 8

        # root ends in -ag, -ig, -ug,
        else:
            return 2

    # root ends in weak -gh
    elif (root[-2:] == "gh" and
          root[-3] != "e"   and
          root[-3] != root[-4]):
        return 3

    # root ends in marked strong -gh
    elif root[-3:] == "gh*":
        return 4

    # root ends in strong -gh
    elif (root[-2:] == "gh"   and
          (root[-4:-2] == "aa" or
          root[-4:-2] == "ii" or
          root[-4:-2] == "uu")):
        return 5

    # root ends in -te
    elif root[-2:] == "te":
        return 6

    # root ends in semi-final -e
    #    -e hops if the word is of
    #    the form "(C) V C e g h" where
    #    V is not -e
    elif (root[-3:] == "egh"):

        # root is of the form VCegh
        if (len(cv) == 4 and cv[0] == "V"):
            # eCegh -> -e can drop but not hop
            if root[0] == "e":
                return 8 
            # [aa|ii|uu]Cegh -> -e can drop but not hop
            elif (''.join(root[0:2]) == "aa" or
                  ''.join(root[0:2]) == "ii" or
                  ''.join(root[0:2]) == "uu"):
                return 8
            else:
                return 7

        # root is of the form CVCegh
        elif (len(cv) == 5 and cv[0] == "C"):
            # CeCegh -> -e can drop but not hop
            if root[1] == "e":
                return 8
            # [aa|ii|uu]Cegh -> -e can drop but not hop
            elif (''.join(root[1:3]) == "aa" or
                  ''.join(root[1:3]) == "ii" or
                  ''.join(root[1:3]) == "uu"):
                return 8
            else:
                return 7

        # root is too short or ends with CCegh
        # -e cannot drop or hop
        elif (len(cv) < 4 or ''.join(cv[-4:-2]) == "CC"):
            return 5

        # root does not end with CCegh and is longer than (C)VCegh
        # -e can drop but not hop
        elif (len(cv) > 5 and ''.join(cv[-4:-2]) != "CC"):
            return 8

        # root is of the form (C)VCegh
        # -e can drop and hop
        else:
            return 7

    # root ends in final -e
    #    -e hops if the root is of
    #    the form "(C) V C e" where
    #    V is not -e
    elif (root[-1] == "e"):

        # root is of the form VCe
        if (len(cv) == 3 and cv[0] == "V"):
            # eCe -> -e can drop but not hop
            if root[0] == "e":
                return 10
            # [aa|ii|uu]Ce -> -e can drop but not hop
            elif (''.join(root[0:2]) == "aa" or
                  ''.join(root[0:2]) == "ii" or
                  ''.join(root[0:2]) == "uu"):
                return 10
            else:
                return 9

        # root is of the form CVCe
        elif (len(cv) == 4 and cv[0] == "C"):
            # CeCe -> -e can drop but not hop
            if root[1] == "e":
                return 10
            # [aa|ii|uu]Ce -> -e can drop but not hop
            elif (''.join(root[1:3]) == "aa" or
                  ''.join(root[1:3]) == "ii" or
                  ''.join(root[1:3]) == "uu"):
                return 10
            else:
                return 9

        # root is longer than (C)VCe or
        # of the form ...CCe
        # -e can drop but not hop
        elif (len(cv) > 4 or ''.join(cv[-3:-1]) == "CC"):
            return 10

        # root is of the form (C)VCe
        # -e can drop and hop
        else:
            return 9

    return -1
