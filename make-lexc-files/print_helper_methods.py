'''
:author: Emily Chen
:date:   2020

Methods related to printing Yupik lexical items
and their continuation classes in a lexc-compatible format.

'''
from operator import itemgetter

def print_inflection_classes(lexicalItemType, resultType, idx2InflClass):
    '''
    :param lexicalItemType: "Root" or "DerivSuffix"
    :type lexicalItemType: str
    :param resultType: type of root that results from using/suffixing
                       lexical items in the given inflection class:
                       either "Noun" or "Verb"
    :type resultType: str
    :param idx2InflClass: dictionary where each key is the
                          index of an inflection class and
                          each value is a list of
                          (lexicalItem, definition) tuples
    :type idx2InflClass: dict

    Janky print function to print each lexical item in each
    inflection class in lexc-compatible format.

    '''
    for i in range(1, len(idx2InflClass)):
        if idx2InflClass[i]:

            romanNumeral = idx_to_roman_numeral(i)

            print("-" * 22 + "-" * len(romanNumeral))
            print(resultType + " Inflection Class " + romanNumeral)
            print("-" * 22 + "-" * len(romanNumeral))

            # get length of longest root or derivational suffix in the
            # inflection class in order to properly calculate padding
            maxLength = get_max_length(lexicalItemType, resultType, i, idx2InflClass[i])

            # for class of roots or derivational suffixes that end in -g, -w, -ghw
            if resultType == "Noun" and i == 2:
                for lexitem, definition in idx2InflClass[i]:

                    # if lexical item ends in -w, add %{k%} -->  kiiw:kii%{k%}w
                    if lexitem[-1] == "w" and ''.join(lexitem[-3:-1]) != "gh":

                        if lexicalItemType == "Root":
                            padding = maxLength - (len(lexitem) * 2 + 6) + 2
                            print(lexitem+ ":" + lexitem[:-1] + "%{k%}w" + " " * padding + \
                                  resultType + "Postbase" + romanNumeral + "; ! " + definition)

                        elif lexicalItemType == "DerivSuffix":
                            padding = maxLength - (len(lexitem) + 5) + 2
                            print(lexitem[:-1] + "%{k%}w" + " " * padding + \
                                  resultType + "Postbase" + romanNumeral + "; ! " + definition)

                    # otherwise lexical item ends in -g or -ghw
                    else:
                        padding = maxLength - len(lexitem) + 2
                        print(lexitem+ " " * padding + resultType + "Postbase" + romanNumeral + \
                              "; ! " + definition)

            # for class of noun roots that end in weak -gh
            #   add %{g%} --> nasaperagh:nasapera%{g%}h
            elif resultType == "Noun" and i == 3:
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - (len(root) * 2 + 5) + 2
                    print(root + ":" + root[:-2] + "%{g%}h" + " " * padding + \
                          resultType + "Postbase" + romanNumeral + "; ! " + definition)

            # for class of noun roots that end in marked strong -gh (*)
            #   remove * at the end of the root, e.g. afsengagh*  --> afsengagh
            elif resultType == "Noun" and i == 4:
                for root, definition in idx2InflClass[i]:
                    padding = maxLength - len(root) + 2
                    print(root[:-1] + " " * padding + resultType + "Postbase" + romanNumeral + \
                          "; ! " + definition)

            # for class of roots or derivational suffixes that end in -te
            #   if root ends in -te, replace t with %{t%} --> riigte:riig%{t%}e
            elif (resultType == "Noun" and i == 6 or
                  resultType == "Verb" and i == 5):
                for lexitem, definition in idx2InflClass[i]:

                    if lexicalItemType == "Root":
                        padding = maxLength - (len(lexitem) * 2 + 5) + 2
                        print(lexitem+ ":" + lexitem[:-2] + "%{t%}e" + " " * padding + \
                              resultType + "Postbase" + romanNumeral + "; ! " + definition)

                    elif lexicalItemType == "DerivSuffix":
                        padding = maximum - (len(root) + 4) + 2
                        print(lexitem[:-2] + "%{t%}e" + " " * padding + \
                              resultType + "Postbase" + i + "; ! " + definition)

            else:
                for lexitem, definition in idx2InflClass[i]:
                    padding = maxLength - len(lexitem) + 2
                    print(lexitem + " " * padding + resultType + "Postbase" + romanNumeral + \
                          "; ! " + definition)
            print()

    # print roots or derivational suffixes that could not be classified,
    # usually those with non-traditional endings
    if idx2InflClass[0]:
        maxLength = get_max_length(lexicalItemType, "None", 0, idx2InflClass[0])

        print("----------------------------------")
        print("Items that Could Not Be Classified")
        print("----------------------------------")
        for lexitem, definition in idx2InflClass[0]:
            padding = maxLength - len(lexitem) + 2
            print(lexitem + " " * padding + definition)
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
    return switcher.get(idx, "INDEX IS BORKED")


