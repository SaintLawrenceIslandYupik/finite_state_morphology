'''
:author Emily Chen:
:date   2019:

Prints an "evaluation report" for the analyzer
on a given dataset.

Given a directory of files with test items and a
corresponding directory of gold standard analyses,
the report will include:
    * precision, recall, f-measure, coverage
	* a list of words that could not be analyzed
	* a list of incorrect analyses paired with their
	  target analyses

Otherwise, given just a directory of files with test
items, the report will include:
    * coverage 
	* a list of words that could not be analyzed

IMPORTANT:
  * evaluate.py must be run in python 2.7

  * a test file and its gold standard file must
    share a basename, e.g.
        [Ch1].tsv
        [Ch1].gold.tsv
    otherwise evaluate.py won't be able to match the
    predicted analysis to the gold standard analysis

'''
import argparse
import csv
import glob
import os
import pprint
import time

from foma import *
from print_func import *


# def generate_output_files():
#     print(analysis.decode("utf-8"))


def get_predicted_analyses(t, testfile):
    '''
    :param t: the 'foma' analyzer
    :type  t: not sure tbh
    :param testfile: path to a file containing
                     the words to be analyzed
    :type  testfile: str

    :return: a tuple, where the first element is
             a list L of all of the words in 'testfile'
             and the second element is a list of lists,
             where each sublist contains all of the
             analyses for each word in L

    Uses the given 'foma' analyzer to analyze each
    word found in 'testfile'. Appends an empty
    list if a morphological analysis cannot be found.

    '''
    allWords    = []
    allAnalyses = []

    # print status update
    print("working on " + testfile + "...")

    with open(testfile) as csvfile:
        items = csv.reader(csvfile, delimiter="\t")

        for row in items:
            for word in row:
                allWords.append(word)

                analyses = list(t.apply_up(word))

                # TODO: clean up all this additional processing
                #       this is not well done D:
                # attempt to analyze the lowercased form
                if not analyses and word != word.lower():
                    surfaceForm = word.lower()
                    analyses = list(t.apply_up(surfaceForm))
    
                # handle vowel lengthening in yes-no questions
                if not analyses:
                    if word[-3:-1] == "aa":
                        # e.g. ighneghaan -> ighneghan
                        surfaceForm = word[:-3] + "a" + word[-1]
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                        # e.g. qiyastaak -> qiyastek
                        surfaceForm = word[:-3] + "e" + word[-1]
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                    elif word[-2:] == "aa":
                        surfaceForm = word[:-2] + "a"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                    elif word[-3:-1] == "ii":
                        # e.g. qiyaziin -> qiyazin
                        surfaceForm = word[:-3] + "i" + word[-1]
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                    elif word[-2:] == "ii":
                        # e.g. qiyatsii -> qiyatsi
                        surfaceForm = word[:-2] + "i"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                    elif word[-3:-1] == "uu":
                        surfaceForm = word[:-3] + "u" + word[-1]
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                    elif word[-2:] == "uu":
                        surfaceForm = word[:-2] + "u"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                # s -> t, g -> k, gh -> q 
                if not analyses:
                    if word[-1] == "s":
                        surfaceForm = word[:-1] + "t"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))
                    elif word[-1] == "g" and word[-2] != "n":
                        surfaceForm = word[:-1] + "k"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))
                    elif ''.join(word[-2:]) == "gh":
                        surfaceForm = word[:-2] + "q"
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                # gw -> g or gw -> 
                if not analyses:
                    if "gw" in word:
                        surfaceForm = word.replace("gw", "g") 
                        analyses = list(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))

                        surfaceForm = word.replace("gw", "w")
                        analyses.extend(t.apply_up(surfaceForm))
                        analyses.extend(list(t.apply_up(surfaceForm.lower())))
                # TODO: additional processing ends here 
   
                allAnalyses.append(analyses)

    return allWords, allAnalyses


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('analyzer', help='path to foma analyzer')
    parser.add_argument('test', help='path to directory containing test sents')
    parser.add_argument('--gold', help='path to directory containing gold standards', required=False)
    args = parser.parse_args()

    # load the analyzer's .fomabin file
    t = FST.load(args.analyzer)

    # initialize list for analyzer-returned analyses
    predicted = []

    # initialize list for words with no analyses
    unanalyzed = []

    # initialize a dictionary for analyzer output where
    #   key   : word to analyze
    #   value : list of analyzer-returned analyses
    output = {}

    if args.gold:
        # initialize list for gold standard analyses
        target = []

        for testfile in glob.glob(args.test + "/*"):
            # get the 'foma' analyzer's predicted analyses
            words, analyses = get_predicted_analyses(t, testfile)
            predicted.extend(analyses)

            for idx, analysis in enumerate(analyses):
                if len(analysis) == 0:
                    unanalyzed.append(words[idx])

                output[words[idx]] = analyses[idx]

            filename = os.path.splitext(os.path.basename(testfile))[0]

            for goldfile in glob.glob(args.gold + "/*"):
                # add the gold analyses in the same order as the
                # analyzer-returned analyses
                if filename == (os.path.basename(goldfile)).split(".")[0]:
                    with open(goldfile) as csvfile:
                        items = csv.reader(csvfile, delimiter="\t")
                        [target.append(word) for row in items for word in row]
            
        # make sure the # test items == # gold items
        if len(predicted) != len(target):
            raise Exception("\n\nthe number of test items doesn't match the " + \
                             "number of gold standard items:\n" + \
                             "  # test = " + str(len(predicted)) + "\n" + \
                             "  # gold = " + str(len(target)))

    else:
        # start = time.time()
        for testfile in glob.glob(args.test + "/*"):
            # get the 'foma' analyzer's predicted analyses
            words, analyses = get_predicted_analyses(t, testfile)
            predicted.extend(analyses)

            for idx, analysis in enumerate(analyses):
                if len(analysis) == 0:
                    unanalyzed.append(words[idx])

                output[words[idx]] = analyses[idx]

        # end = time.time()
        # print(end - start)
        # pprint.pprint(output)

    # print the full evaluation report
    if args.gold:
        print_eval_report(True, predicted, unanalyzed, output, target)
    else:
        print_eval_report(False, predicted, unanalyzed, output)


if __name__ == "__main__":
    main()
