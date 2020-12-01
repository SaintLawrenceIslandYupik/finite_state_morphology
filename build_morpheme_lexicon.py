'''
:author: Emily Chen
:date:   2020

'''
import glob


NOUN_ROOT_FILES = "lexc-files/roots/noun/*"


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


def convert_to_cv(word):
    '''
    :param word: the word to convert
    :type word: str

    :return: list of tuples

    Converts the given word into C(onsonant)s and V(owel)s

    '''
    CONSONANTS = ['Ngngw', 'ngngw', 'Ghhw', 'ghhw', 'Ngng', 'ngng',
                  'Ghh', 'gh', 'Ghw', 'ghw', 'Ngw', 'ngw',
                  'Gg', 'gg', 'Gh', 'gh', 'Kw', 'kw', 'Ll', 'll',
                  'Mm', 'mm', 'Ng', 'ng', 'Nn', 'nn', 'Qw', 'qw',
                  'Rr', 'rr', 'Wh', 'wh',
                  'F', 'f', 'G', 'g', 'H', 'h', 'K', 'k', 'L', 'l',
                  'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r',
                  'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'Y', 'y', 'Z', 'z']

    FULL_VOWELS = ['A', 'a', 'I', 'i', 'U', 'u']

    tokenized = tokenize(word)

    result = []

    for grapheme in tokenized:
        if grapheme in CONSONANTS:
            result.append((grapheme, "C"))
        elif grapheme in FULL_VOWELS:
            result.append((grapheme, "V"))
        else:
            result.append((grapheme, grapheme))

    return result


def make_noun_root_lexicon(NOUN_ROOT_FILES):
    '''
    :param:
    :type:

    '''
    root_inventory = []

    for filename in glob.glob(NOUN_ROOT_FILES):
        with open(filename, 'r') as f:
            for line in f:

                # check if current line actually contains a root
                if "NounTag" in line:
                    root    = line.split(" ")[0].split(":")[0].split("*")[0]
                    root_cv = convert_to_cv(root)

                    if filename.endswith("semiFinalE.txt") and root.isalpha():
                        root_inventory.append(root)

                        # alloforms for roots that end in -g, -w, -ghw
                        #   e.g. atkug, atku
                        if filename.endswith("g-w-ghw.txt"):
                            if root.endswith("g"):
                                root_inventory.append(root[:-1])
                            elif root.endswith("ghw"):
                                root_inventory.append(root[:-3])
                            elif root.endswith("w"):
                                root_inventory.append(root[:-1])

                        # alloforms for roots that end in -gh
                        # including weak, strong, marked strong
                        #   e.g. naayvagh, naayva (weak)
                        #   e.g. kaviigh, kavii (strong)
                        #   e.g. aakagh*, aaka (marked strong)
                        if filename.endswith("weakGH.txt") or \
                           filename.endswith("markedStrongGH.txt") or \
                           filename.endswith("strongGH.txt"):
                            root_inventory.append(root[:-2])

                        # alloforms for roots that end in -te
                        #   e.g. ggute, ggu, gguut OR yughaghte, yughagh, yughaght
                        if filename.endswith("te.txt"):
                            root_inventory.append(root[:-2])

                            cv = [tup[1] for tup in root_cv]
                            if ''.join(cv) == "VCe":
                                root_inventory.append(root_cv[0][0] + root_cv[0][0] + root_cv[1][0])
                            elif ''.join(cv) == "CVCe":
                                root_inventory.append(root_cv[0][0] + root_cv[1][0] + root_cv[1][0] + root_cv[2][0])
                            else:
                                root_inventory.append(root[:-1])

                        # alloforms for roots that end in semi-final e
                        #   e.g. ategh, ate, aatgh OR aghvegh, aghve
                        #        aveg, ave, aavg OR angyaleg, angyale
                        if filename.endswith("semiFinalE.txt"):
                            if root.endswith("gh"):
                                root_inventory.append(root[:-2])
                            elif root.endswith("g"):
                                root_inventory.append(root[:-1])

                            cv = [tup[1] for tup in root_cv]
                            if ''.join(cv) == "VCeC":
                                root_inventory.append(root_cv[0][0] + root_cv[0][0] + root_cv[1][0] + root_cv[3][0])
                            elif ''.join(cv) == "CVCeC":
                                root_inventory.append(root_cv[0][0] + root_cv[1][0] + root_cv[1][0] + root_cv[2][0] + root_cv[4][0])

                        # alloforms for roots that end in final -e, hop or no hop
                        #   e.g. iqe, iiq OR nalle, naall OR suupe, suup
                        if filename.endswith("finalE-hop.txt") or \
                           filename.endswith("finalE-noHop.txt"):
                            cv = [tup[1] for tup in root_cv]

                            if ''.join(cv) == "VCe":
                                root_inventory.append(root_cv[0][0] + root_cv[0][0] + root[1][0])
                            elif ''.join(cv) == "CVCe":
                                root_inventory.append(root_cv[0][0] + root_cv[1][0] + root_cv[1][0] + root_cv[2][0])
                            else:
                                root_inventory.append(root[:-1])

    return root_inventory



if __name__ == "__main__":

    root_inventory = make_noun_root_lexicon(NOUN_ROOT_FILES)
    print(root_inventory)
