'''
:author:      Hayley Park
:modified by: Emily Chen
:date:        2020

usage: python annotate_suffixes.py -s suffix_lists/intrg.txt -r Noun

'''
import argparse
import csv
import glob
import pprint
import re 

from collections import OrderedDict
from classify_roots import idx_to_roman_numeral
from methods_for_classify import classify_verb_root, \
                                 convert_to_base_form, classify_noun_root


 # Jacobson (2001) Notation <-> foma v.2 Notation
symbol_conversion = OrderedDict()
symbol_conversion["~sf"] = "%{.sf.%}"
symbol_conversion["~f"]  = "%{.f.%}"
symbol_conversion["~"]   = "%{.f.%}%{.sf.%}"
symbol_conversion["@"]   = "%{.at.%}"
symbol_conversion[":"]   = "%{.c.%}"
symbol_conversion["–"]   = "%{.m.%}"
symbol_conversion["-w"]  = "%{.w.%}"
symbol_conversion["(e)"] = "%{E%}"
symbol_conversion["(g)"] = "%{G%}"
symbol_conversion["+"]   = ""

rules_for_noun_roots = [ # Noun Class I: end in -a, -i, -u
                         {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v"},
                         # Noun Class II: end in -g, -w, -ghw
                         {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"v"},
                         # Noun Class III: end in weak -gh
                         {"%{E%}":"", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}", "%{.w.%}":"%{.w.%}", "%{.c.%}":"%{.c.%}"},
                         # Noun Class IV: end in marked strong -gh (*)
                         {"%{E%}":"%{E%}", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}", "%{.c.%}":"%{.c.%}"},
                         # Noun Class V: end in strong -gh
                         {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}"},
                         # Noun Class VI: end in -te 
                         {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}"},
                         # Noun Class VII: have semi-final -e
                         {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.sf.%}":"%{.sf.%}", "%{.m.%}":"%{.m.%}"},
                         # Noun Class VIII: end in -e that can be dropped but not hopped
                         {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}"},
                         # Noun Class IX: end in -e that can be dropped and hopped
                         {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}"}
                       ]

rules_for_verb_roots = [ # Verb Class I: end in -a, -i, -u
                         {"(g/t)": "%{G%}", "%{G%}":"%{G%}", "(t)":"", "(te)":""},
                         # Verb Class II: end in -e
                         {"(g/t)": "", "(t)":"", "(te)":"", "%{.f.%}": "%{.f.%}", "%{G%}":"%{G%}"},
                         # Verb Class III: end in -g, -w, -ghw
                         {"(g/t)": "t", "(t)":"t", "(te)":"te", "%{E%}":"e", "%{.m.%}": "%{.m.%}"},
                         # Verb Class IV: end in -agh, -igh, -ugh
                         {"(g/t)": "t", "(t)":"t", "(te)":"te",  "%{E%}":"e", "%{.m.%}": "%{.m.%}"},
                         # Verb Class V: end in -te
                         {"(g/t)": "", "(t)":"", "(te)":"", "%{.f.%}": "%{.f.%}", "%{.at.%}": "%{.at.%}"},
                         # Verb Class VI: end in special -te
                         {"(g/t)": "", "(t)":"", "(te)":"", "%{.f.%}": "%{.f.%}", "%{.at.%}": "%{.at.%}"},
                         # Verb Class VII: have semi-final -e
                         {"(g/t)": "t", "(t)":"t", "(te)":"te", "%{E%}":"e", "%{.sf.%}%{G%}": "%{.sf.%}%{G%}", "%{.sf.%}": "%{.sf.%}", "%{.m.%}": "%{.m.%}"},
                       ]


def replace_all(my_text, my_dict):
    '''
    :param my_text: string to undergo replacement 
    :type my_text: str
    :param my_dict: associates original text 'i' with
                    its replacement text 'j' 
    :type my_dict: dict

    Replaces all instances of 'i' in my_text with 'j'.
    '''
    for i, j in my_dict.items():
        my_text = my_text.replace(i, j)
    return my_text


def annotate_suffixes(my_suffixes, my_root_type):
    '''
    :param my_suffixes: path to file containing suffixes
    :type my_suffixes: str
    :param my_root_type: "Noun" or "Verb"
    :type my_root_type: str

    :return: A dictionary where each key is an integer
             representing an inflection class, and each
             value is a string containing all of the
             suffixes annotated for a particular class,
             and their definitions.

    '''
    class2suffixes = {}

    if my_root_type == "Noun":
        rules = rules_for_noun_roots
        n_class = len(rules)
        
    elif my_root_type == "Verb":
        rules = rules_for_verb_roots
        n_class = len(rules)

    else:
        raise ValueError('root_type needs to be either "Noun" or "Verb"')

    with open(my_suffixes, 'r') as suffix_input:
        suffixes_jacobson_notation = suffix_input.read()

    class2suffixes[0] = suffixes_jacobson_notation

    for i in range(1, n_class+1):

        # convert Jacobson (2001) Notation to v.2 Notation
        suffixes_v2_notation = replace_all(suffixes_jacobson_notation, symbol_conversion)

        # rewrite certain symbols as required for a given class of roots
        suffixes_class_specific = replace_all(suffixes_v2_notation, rules[i-1])

        for symbol in symbol_conversion.values():
            # remove any symbols that are not necessary for the given class of roots 
            if symbol not in rules[i-1]:
                final_annotated_suffixes = suffixes_class_specific.replace(symbol, "")
                suffixes_class_specific = final_annotated_suffixes
    
        class2suffixes[i] = suffixes_class_specific

    return class2suffixes


def print_suffixes(inflClass, jacobson_notation_suffixes, class_specific_suffixes, rootType, resultType):

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

    romanNumeral = idx_to_roman_numeral(inflClass)

    print("-" * 22 + "-" * len(romanNumeral)) 
    print(rootType + " Inflection Class " + romanNumeral)
    print("-" * 22 + "-" * len(romanNumeral)) 

    jacobsonSuffixes = jacobson_notation_suffixes.split("\n")
    annotatedSuffixes = class_specific_suffixes.split("\n")
    
    for i, suffixWithDefinition in enumerate(annotatedSuffixes):
        if suffixWithDefinition:
            suffix, definition = suffixWithDefinition.split(",", 1)

            jacobsonSuffix = re.sub('-[^w]', '', jacobsonSuffixes[i].split(",", 1)[0])

            # determine the derivational suffix's continuation class
            if resultType == "Noun":
                sffx = convert_to_base_form(suffix)
            else:
                sffx = suffix[:-1]

            classIdx = classify_noun_root(sffx)
            suffixMapping = jacobsonSuffix + "[" + rootType[0] + "." + resultType[0] + "]" + ":^" + sffx
            idx2InflClass[classIdx].append((suffixMapping, definition))

    # for the given class of roots, print each class of annotated suffixes
    for i in range(1, len(idx2InflClass)):
        if idx2InflClass[i]:
             # get length of longest root in inflection class
             # in order to properly calculate padding
             maxLength = get_max_length_suffixes(resultType, i, idx2InflClass[i])
 
             # class of noun roots that end in -g, -w, -ghw
             if resultType == "Noun" and i == 2:
                 for root, definition in idx2InflClass[i]:
                     # if noun root ends in -w, add %{k%} -->  kiiw:kii%{k%}w
                     if root[-1] == "w" and ''.join(root[-3:-1]) != "gh":
                         padding = maxLength - (len(root) + 5) + 2
                         print(root[:-1] + "%{k%}w" + " " * padding + \
                               resultType + "Postbase" + idx_to_roman_numeral(i) + "; ! " + definition)
                     else:
                         padding = maxLength - len(root) + 2
                         print(root + " " * padding + resultType + "Postbase" + idx_to_roman_numeral(i) + \
                               "; ! " + definition)
 
             # class of noun roots that end in weak -gh
             #   add %{g%} --> nasaperagh:nasapera%{g%}h
             elif resultType == "Noun" and i == 3:
                 for root, definition in idx2InflClass[i]:
                     padding = maxLength - (len(root) + 4) + 2
                     print(root[:-2] + "%{g%}h" + " " * padding + \
                           resultType + "Postbase" + idx_to_roman_numeral(i) + "; ! " + definition)
 
             # class of noun roots that end in marked strong -gh (*)
             #   remove * at the end of the root, e.g. afsengagh*  --> afsengagh
             elif resultType == "Noun" and i == 4:
                 for root, definition in idx2InflClass[i]:
                     padding = maxLength - len(root) + 2
                     print(root[:-1] + " " * padding + resultType + "Postbase" + idx_to_roman_numeral(i) + \
                           "; ! " + definition)
 
             # class of roots that end in -te
             #   if root ends in -te, add %{t%} --> riigte:riig%{t%}e
             elif (resultType == "Noun" and i == 6 or
                   resultType == "Verb" and i == 5):
                 for root, definition in idx2InflClass[i]:
                     padding = maxLength - (len(root) + 4) + 2
                     print(root[:-2] + "%{t%}e" + " " * padding + \
                           resultType + "Postbase" + idx_to_roman_numeral(i) + "; ! " + definition)
 
             else:
                 for root, definition in idx2InflClass[i]:
                     padding = maxLength - len(root) + 2
                     print(root + " " * padding + resultType + "Postbase" + idx_to_roman_numeral(i) + \
                           "; ! " + definition)
             print()
 
    # print roots that could not be classified, usually those with non-traditional endings
    if idx2InflClass[0]:
        maxLength = get_max_length_suffixes("None", 0, idx2InflClass[0])

        print("----------------------------------------------------")
        print("Extended " + resultType + " Roots (?) that Could Not Be Classified")
        print("----------------------------------------------------")
        for root, definition in idx2InflClass[0]:
            padding = maxLength - len(root) + 2
            print(root + " " * padding + definition)
    print()


def get_max_length_suffixes(inflType, classIdx, inflClass):
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
                alteredLength = len(root) + 5  # adding %, {, k, %, }
                if alteredLength > alteredMaxLength:
                    alteredMaxLength = alteredLength

        if alteredMaxLength > maxLength:
            maxLength = alteredMaxLength

    # get length of longest weak -gh root with %{g%} inserted
    # -te root with %{t%} inserted
    #   e.g. nasapera%{g%}h
    #        riig%{t%}e
    elif (inflType == "Noun" and classIdx == 3 or
          inflType == "Noun" and classIdx == 6 or
          inflType == "Verb" and classIdx == 5):
        maxLength = maxLength + 4 # adding %, {, %, }

    return maxLength


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--suffixes', '-s', type=str, help = 'path to file containing derivational suffixes')
    parser.add_argument('--suffix_type', '-r', type=str, help = 'type of derivational suffix: NN, NV, VV, VN')
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

    for inflectionClass in class2suffixes.keys():
        # class2suffixes[0] lists the suffixes annotated in Jacobson (2001) Notation
        if inflectionClass > 0:
            print_suffixes(inflectionClass, class2suffixes[0], class2suffixes[inflectionClass], rootType, resultType) 


if __name__ == "__main__":
    main()
