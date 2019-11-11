import argparse
import glob
from classify import idx_to_roman_numeral
import re 


'''
usage: python modify_suffixes.py -s suffix_lists/Intrg.txt -r Noun

'''


symbol_conversion = {"~f": "%{.f.%}", # Jacobson notation <-> foma v.2 notation
                    "~sf": "%{.sf.%}", 
                    "~": "%{.f.%}%{.sf.%}", 
                    "@": "%{.at.%}", 
                    "%:": "%{.c.%}", 
                    "–": "%{.m.%}",
                    "-w": "%{.w.%}",
                    "(e)": "%{E%}",
                    "(g)": "%{G%}",
                    ":": ":%^",
                    "EncliticOrEnd": "#",
                    "-":"",
                    "+":""}

rules_for_noun = [{"%{E%}": "", "(ng)": "ng"}, # NounInflI: when suffixing to noun roots that end in -a, -i, -u, -aa, -ii-, -uu
                  {"%{E%}": "e", "(ng)": ""},  # NounInflII: when suffixing to noun roots that end in -g, -w, -ghw
                  {"%{E%}": "", "(ng)": "", "%{.m.%}": "%{.m.%}", "%{.w.%}%{.c.%}":"%{.w.%}%{.c.%}", "%{.w.%}": "%{.w.%}", "%{.c.%}": "%{.c.%}"}, # NounInflIII: when suffixing to noun roots that end in weak -gh
                  {"%{E%}": "%{E%}", "(ng)": "", "%{.m.%}": "%{.m.%}", "%{.c.%}": "%{.c.%}"}, # NounInflIV: when suffixing to noun roots that end in marked strong -gh (*)
                  {"%{E%}": "e", "(ng)": "", "%{.m.%}": "%{.m.%}"}, # NounSuffixV: when suffixing to noun roots that end in strong -gh
                  {"%{E%}": "", "(ng)": "ng", "%{.f.%}": "%{.f.%}"}, # NounInflVI: when suffixing to noun roots that end in -te
                  {"%{E%}": "e", "(ng)": "", "%{.sf.%}": "%{.sf.%}", "%{.m.%}": "%{.m.%}"}, # NounInflVII: when suffixing to noun roots that have semi-final -e that can be hopped
                  {"%{E%}": "e", "(ng)": "", "%{.sf.%}": "%{.sf.%}", "%{.m.%}": "%{.m.%}"}, # NounInflVIII: when suffixing to noun roots that have semi-final -e that can be dropped but not hopped
                  {"%{E%}": "", "(ng)": "ng", "%{.f.%}": "%{.f.%}"}, # NounInflIX: when suffixing to noun roots that end in -e that can be hopped
                  {"%{E%}": "", "(ng)": "ng", "%{.f.%}": "%{.f.%}"} # NounInflX: when suffixing to noun roots that end in final -e that can be dropped but not hopped
                  ]

rules_for_verb = [{"(g/t)": "%{G%}", "%{G%}":"%{G%}", "(t)":"", "(te)":""}, # VerbSuffixI: when suffixing to verb roots that end in -a, -i, -u
                  {"(g/t)": "", "(t)":"", "(te)":"", "%{.f.%}": "%{.f.%}", "%{G%}":"%{G%}"}, # VerbSuffixII: when suffixing to verb roots that have final -e
                  {"(g/t)": "t", "(t)":"t", "(te)":"te", "%{E%}":"e", "%{.m.%}": "%{.m.%}"}, # VerbSuffixIII: when suffixing to verb roots that end in -g, -w, -ghw
                  {"(g/t)": "t", "(t)":"t", "(te)":"te",  "%{E%}":"e", "%{.m.%}": "%{.m.%}"}, # VerbSuffixIV: when suffixing to verb roots that end in -agh, -igh, -ugh or -egh where e cannot be dropped
                  {"(g/t)": "", "(t)":"", "(te)":"", "%{.f.%}": "%{.f.%}", "%{.at.%}": "%{.at.%}"}, # VerbInflV: when suffixing to verbs that end in -te
                  {"(g/t)": "t", "(t)":"t", "(te)":"te", "%{E%}":"e", "%{.sf.%}%{G%}": "%{.sf.%}%{G%}", "%{.sf.%}": "%{.sf.%}", "%{.m.%}": "%{.m.%}"}, # VerbSuffixVI: when suffixing to verb roots that have semi-final -e that can be hopped
                  {"(g/t)": "t", "(t)":"t", "(te)":"te", "%{E%}":"e", "%{.sf.%}%{G%}": "%{.sf.%}%{G%}", "%{.sf.%}": "%{.sf.%}", "%{.m.%}": "%{.m.%}"} # VerbSuffixVII: when suffixing to verb roots that have semi-final -e that can be dropped but not hopped
                  ]

def replace_all(my_text, my_dict):
    for i, j in my_dict.items():
        my_text = my_text.replace(i, j)
    return my_text

def print_inflections(my_suffixes, my_root_type):
    '''
    :param my_root_type: "Noun" or "Verb"
    :type my_root_type: str

    Janky print function to print each suffix in each
    inflection class in lexc-compatible format.

    '''
    if my_root_type == "Noun":
        rules = rules_for_noun
        n_class = len(rules)
        

    elif my_root_type == "Verb":
        rules = rules_for_verb
        n_class = len(rules)

    else:
        raise ValueError('root_type needs to be either "Noun" or "Verb"')

    with open(my_suffixes, 'r') as suffix_input:
        suffix_org = suffix_input.read()

    for i in range(1, n_class+1):

        romanNumeral = idx_to_roman_numeral(i)

        print("-" * 22 + "-" * len(romanNumeral)) 
        print(my_root_type + " Inflection Class " + romanNumeral)
        print("-" * 22 + "-" * len(romanNumeral)) 
        suffixes_new = replace_all(suffix_org, symbol_conversion) # convert the Jacobson symbols to our new notations

        suffixes_specific = replace_all(suffixes_new, rules[i-1]) # apply the class-specific rules

        for symbol in symbol_conversion.values(): # remove any symbols that are not specified in the class-specific rules
            if symbol == ":%^" or symbol == "#": # do not remove these symbols
                continue
            elif symbol not in rules[i-1]:
                suffixes_specific = suffixes_specific.replace(symbol, "")
    
        print(suffixes_specific)

        



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--suffixes', '-s', type=str, help = 'path to the file containing derivational/inflectional suffixes e.g. "./suffix_lists/Intrg.txt"')
    parser.add_argument('--root_type', '-r', type=str, help = 'Type of the root: either noun or verb')
    args = parser.parse_args()

    print_inflections(args.suffixes, args.root_type)

if __name__ == "__main__":
    main()