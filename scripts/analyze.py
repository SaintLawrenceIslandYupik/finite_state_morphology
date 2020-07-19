# -*- coding: utf-8 -*-

'''
:author Emily Chen:
:date   2020:

'''
import argparse
import glob
import os
import string
import re

from foma import *


def analyze_input_file(t, input):
    '''
    :param t: the 'foma' analyzer
    :type  t: not sure tbh
    :param input: file containing
                  words to be analyzed
    :type  input: str

    :return: a list of lists, where each sublist
             contains all of the analyses for each
             word in the given text file

    Uses the given 'foma' analyzer to analyze each
    word found in 'textfile'. Appends the original
    word if a morphological analysis cannot be found,
    and the string "<br>" for each newline.

    '''
    allAnalyses = []

    # print status update
    print("working on " + input + "...")

    allWords    = prep_input(input)
    allAnalyses = []

    for word in allWords:
        print(word)

        # actually a new sentence
        if len(word) > 5 and word[:5] == "SENT:":
            allAnalyses.append(word)

        else:
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

            # handle vocatives 
            if not analyses and len(word) > 3:
                if word[-3:] == "aay":
                    # e.g. apaay -> apa
                    tryThis = word[:-2]
                    analyses.extend(["VOCATIVE"] + list(t.apply_up(tryThis)))
        
                elif word[-3:] == "iiy":
                    # e.g. -> apa
                    tryThis = word[:-2]
                    analyses.extend(["VOCATIVE"] + list(t.apply_up(tryThis)))
        
                elif word[-3:] == "uuy":
                    # e.g. Umiilguuy -> Umiilgu 
                    tryThis = word[:-2]
                    analyses.extend(["VOCATIVE"] + list(t.apply_up(tryThis)))
        
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
                   
            if not analyses:
                allAnalyses.append("?" + word)
            else:
                allAnalyses.append(analyses)
        
             # separates one word's analyses from the next
            allAnalyses.append("<br>")

    return allAnalyses


def prep_input(inputfile):
    '''
    :param inputfile: file containing words
                     to be analyzed
    :type  inputfile: str

    :return: a list of words, stripped of punctuation,
             ready for analysis

    '''
    allWords = []

    with open(inputfile, 'r') as f:
        for sentence in f:
            allWords.append("SENT:" + sentence)

            if sentence != "\n":
                words = sentence.strip("\n ").lower().split(" ")

                for w in words:
                    # strip punctuation except apostrophes
                    word = re.sub(ur"[^\w\d'\-\s]+", '', w)

                    if any(char.isalpha() for char in word):
                        allWords.append(word)

    return allWords


def generate_output_file(allAnalyses, filename, outputdir):
    '''
    :param allAnalyses: all of the analyses for each word in a text
    :type  allAnalyses: list of lists
    :param filename: name of the text
    :type  filename: str
    :param outputdir: name of the directory to which to write the output
    :type  outputdir: str 

    Writes the predicted analyses for a text to a file that is placed
    in the specified output directory.

    '''
    with open(outputdir+"/"+filename, 'w') as f:
        for elem in allAnalyses:

            # analyzer found analyses
            if isinstance(elem, list):

                # handle vocatives
                if elem[0] == "VOCATIVE":
                    for analysis in elem[1:]:
                        writeThis = analysis.split("^")[0] + "^[VOC]"
                        f.write(writeThis.decode("utf-8").encode("utf-8") + "\n")
                else:
                    for analysis in elem:
                        f.write(analysis.decode("utf-8").encode("utf-8") + "\n")

            # newline element; separate the analyses for each word
            elif elem == "<br>":
                f.write("\n")

            # new sentence
            elif len(elem) > 5 and elem[:5] == "SENT:":
                f.write("π ".decode("utf-8").encode("utf-8") + elem.split(":")[1])

            # analyzer did not find analyses
            else:
                f.write(elem + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('analyzer', help='path to foma analyzer')
    parser.add_argument('texts', help='path to directory containing texts to analyze')
    parser.add_argument('outputdir', help='path to output directory')
    args = parser.parse_args()

    # load the analyzer's .fomabin file
    t = FST.load(args.analyzer)

    # run the analyzer over each file in the input directory
    for filename in glob.glob(args.texts + "/*"):
        analyses = analyze_input_file(t, filename)
        generate_output_file(analyses, os.path.basename(filename), args.outputdir)


if __name__ == "__main__":
    main()
