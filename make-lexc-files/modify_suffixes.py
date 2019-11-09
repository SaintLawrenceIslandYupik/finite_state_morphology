import argparse
import glob
from classify import idx_to_roman_numeral
import re 


'''
usage: python modify_suffixes.py -s suffix_lists/Intrg.txt -r Noun

'''


symbol_conversion = { "~": "%{.f.%}%{.sf.%}", # Jacobson notation <-> foma v.2 notation
                    "~f": "%{.f.%}", 
                    "~sf": "%{.sf.%}",  
                    "@": "%{.at.%}", 
                    "%:": "%{.c.%}", 
                    "–": "%{.m.%}",
                    "-w": "%{.w.%}",
                    "(e)": "%{E%}",
                    "(g)": "%{G%}",
                    ":": ":%^",
                    "EncliticOrEnd": "#;"}

rules_for_noun = [{"%{E%}": "", "(ng)": "ng"}, # NounInflI: noun roots that end in -a, -i, -u, -aa, -ii-, -uu
                  {"%{E%}": "e", "(ng)": ""},  # NounInflII: noun roots that end in -g, -w, -ghw
                  {"%{E%}": "", "(ng)": "", "%{.m.%}": "%{.m.%}", "%{.w.%}": "%{.w.%}", "%{.c.%}": "%{.c.%}"}, # NounInflIII: noun roots that end in weak -gh
                  {"%^%{.c.%}%{E%}":"%^%{.c.%}%{E%}", "%{E%}": "", "(ng)": "", "%{.m.%}": "%{.m.%}", "%{.c.%}": "%{.c.%}"}# NounInflIV for noun roots that end in marked strong -gh (*)
                  ]

# rules_for_verb = {1: 
#                   2:
#                  3:
#                 4: 
#                 5:
#                 6:
#                 7:
#                 }

			#(g/t) (ng) (e)

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
        n_class = len(rules_for_noun)

    elif my_root_type == "Verb":
        n_class = len(rules_for_verb)

    else:
        raise ValueError('root_type needs to be either "Noun" or "Verb"')

    with open(my_suffixes, 'r') as suffix_input:
        suffix_org = suffix_input.read()

    # for i in range(1, n_class+1):
    for i in range(1, 3):

        romanNumeral = idx_to_roman_numeral(i)

        print("-" * 22 + "-" * len(romanNumeral)) 
        print(my_root_type + " Inflection Class " + romanNumeral)
        print("-" * 22 + "-" * len(romanNumeral)) 
        suffixes_new =replace_all(suffix_org, symbol_conversion)

        for symbol in symbol_conversion.values():
            if symbol == ":%^":
                continue
            elif symbol not in rules_for_noun[i-1]:
                suffixes_new = suffixes_new.replace(symbol, "")
            else:
                suffixes_new = suffixes_new.replace(symbol, rules_for_noun[i-1][symbol])
        
        print(suffixes_new)
            # symbol_conversion = dict((re.escape(k), v) for k, v in symbol_conversion.items()) 
            # pattern = re.compile("|".join(symbol_conversion.keys()))
            # new_line = pattern.sub(lambda m: symbol_conversion[re.escape(m.group(0))], line)
            # print(new_line)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--suffixes', '-s', type=str, help = 'path to the file containing derivational/inflectional suffixes e.g. "./suffix_lists/Intrg.txt"')
    parser.add_argument('--root_type', '-r', type=str, help = 'Type of the root: either noun or verb')
    args = parser.parse_args()

    print_inflections(args.suffixes, args.root_type)

if __name__ == "__main__":
    main()