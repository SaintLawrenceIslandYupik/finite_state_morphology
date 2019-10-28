'''
:author: Emily Chen
:date:   2019

Given a word list in .csv format, classifies each word
into its respective inflection class.

Eventually, this script should automatically generate
the lexc files from the completed Yupik database.

'''
import argparse
import csv
import glob
from operator import itemgetter

from methods import classify_verb_root, \
                    convert_to_base_form, classify_noun_root


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
                 10: "X" 
               } 
    return switcher.get(idx, "nothing...") 


def print_inflection_classes(inflType, idx2InflClass):
    '''
    :param inflType: "Noun" or "Verb"
    :type inflType: str
    :param idx2InflClass: dictionary where each key is an
                          inflection class # and its value
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

            # get length of longest root in the inflection class
            maxLength = len((sorted(idx2InflClass[i], key=lambda x: len(x[0]), reverse=True)[0])[0])

            for pair in idx2InflClass[i]:
                root = pair[0]
                definition = pair[1]

                padding = maxLength - len(root) + 2
                print(root + " " * padding + inflType + "Suffix" + romanNumeral + \
                      "; ! " + definition)

            print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname', help = 'name of directory containing word lists')
    args = parser.parse_args()

    # initialize verbal inflection classes
    idx2VerbClass = { 1 : [],  # ends in -a, -i, -u
                      2 : [],  # ends in -e
                      3 : [],  # ends in -g, -w, -ghw
                      4 : [],  # ends in -agh, -igh, -ugh,
                               #   -egh if -e cannot drop/hop
                      5 : [],  # ends in -te 
                      6 : [],  # ends in semi-final -e that
                               # can drop and hop
                      7 : [],  # ends in semi-final -e that
                               # can drop but not hop
                     -1 : []   # cannot be classified
                    }

    # initialize nominal inflection classes
    idx2NounClass = { 1 : [],  # ends in -a, -i, -u
                      2 : [],  # ends in -g, -w, -ghw
                      3 : [],  # ends in weak -gh
                      4 : [],  # ends in marked strong -gh 
                      5 : [],  # ends in strong -gh
                      6 : [],  # ends in -te 
                      7 : [],  # ends in semi-final -e that
                               # can drop and hop
                      8 : [],  # ends in semi-final -e that
                               # can drop but not hop
                      9 : [],  # ends in final -e that
                               # can drop and hop
                     10 : [],  # ends in final -e that
                               # can drop but not hop
                     -1 : []   # cannot be classified
                    }

    for filename in glob.glob(args.dirname + "/*"):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')

            for line in reader:
                if "particle" not in line[1]:
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


if __name__ == "__main__":
    main()
