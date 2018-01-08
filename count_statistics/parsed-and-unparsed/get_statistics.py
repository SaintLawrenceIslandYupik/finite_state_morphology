#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script is designed to acquire various statistics from the txt files contained in the 'count-output-txts' directory,
# which contains all words in the evaluation txt files
#
# Usage: ./get_statistics.py count-output-txts/
# The script recursively processes each txt file, starting at the provided root directory

import os
import sys

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
					if "\t" in line and "------------------------" not in line:
						word = line.split("\t")[0]
						num_analyses = line.split("\t")[1]

						# Builds a dictionary where each key is tuple: (word, # analyses)
						# and each value is the number of times that word occurs in
						# the evaluation txts
						tup = (word, num_analyses)

						if tup in d:
							d[tup] += 1
						else:
							d[tup] = 1 

'''
# Print the dictionary
for k in d:
	print("{} => {}".format(str(k), str(d[k])))


# Calculates average and median number of analyses per word
sum_analyses = 0
l = []

for k in d:
	sum_analyses += int(k[1])
	l.append(int(k[1]))

sorted_l = sorted(l)

print "Sum of all analyses = " + str(sum_analyses)
print "Sum of all words = 29805 "
print "Average number of analyses per word = " + str(sum_analyses/29805)
print "Median number of analyses per word = " + str(sorted_l[29805/2])
'''