def get_max_length(lexicalItemType, resultType, classIdx, inflClass):
    '''
    :param lexicalItemType: "Root" or "DerivSuffix"
    :type lexicalItemType: str
    :param resultType: type of root that results from using/suffixing
                       lexical items in the given inflection class:
                       either "Noun" or "Verb"
    :type resultType: str
    :param classIdx: inflection class index
    :type classIdx: int
    :param inflClass: all lexical items in a given 
                      inflection class, where each item
                      is represented as a
                      (lexicalItem, definition) tuple
    :type inflClass: list of tuples

    Calculates the length of the longest root in the inflection
    class or the length of the longest "altered" root in the
    inflection class (takes foma-style symbols into account,
    i.e. %{k%}, %{g%}, %{t%})

    '''
    maxLength = len((sorted(inflClass, key=lambda x: len(x[0]), reverse=True)[0])[0])
    alteredMaxLength = 0

    # get length of longest -w root or derivational suffix with %{k%} inserted
    #   e.g. kii%{k%}w
    if resultType == "Noun" and classIdx == 2:
        for pair in inflClass:
            lexitem = pair[0]
            if lexitem[-1] == "w":
                if lexicalItemType == "Root":
                    alteredLength = len(lexitem) * 2 + 6  # len(lexitem) * 2 + 6 since
                                                       # e.g. kiiw -> kiiw:kii%{k%}w
                elif lexicalItemType == "DerivSuffix":
                    alteredLength = len(lexitem) + 5  # just adding %, {, k, %, }

                if alteredLength > alteredMaxLength:
                    alteredMaxLength = alteredLength

        if alteredMaxLength > maxLength:
            maxLength = alteredMaxLength

    # get length of longest weak -gh root with %{g%} inserted
    #                       -te root or derivational suffix with %{t%} inserted
    #   e.g. nasapera%{g%}h
    #        riig%{t%}e
    elif (resultType == "Noun" and classIdx == 3 or
          resultType == "Noun" and classIdx == 6 or
          resultType == "Verb" and classIdx == 5):
        if lexicalItemType == "Root":
            maxLength = maxLength * 2 + 5 # len(lexitem) * 2 + 5 since 
                                          # e.g. riigte -> riigte:riig%{t%}e
        elif lexicalItemType == "DerivSuffix":
            maxLength = maxLength + 4  # just adding %, {, %, }

    return maxLength


def print_other_roots(rootName, rootList):
    '''
    :param rootName: any other root in Yupik besides
                     noun and verb roots
    :type rootName: str
    :param rootList: list of "other" roots
    :type rootList: list of tuples

    Janky print function to print "other" roots in
    lexc-compatible format.

    '''
    print("-" * len(rootName))
    print(rootName)
    print("-" * len(rootName))

    # get length of longest root
    maxLength = len((sorted(rootList, key=lambda x: len(x[0]), reverse=True)[0])[0])

    for pair in rootList:
        root = pair[0]
        definition = pair[1]

        padding = maxLength - len(nonRoot) + 2
        print(root + " " * padding + "#; ! " + definition)

    print()
