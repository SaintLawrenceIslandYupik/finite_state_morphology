'''
:author: Emily Chen
:date:   2019

A collection of super janky print functions to print out
various aspects of the "evaluation report" for the 'foma'
analyzer on a given dataset.

If gold standards were provided, the report will include
precision, recall, f-measure, and coverage statistics,
as well as a list of words that could not be analyzed and
a list of incorrect analyses paired with their target
analysis.

If gold standards were NOT provided, the report will
simply include a coverage percentage and a list of words
that could not be analyzed.

'''
from numpy import median

def print_eval_report(hasGold, predicted, unanalyzed, output, target=[]):
    '''
    :param hasGold: specifies whether gold standards were provided
    :type  hasGold: boolean
    :param predicted: all of the analyzer's predicted analyses
    :type  predicted: list of lists
    :param unanalyzed: all of the words the analyzer could not analyze
    :type  unanalyzed: list
    :param output: dict of analyzer outputs where each key
                   is a word and each value is a list of
                   predicted analyses for that word 
    :type output: dict
    :param target: the gold standard analyses 
    :type  target: list

    Master function to print the full evaluation report.

    '''
    print("\n=================")
    print("EVALUATION REPORT")
    print("=================")

    if hasGold:
        print_unanalyzed_words(unanalyzed)
        print_incorrect_analyses(predicted, target) 
        print_analysis_counts(output)
        print_prfc(predicted, target)
    else:
        print_unanalyzed_words(unanalyzed)
        print_analysis_counts(output)
        print_coverage(predicted)


def print_prfc(predicted, target):
    '''
    :param predicted: the analyses predicted by the
                      'foma' analyzer for a given
                      list of words
    :type  predicted: list of lists
    :param target: the gold analyses for a given
                   list of words
    :type  target: list

    Prints precision, recall, f-measure, and coverage of the
    'foma' analyzer for the given list of words, where precision,
    recall, f-measure, and coverage are defined as:

        * precision = # correct analyses / # items with analyses
        * recall    = # items with analyses / # total items
        * f-measure = 2 * (precision * recall / (precision + recall))
        * coverage = # items analyzed / # total items

    '''
    num_correct = 0
    num_analyzed = 0
    num_total = len(target)

    for idx, goldAnalysis in enumerate(target):
        if predicted[idx]:
            num_analyzed += 1

            if goldAnalysis in predicted[idx]:
                num_correct += 1

    precision = float(num_correct) / num_analyzed
    recall    = float(num_correct) / num_total
    fmeasure  = 2 * (precision * recall) / float(precision + recall)
    coverage  = float(num_analyzed) / num_total

    print("\n+----------------------------+")
    print("| Precision | " + str(precision) + " |")
    print("+-----------|----------------+")
    print("| Recall    | " + str(recall) + " |")
    print("+-----------|----------------+")
    print("| F-Measure | " + str(fmeasure) + " |")
    print("+-----------|----------------+")
    print("| Coverage  | " + str(coverage) + " |")
    print("+----------------------------+")
    print("Correct Analyses    = " + str(num_correct))
    print("Items with Analyses = " + str(num_analyzed))
    print("Total Items         = " + str(num_total))


def print_incorrect_analyses(predicted, target):
    '''
    :param predicted: all of the analyzer's predicted analyses
    :type  predicted: list of lists
    :param target: the gold standard analyses 
    :type  target: list

    Prints all of the incorrect analyses paired with their
    respective gold analyses.

    '''
    d = {}

    for idx, goldAnalysis in enumerate(target):
        if predicted[idx] and goldAnalysis not in predicted[idx]:
            d[goldAnalysis] = predicted[idx]

    print("\n------------------")
    print("Incorrect Analyses")
    print("------------------")

    for key in d:
        print("TARGET: " + key.decode("utf-8"))
        print("PREDICTED: ")
        for value in d[key]:
            print("  " + value.decode("utf-8"))
        print(" ")



def print_coverage(allPredictedAnalyses):
    '''
    :param allPredictedAnalyses: the analyses predicted by the
                                 'foma' analyzer for a given
                                 list of words
    :type  allAnalyses: list of lists

    Prints the coverage of the 'foma' analyzer for the given
    list of words, where coverage is defined as:

        * coverage = # items analyzed / # total items

    '''
    num_analyzed = sum(len(sublist) > 0 for sublist in allPredictedAnalyses)
    num_total    = len(allPredictedAnalyses)
    coverage     = float(num_analyzed) / num_total

    print("\n+-----------------------------+")
    print("| Coverage   | " + str(coverage) + " |")
    print("+-----------------------------+")
    print("Items with Analyses = " + str(num_analyzed))
    print("Total Items         = " + str(num_total))



def print_unanalyzed_words(unanalyzed):
    '''
    :param unanalyzed: all of the words the analyzer could not analyze
    :type  unanalyzed: list

    Prints all of the words that the analyzer could not analyze.

    '''
    print("\n--------------------------------")
    print("Words That Could Not Be Analyzed")
    print("--------------------------------")

    for word in unanalyzed:
        print(word)



def print_analysis_counts(output):
    '''
    :param output: dict of analyzer outputs where each key
                   is a word and each value is a list of
                   predicted analyses for that word 
    :type output: dict

    Prints:
      * the average number of analyses per word in the dictionary
      * the median number of analyses per word
      * the word with the greatest number of analyses and the amount 

    '''
    print("\n------------------------")
    print("Assorted Analysis Counts")
    print("------------------------")

    totalAnalyses = 0

    wordWithMaxAnalyses = ""
    maxNumAnalyses = 0

    numAnalysesList = []

    for key, value in output.items():
        totalAnalyses += len(value)

        if len(value) > maxNumAnalyses:
            wordWithMaxAnalyses = key
            maxNumAnalyses = len(value)

        numAnalysesList.append(len(value))

    print("Average Number of Analyses = " + str(float(totalAnalyses)/len(output)))
    print("Median Number of Analyses  = " + str(median(numAnalysesList)) + "\n")
    print("Word with Greatest Number of Analyses  = " + wordWithMaxAnalyses)
    print("Greatest Number of Analyses  = " + str(maxNumAnalyses))
