'''
:author: Emily Chen
:date:   2020

Methods related to printing Yupik lexical items
and their continuation classes in a lexc-compatible format.

'''
from operator import itemgetter

def print_inflection_classes(inflType, idx2InflClass):
    '''
    :param inflType: "Noun" or "Verb"
    :type inflType: str
    :param idx2InflClass: dictionary where each key is an
                          inflection class and its value
                          is a list of roots that belong to
                          that inflection class
    :type idx2InflClass: dict

    Janky print function to print each root in each
    inflection class in lexc-compatible format.

    '''
    for i in range(1, len(idx2InflClass)):
        if idx2InflClass[i]:

            romanNumeral = idx_to_roman_numeral(i)

            print("-" * 22 + "-" * len(romanNumeral))
            print(inflType + " Inflection Class " + romanNumeral)
            print("-" * 22 + "-" * len(romanNumeral))

            # get length of longest root in inflection class
            # in order to properly calculate padding
            maxLength = get_max_length(inflType, i, idx2InflClass[i])

            # class of noun roots that end in -g, -w, -ghw
            if inflType == "Noun" and i == 2:
                for root, definition in idx2InflClass[i]:
                    # if noun root ends in -w, add %{k%} -->  kiiw:kii%{k%}w
                    if root[-1] == "w" and ''.join(root[-3:-1]) != "gh":
                        padding = maxLength - (len(root) * 2 + 6) + 2
                        print(root + ":" + root[:-1] + "%{k%}w" + " " * padding + \
                              inflType + "Postbase" + romanNumeral + "; ! " + definition)
                    else:
                        padding = maxLength - len(root) + 2
                        print(root + " " * padding + inflType + "Postbase" + romanNumeral + \
                              "; ! " + definition)

            # class of noun roots that end in weak -gh
            #   add %{g%} --> nasaperagh:nasapera%{g%}h
            elif inflType == "Noun" and i == 3:
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - (len(root) * 2 + 5) + 2
                    print(root + ":" + root[:-2] + "%{g%}h" + " " * padding + \
                          inflType + "Postbase" + romanNumeral + "; ! " + definition)

            # class of noun roots that end in marked strong -gh (*)
            #   remove * at the end of the root, e.g. afsengagh*  --> afsengagh
            elif inflType == "Noun" and i == 4:
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - len(root) + 2
                    print(root[:-1] + " " * padding + inflType + "Postbase" + romanNumeral + \
                          "; ! " + definition)

            # class of roots that end in -te
            #   if root ends in -te, add %{t%} --> riigte:riig%{t%}e
            elif (inflType == "Noun" and i == 6 or
                  inflType == "Verb" and i == 5):
                print()
                print("[ WARNING: check for roots that actually end in -ta ]")
                print()
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - (len(root) * 2 + 5) + 2
                    print(root + ":" + root[:-2] + "%{t%}e" + " " * padding + \
                          inflType + "Postbase" + romanNumeral + "; ! " + definition)

            else:
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - len(root) + 2
                    print(root + " " * padding + inflType + "Postbase" + romanNumeral + \
                          "; ! " + definition)
            print()

    # print roots that could not be classified, usually those with non-traditional endings
    if idx2InflClass[0]:
        maxLength = get_max_length("None", 0, idx2InflClass[0])

        print("-------------------------------------------")
        print(inflType + " Roots (?) that Could Not Be Classified")
        print("-------------------------------------------")
        for root, definition in idx2InflClass[0]:
            padding = maxLength - len(root) + 2
            print(root + " " * padding + definition)
    print()


def idx_to_roman_numeral(idx):
    '''
    :param idx: index of inflection class
    :type idx: int

    :return: str

    Converts the given index to its
    Roman numeral counterpart.

    '''
    switcher = { 1: "I"   ,
                 2: "II"  ,
                 3: "III" ,
                 4: "IV"  ,
                 5: "V"   ,
                 6: "VI"  ,
                 7: "VII" ,
                 8: "VIII",
                 9: "IX"  ,
               }
    return switcher.get(idx, "nothing...")


def get_max_length(inflType, classIdx, inflClass):
    '''
    :param inflType: "Noun" or "Verb"
    :type inflType: str
    :param classIdx: inflection class index
    :type classIdx: int
    :param inflClass: the inflection class where each
                      element is a tuple: (root, definition)
    :type inflClass: list of tuples

    Calculates the length of the longest root in the inflection
    class or the length of the longest "altered" root in the
    inflection class (takes foma-style symbols into account,
    i.e. %{k%}, %{g%}, %{t%})

    '''
    maxLength = len((sorted(inflClass, key=lambda x: len(x[0]), reverse=True)[0])[0])
    alteredMaxLength = 0

    # get length of longest -w root with %{k%} inserted
    #   e.g. kii%{k%}w
    if inflType == "Noun" and classIdx == 2:
        for pair in inflClass:
            root = pair[0]
            if root[-1] == "w":
                alteredLength = len(root) * 2 + 6  # adding :, %, {, k, %, }
                if alteredLength > alteredMaxLength:
                    alteredMaxLength = alteredLength

        if alteredMaxLength > maxLength:
            maxLength = alteredMaxLength

    # get length of longest weak -gh root with %{g%} inserted
    #                       -te root with %{t%} inserted
    #   e.g. nasapera%{g%}h
    #        riig%{t%}e
    elif (inflType == "Noun" and classIdx == 3 or
          inflType == "Noun" and classIdx == 6 or
          inflType == "Verb" and classIdx == 5):
        maxLength = maxLength * 2 + 5 # adding :, %, {, %, }

    return maxLength


def print_nonroots(nonRootType, nonRootList):
    '''
    :param nonRootType: "Particles" or "Question Words"
    :type nonRootType: str
    :param nonRootList: list of non-roots
    :type nonRootList: list of tuples

    Janky print function to print each non-root (particle
    or question word) in lexc-compatible format.

    '''
    print("-" * len(nonRootType))
    print(nonRootType)
    print("-" * len(nonRootType))

    # get length of longest noun-root
    maxLength = len((sorted(nonRootList, key=lambda x: len(x[0]), reverse=True)[0])[0])

    for pair in nonRootList:
        nonRoot = pair[0]
        definition = pair[1]

        padding = maxLength - len(nonRoot) + 2
        print(nonRoot + " " * padding + "#; ! " + definition)

    print()
