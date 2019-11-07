import argparse
import glob

from methods import idx_to_roman_numeral

symbols = { "~": "%{.f.%}%{.sf.%}", # Jacobson notation: foma v.2 notation
           "~f": "%{.f.%}", 
           "~sf": "%{.sf.%}",  
			"@": "%{.at.%}", 
			"%:": "%{.c.%}", 
			"–": "%{.m.%}",
			"-w": "%{.w.%}",
			"(e)": "%{E%}",
			"(g)": "%{G%}",
			":": "%^"}


			#(g/t) (ng) (e)

def print_inflections(inflType):
    '''
    :param inflType: "Noun" or "Verb"
    :type inflType: str

    Janky print function to print each suffix in each
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
    parser.add_argument('--dirname', type=str, default="./suffix_lists", help = 'name of directory containing suffix lists')
    parser.add_argument('root_type', type=str, help = 'Type of the root: either noun or verb')
    args = parser.parse_args

	for filename in glob.glob(args.dirname + "/*.txt"):
		with open(filename, 'r') as txtfile:
            for line in txtfile:
                if "particle" not in line[1]:
                    root = line[0]

                    # verb roots are annotated with a hyphen at the end
                    if root[-1] == "-":
                        verbRoot = root[:-1]
                        classIdx = classify_verb_root(verbRoot)
                        if classIdx in idx2VerbClass.keys():
                          idx2VerbClass[classIdx].append((verbRoot, line[1]))
                        else:
                          print("{} not found".format(verbRoot))

                    else:
                        nounRoot = convert_to_base_form(root)
                        classIdx = classify_noun_root(nounRoot)
                        if classIdx in idx2NounClass.keys():
                          idx2NounClass[classIdx].append((nounRoot, line[1]))
                        else:
                          print("{} not found".format(nounRoot))

    print_inflection_classes("Verb", idx2VerbClass)
    print_inflection_classes("Noun", idx2NounClass)