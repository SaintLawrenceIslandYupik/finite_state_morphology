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

from methods_for_classification import classify_verb_root, \
                                       convert_to_base_form, classify_noun_root




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
