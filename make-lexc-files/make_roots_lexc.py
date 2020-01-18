'''
:author: Emily Chen
:date:   2019

Given a list of Yupik noun or verb roots in .csv format,
classifies each root into its respective inflection class,
and prints each inflection class in lexc-compatible format.

Usage: python3 make_roots_lexc.py -d [dirname]
'''
import argparse
import csv
import glob

from classify_helper_methods import classify_verb_root, \
                                       convert_to_base_form, classify_noun_root
from print_helper_methods import print_inflection_classes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirname', '-d', type=str, help='name of directory containing root lists')
    args = parser.parse_args()

    # initialize a dictionary where each key is an int
    # representing an inflection class, and each value
    # is a list of (root, definition) tuples
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

    for filename in glob.glob(args.dirname + "/*"):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')

            for line in reader:
                root = line[0]

                # verb roots are annotated with a hyphen at the end
                if root[-1] == "-":
                    trueRoot = root[:-1]
                    classIdx = classify_verb_root(trueRoot)
                else:
                    trueRoot = convert_to_base_form(root)
                    classIdx = classify_noun_root(trueRoot)

                idx2InflClass[classIdx].append((trueRoot, line[1]))

    print_inflection_classes("Root", "Verb", idx2InflClass)
    print_inflection_classes("Root", "Noun", idx2InflClass)


if __name__ == "__main__":
    main()
