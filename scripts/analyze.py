'''
:author Emily Chen:
:date   2020:

'''
import argparse
import glob
import os
import pprint
import string

from foma import *


def generate_output_file(allAnalyses, filename):
    '''
    '''
    with open(filename, 'w') as f:
        for elem in allAnalyses:

            # analyzer found analyses
            if isinstance(elem, list):
                for analysis in elem:
                    f.write(analysis.decode("utf-8").encode("utf-8") + "\n")

            # newline element
            elif elem == "<br>":
                f.write("\n")

            # analyzer did not find analyses
            else:
                f.write(elem)


def analyze_input_file(t, input):
    '''
    :param t: the 'foma' analyzer
    :type  t: not sure tbh
    :param input: path to a file containing
                  the words to be analyzed
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

    with open(input, 'r') as f:

        for sentence in f:
            if sentence != "\n":
                words = sentence.rstrip("\n").lower().split(" ")

                for w in words:
    
                    # strip any punctuation and analyze
                    word = w.translate(None, string.punctuation)
    
                    analyses = list(t.apply_up(word))

                    ''' 
                    some additional processing in case the
                    analyzer can't analyze the word as is
                    '''
                    # handle vowel lengthening in yes-no questions
                    if not analyses:
                        if word[-3:-1] == "aa":
                            # e.g. ighneghaan -> ighneghan
                            tryThis = word[:-3] + "a" + word[-1]
                            analyses = list(t.apply_up(tryThis))
        
                            # e.g. qiyastaak -> qiyastek
                            tryThis = word[:-3] + "e" + word[-1]
                            analyses = list(t.apply_up(tryThis))
        
                        elif word[-2:] == "aa":
                            tryThis = word[:-2] + "a"
                            analyses = list(t.apply_up(tryThis))
        
                        elif word[-3:-1] == "ii":
                            # e.g. qiyaziin -> qiyazin
                            tryThis = word[:-3] + "i" + word[-1]
                            analyses = list(t.apply_up(tryThis))
        
                        elif word[-2:] == "ii":
                            # e.g. qiyatsii -> qiyatsi
                            tryThis = word[:-2] + "i"
                            analyses = list(t.apply_up(tryThis))
        
                        elif word[-3:-1] == "uu":
                            tryThis = word[:-3] + "u" + word[-1]
                            analyses = list(t.apply_up(tryThis))
        
                        elif word[-2:] == "uu":
                            tryThis = word[:-2] + "u"
                            analyses = list(t.apply_up(tryThis))
        
                    # s -> t, g -> k, gh -> q 
                    if not analyses:
                        if word[-1] == "s":
                            tryThis = word[:-1] + "t"
                            analyses = list(t.apply_up(tryThis))
                        elif word[-1] == "g" and word[-2] != "n":
                            tryThis = word[:-1] + "k"
                            analyses = list(t.apply_up(tryThis))
                        elif ''.join(word[-2:]) == "gh":
                            tryThis = word[:-2] + "q"
                            analyses = list(t.apply_up(tryThis))
        
                    # gw -> g or gw -> w
                    if not analyses:
                        if "gw" in word:
                            tryThis = word.replace("gw", "g") 
                            analyses = list(t.apply_up(tryThis))
        
                            tryThis = word.replace("gw", "w")
                            analyses.extend(t.apply_up(tryThis))
           
                    if not analyses:
                        allAnalyses.append(word)
                    else:
                        allAnalyses.append(analyses)
    
                allAnalyses.append("<br>")

    return allAnalyses


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('analyzer', help='path to foma analyzer')
    parser.add_argument('texts', help='path to directory containing texts to analyze')
    args = parser.parse_args()

    # load the analyzer's .fomabin file
    t = FST.load(args.analyzer)

    # run the analyzer over each file in the input directory
    for filename in glob.glob(args.texts + "/*"):
        print(filename)
        analyses = analyze_input_file(t, filename)
        generate_output_file(analyses, os.path.basename(filename))


if __name__ == "__main__":
    main()
