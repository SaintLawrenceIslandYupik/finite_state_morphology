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
import re

from foma import *
from print_func import *


def get_predicted_analyses(t, testfile):
    '''
    :param t: the 'foma' analyzer
    :type  t: not sure tbh
    :param testfile: file containing words
                     to be analyzed
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
    # print status update
    print("working on " + testfile + "...")

    allWords    = prep_input(testfile)
    allAnalyses = []

    for word in allWords:
        analyses = list(t.apply_up(word))
    
        ''' 
        some additional processing in case the
        analyzer can't analyze the word as is
        '''
        # handle vowel lengthening in yes-no questions
        if not analyses and len(word) > 2:
            if word[-3:-1] == "aa":
                # e.g. ighneghaan -> ighneghan
                tryThis = word[:-3] + "a" + word[-1]
                analyses.extend(list(t.apply_up(tryThis)))
    
                # e.g. qiyastaak -> qiyastek
                tryThis = word[:-3] + "e" + word[-1]
                analyses = list(t.apply_up(tryThis))
                analyses.extend(list(t.apply_up(tryThis)))
    
            elif word[-2:] == "aa":
                tryThis = word[:-2] + "a"
                analyses.extend(list(t.apply_up(tryThis)))
    
            elif word[-3:-1] == "ii":
                # e.g. qiyaziin -> qiyazin
                tryThis = word[:-3] + "i" + word[-1]
                analyses.extend(list(t.apply_up(tryThis)))
    
            elif word[-2:] == "ii":
                # e.g. qiyatsii -> qiyatsi
                tryThis = word[:-2] + "i"
                analyses.extend(list(t.apply_up(tryThis)))
    
            elif word[-3:-1] == "uu":
                tryThis = word[:-3] + "u" + word[-1]
                analyses.extend(list(t.apply_up(tryThis)))
    
            elif word[-2:] == "uu":
                tryThis = word[:-2] + "u"
                analyses.extend(list(t.apply_up(tryThis)))
    
        # s -> t, g -> k, gh -> q 
        if not analyses and len(word) > 1:
            if word[-1] == "s":
                tryThis = word[:-1] + "t"
                analyses.extend(list(t.apply_up(tryThis)))
            elif word[-1] == "g" and word[-2] != "n":
                tryThis = word[:-1] + "k"
                analyses.extend(list(t.apply_up(tryThis)))
            elif ''.join(word[-2:]) == "gh":
                tryThis = word[:-2] + "q"
                analyses.extend(list(t.apply_up(tryThis)))
    
        # gw -> g or gw -> 
        if not analyses:
            if "gw" in word:
                tryThis = word.replace("gw", "g") 
                analyses.extend(list(t.apply_up(tryThis)))
    
                tryThis = word.replace("gw", "w")
                analyses.extend(list(t.apply_up(tryThis)))
       
        allAnalyses.append(analyses)

    return allWords, allAnalyses


def prep_input(testfile):
    '''
    :param testfile: file containing words
                     to be analyzed
    :type  testfile: str

    :return: a list of words, stripped of punctuation,
	         ready for analysis

    '''
    allWords = []

    with open(testfile, 'r') as f:
        for sentence in f:
            if sentence != "\n":
                words = sentence.strip("\n ").lower().split(" ")

                for w in words:
                    # strip punctuation except apostrophes
                    word = re.sub(ur"[^\w\d'\s]+", '', w)

                    if any(char.isalpha() for char in word):
                        allWords.append(word)

    return allWords


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
        for testfile in glob.glob(args.test + "/*"):
            # get the 'foma' analyzer's predicted analyses
            words, analyses = get_predicted_analyses(t, testfile)
            predicted.extend(analyses)

            for idx, analysis in enumerate(analyses):
                if len(analysis) == 0:
                    unanalyzed.append(words[idx])

                output[words[idx]] = analyses[idx]

    # print the full evaluation report
    if args.gold:
        print_eval_report(True, predicted, unanalyzed, output, target)
    else:
        print_eval_report(False, predicted, unanalyzed, output)


if __name__ == "__main__":
    main()
