'''
:author: Hayley Park and Emily Chen
:date:   2020

Methods related to printing Yupik lexical items
and their continuation classes in a lexc-compatible format.

'''
from collections import OrderedDict

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

# TODO: should check these and eliminate incorrect pairings, e.g. %{.w.%}%{.c.%}
#       also (g) doesn't always map to %{G%}
rules_for_nouns = [ # Noun Class I: end in -a, -i, -u
                    {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v"},
                    # Noun Class II: end in -g, -w, -ghw
                    {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"v", "%{.m.%}":"%{.m.%}"},
                    # Noun Class III: end in weak -gh
                    {"%{E%}":"", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}", "%{.w.%}":"%{.w.%}", "%{.c.%}":"%{.c.%}"},
                    # Noun Class IV: end in marked strong -gh (*)
                    {"%{E%}":"%{E%}", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}", "%{.c.%}":"%{.c.%}"},
                    # Noun Class V: end in strong -gh
                    {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.m.%}":"%{.m.%}", "%{.c.%}":"%{.c.%}"},
                    # Noun Class VI: end in -te 
                    {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}", "%{.at.%}":"%{.at.%}"},
                    # Noun Class VII: have semi-final -e
                    {"%{E%}":"e", "(ng)":"", "(te)":"te", "(p/v)":"p", "%{.sf.%}":"%{.sf.%}", "%{.m.%}":"%{.m.%}"},
                    # Noun Class VIII: end in -e that can be dropped but not hopped
                    {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}"},
                    # Noun Class IX: end in -e that can be dropped and hopped
                    {"%{E%}":"", "(ng)":"ng", "(te)":"", "(p/v)":"v", "%{.f.%}":"%{.f.%}"}
                 ]

rules_for_verbs = [ # Verb Class I: end in -a, -i, -u
                    {"(g/t)":"%{G%}", "(i/u)": "", "(p/v)":"v", "(q/t)":"", "(at)":"at", "(ng)":"ng", "(te)":"", "(a)":"", "(s)":"s", "(t)":"", "(u)":""},
                    # Verb Class II: end in -e
                    {"(g/t)":"", "(i/u)":"u", "(p/v)":"v", "(q/t)":"", "(at)":"at", "(ng)":"ng", "(te)":"", "(a)":"a", "(s)":"s", "(t)":"", "(u)":"u", "%{.f.%}": "%{.f.%}", "%{G%}":"%{G%}"},
                    # Verb Class III: end in -g, -w, -ghw
                    {"(g/t)":"t", "(i/u)":"u", "(p/v)":"p", "(q/t)":"t", "(at)":"at", "(ng)":"", "(te)":"te", "(s)":"", "(t)":"t", "(u)":"u", "%{E%}":"e", "%{.m.%}":"%{.m.%}"},
                    # Verb Class IV: end in -agh, -igh, -ugh
                    {"(g/t)":"t", "(i/u)":"u", "(p/v)":"p", "(q/t)":"t", "(at)":"at", "(ng)":"", "(te)":"te", "(s)":"", "(t)":"t", "(u)":"u", "%{E%}":"e", "%{.m.%}":"%{.m.%}", "%{.c.%}":"%{.c.%}"},
                    # Verb Class V: end in -te
                    {"(g/t)":"", "(i/u)":"i", "(p/v)":"v", "(q/t)":"q", "(at)":"", "(ng)":"ng", "(te)":"", "(s)":"s", "(t)":"", "(u)":"u", "%{.f.%}":"%{.f.%}", "%{.at.%}":"%{.at.%}"},
                    # Verb Class VI: end in special -te
                    {"(g/t)":"", "(i/u)":"i", "(p/v)":"v", "(q/t)":"q", "(at)":"", "(ng)":"ng", "(te)":"", "(s)":"s", "(t)":"", "(u)":"u", "%{.f.%}":"%{.f.%}", "%{.at.%}":"%{.at.%}"},
                    # Verb Class VII: have semi-final -e
                    {"(g/t)":"t", "(i/u)":"u", "(p/v)":"p", "(q/t)":"t", "(at)":"at", "(ng)":"", "(te)":"te", "(s)":"", "(t)":"t", "(u)":"u", "%{E%}":"e", "%{.sf.%}%{G%}":"%{.sf.%}%{G%}", "%{.sf.%}":"%{.sf.%}", "%{.m.%}":"%{.m.%}"}
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
        rules = rules_for_nouns
        n_class = len(rules)
        
    elif my_root_type == "Verb":
        rules = rules_for_verbs
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
