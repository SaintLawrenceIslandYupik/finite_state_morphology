'''
:author: Emily Chen
:date:   2019

Given a root list in .csv format, classifies each root
into its respective inflection class.

Eventually, this script should automatically generate
the lexc files from the completed Yupik database.

NOTE: There are several problem children for this script
      when it comes to identifying part of speech,
      especially if "particle" or "?" appears in the
      definition of a noun root or verb root (e.g. tefli-).

Usage: python3 classify.py [dirname]
'''
import argparse
import csv
import glob
from operator import itemgetter

from methods_for_classify import classify_verb_root, \
                                 convert_to_base_form, classify_noun_root


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname', help = 'name of directory containing word lists')
    args = parser.parse_args()

    # initialize verbal inflection classes
    idx2VerbClass = { 0 : [],  # cannot be classified
                      1 : [],  # ends in -a, -i, -u
                      2 : [],  # ends in -e
                      3 : [],  # ends in -g, -w, -ghw
                      4 : [],  # ends in -agh, -igh, -ugh,
                               #   -egh if -e cannot drop/hop
                      5 : [],  # ends in -te
                      6 : [],  # ends in special -te
                      7 : [],  # ends in semi-final -e
                    }

    # initialize nominal inflection classes
    idx2NounClass = { 0 : [],  # cannot be classified
                      1 : [],  # ends in -a, -i, -u
                      2 : [],  # ends in -g, -w, -ghw
                      3 : [],  # ends in weak -gh
                      4 : [],  # ends in marked strong -gh
                      5 : [],  # ends in strong -gh
                      6 : [],  # ends in -te
                      7 : [],  # ends in semi-final -e
                      8 : [],  # ends in final -e that
                               # can drop and hop
                      9 : []   # ends in final -e that
                               # can drop but not hop
                    }

    # initialize list of particles
    particles = []

    # initialize list of question words
    questionWords = []

    # initialize list of postural roots
    posturalRoots = []

    # initialize list of emotional roots 
    emotionalRoots = []

    for filename in glob.glob(args.dirname + "/*"):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')

            for line in reader:
                #if "particle" in line[1]:
                #    particles.append((line[0], line[1]))

                #elif "?" in line[1]:
                #    questionWords.append((line[0], line[1]))

                if "postural root" in line[1]:
                    posturalRoots.append((line[0], line[1]))

                elif "emotional root" in line[1]:
                    emotionalRoots.append((line[0], line[1]))

                else: 
                    root = line[0]

                    # verb roots are annotated with a hyphen at the end
                    if root[-1] == "-":
                        verbRoot = root[:-1]
                        classIdx = classify_verb_root(verbRoot)
                        idx2VerbClass[classIdx].append((verbRoot, line[1]))

                    else:
                        nounRoot = convert_to_base_form(root)
                        classIdx = classify_noun_root(nounRoot)
                        idx2NounClass[classIdx].append((nounRoot, line[1]))

    print_inflection_classes("Verb", idx2VerbClass)
    print_inflection_classes("Noun", idx2NounClass)

    if particles:
        print_nonroots("Particles", particles)

    if questionWords:
        print_nonroots("Question Words", questionWords)

    if posturalRoots:
        print_nonroots("Postural Roots", posturalRoots)

    if emotionalRoots:
        print_nonroots("Emotional Roots", emotionalRoots)


if __name__ == "__main__":
    main()
