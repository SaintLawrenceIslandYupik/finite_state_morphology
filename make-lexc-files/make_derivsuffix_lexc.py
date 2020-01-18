'''
:author:      Hayley Park
:modified by: Emily Chen
:date:        2020

Given a list of Yupik NN, NV, VN, VV derivational suffixes
in .csv format, annotates each suffix for each inflection
class and prints them in lexc-compatible format. 

Usage: python make_derivsuffix_lexc.py -s [csv] -r [NN | NV | VN | VV]



                    # insert %: when printing
                    # {.c.} and {.w.} isn't a good pairing
                    # {.f.} and {.at.}
                    # won't handle special -te
                    # (g) isn't always {G}
                    #print("[ WARNING: check for roots that actually end in -ta ]")
        

'''
import argparse
import csv
import re 

from annotate_helper_methods import annotate_suffixes
from classify_helper_methods import classify_verb_root, \
                                        convert_to_base_form, classify_noun_root
from print_helper_methods import print_inflection_classes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--suffixes', '-s', type=str, help = 'path to file containing derivational suffixes')
    parser.add_argument('--suffix_type', '-t', type=str, help = 'type of derivational suffix: NN, NV, VV, VN')
    args = parser.parse_args()

    rootType   = ""  # type of root the derivational suffixes affix to
    resultType = ""  # type of root that results from affixing the derivational suffixes
    if args.suffix_type.startswith("N"):
        rootType = "Noun"
    else:
        rootType = "Verb"

    if args.suffix_type.endswith("N"):
        resultType = "Noun"
    else:
        resultType = "Verb"

    # annotate each suffix for each inflection class
    class2suffixes = annotate_suffixes(args.suffixes, rootType)

    # determine each suffix's continuation class
    idx2InflClass = { 0 : [],
                      1 : [],
                      2 : [],
                      3 : [],
                      4 : [],
                      5 : [],
                      6 : [],
                      7 : [],
                      8 : [],
                      9 : []
                    }

    for classIdx in class2suffixes.keys():

        # class2suffixes[0] lists the suffixes annotated in Jacobson (2001) Notation
        if classIdx == 0:
            jacobsonSuffixes = class2suffixes[classIdx].split("\n")

        else:
            annotatedSuffixes = class2suffixes[classIdx].split("\n")

            for i, suffixWithDefinition in enumerate(annotatedSuffixes):
                if suffixWithDefinition:
                    annotatedSuffix, definition = suffixWithDefinition.split(",", 1)
        
                    # buggy...
                    # desired behavior will not delete -w, but will delete - at the end of the suffix
                    jacobsonSuffix = re.sub('-|$', '', jacobsonSuffixes[i].split(",", 1)[0])
        
                    # determine the derivational suffix's continuation class
                    if resultType == "Noun":
                        suffix = convert_to_base_form(annotatedSuffix)
                        classIdx = classify_noun_root(suffix)
                    else:
                        suffix = annotatedSuffix[:-1]
                        classIdx = classify_verb_root(suffix)
        
                    suffixMapping = jacobsonSuffix + "[" + rootType[0] + "." + resultType[0] + "]" + ":^" + suffix
                    idx2InflClass[classIdx].append((suffixMapping, definition))

    print_inflection_classes("DerixSuffix", resultType, idx2InflClass)


if __name__ == "__main__":
    main()
