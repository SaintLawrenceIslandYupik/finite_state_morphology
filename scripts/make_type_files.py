'''
:author: Emily Chen
:date:   2019

Converts a series of .csv files containing test TOKENS and
a corresponding series of .csv files containing gold TOKENS
into a single pair of files:
  * a file containing test TYPES
  * a corresponding file containing gold TYPES

The resulting TYPES files can be passed as input to the
script 'evaluate.py' to calculate precision, recall, f-measure,
and coverage.

'''
import argparse
import csv
import glob
import os


def main():

    # initialize a dictionary to hold surfaceForm<->lexicalForm pairs
    d = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('test_tokens', help='path to directory containing all test TOKENS')
    parser.add_argument('gold_tokens', help='path to directory containing all gold TOKENS')
    parser.add_argument('test_types', help='desired file path to test TYPES')
    parser.add_argument('gold_types', help='desired file path to gold TYPES')
    args = parser.parse_args()

    # check that the user-input filenames match for the output TYPES files
    test_filename = os.path.splitext(os.path.basename(args.test_types))[0]
    gold_filename = os.path.splitext(os.path.basename(args.gold_types))[0]

    if test_filename != gold_filename:
        raise Exception("\n\nselected basenames do not match:\n" + \
                        "  " + test_filename + " != " + gold_filename + "\n" + \
                        "'evaluate.py' requires that these basenames match.\n" + \
					    "sry, but pls don't fight the system.")

    else:
        for testfile in glob.glob(args.test_tokens + "/*"):
            filename = os.path.splitext(os.path.basename(testfile))[0]

            for goldfile in glob.glob(args.gold_tokens + "/*"):

                # open matching test and gold standard files
                if filename == (os.path.basename(goldfile)).split(".")[0]:
                    with open(testfile, 'r') as tf, open(goldfile, 'r') as gf:
                        testItems = csv.reader(tf, delimiter="\t")
                        goldItems = csv.reader(gf, delimiter="\t")

                        surfaceForms = []
                        lexicalForms = []

                        [surfaceForms.extend(row) for row in testItems]
                        [lexicalForms.extend(row) for row in goldItems]

                        # make sure the # test items == # gold items
                        if len(surfaceForms) != len(lexicalForms):
                            raise Exception("\n\nthe number of test items doesn't match the " + \
                                            "number of gold standard items:\n" + \
                                            "  # test = " + str(len(surfaceForms)) + "\n" + \
                                            "  # gold = " + str(len(lexicalForms)))

                        for idx, word in enumerate(surfaceForms):
                            if word not in d:
                                d[word.lower()] = lexicalForms[idx]

        # write out new test file and gold file containing TYPES
        with open(args.test_types, 'w') as testfile, open(args.gold_types, 'w') as goldfile:
            for word in d.keys():
               testfile.write(word + "\n")
               goldfile.write(d[word] + "\n")


if __name__ == "__main__":
    main()
