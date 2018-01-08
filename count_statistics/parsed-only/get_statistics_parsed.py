#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script is designed to acquire various statistics from the txt files contained in the 'parsed-only-txts' directory,
# which contains only those words that the morphological analyzer was capable of parsing.
#
# Usage: ./get_statistics_parsed.py parsed-only-txts/
# The script recursively processes each txt file, starting at the provided root directory

import os
import sys
from operator import itemgetter

d = {}

walk_dir = sys.argv[1]

# print('walk_dir = ' + walk_dir)

# print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
#	print('--\nroot = ' + root)
	list_file_path = os.path.join(root, 'x.txt')
#	print('list_file_path = ' + list_file_path)

	with open(list_file_path, 'r') as list_file:
#		for subdir in subdirs:
#			print('\t- subdirectory ' + subdir)

		for filename in files:
			file_path = os.path.join(root, filename)

#			print('\t- file %s (full path: %s)' % (filename, file_path))

			with open(file_path, 'r') as f:
				lines = f.readlines()		

				word = ""
				num_analyses = 0

				for line in lines:
					line = line.strip()

					if not line:
						tup = (word, num_analyses)

						# Builds a dictionary where each key is a tuple: (word, # analyses)
						# and each value is the number of occurrences of that word across
						# all the txts in the root directory
						if tup in d:
							d[tup] += 1
						else:
							d[tup] = 1 

						word = ""
						num_analyses = 0

					elif "\t" in line:
						word = line.split("\t")[0]
						num_analyses += 1 

'''
# Prints the dictionary
for k in d:
	print("{} => {}".format(str(k), str(d[k])))

#-----------------------------------------------------------#

# Calculates average and median number of analyses per word
# and the number of words that occur more than 'x' times
sum_analyses = 0
l = []
geq = []

for k in d:
	n = int(k[1])
	sum_analyses += n 
	l.append(n)

	if n > 6:
		geq.append(k)

sorted_l = sorted(l)
sorted_geq = sorted(geq)

print "Sum of all analyses = " + str(sum_analyses)
print "Sum of all words = 19701"
print "Average analyses per word = " + str(sum_analyses/19701)
print "Median analyses per word = " + str(sorted_l[19701/2])

print "Num words with num analyses greater than 6 = " + str(len(sorted_geq)) + "\n"

#-----------------------------------------------------------#

# Prints occurrence frequency for each word and top ten most frequently-occurring words
freq = []

for k in d:
	freq.append((d[k], k[0]))	

sorted_freq = sorted(freq, key=itemgetter(0), reverse=True)

print "Top ten most frequently-occurring words = " + str(sorted_freq[0:11])
'''
