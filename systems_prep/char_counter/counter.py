#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Sun 04 Feb 2018 05:22:01 PM MST
#
###############################
#
#Word count and letter count on given text
#
###############################

import re
import string
from collections import Counter, OrderedDict
from operator import itemgetter

#user input for file
#user input for output desired
def get_parameters():

	#get file path and open
	filepath = input("Path to text file (default.txt included): ")
	f = open(filepath)
	text = f.read()

	#lets make a loop for correct user input
	param = 0
	count = 0

	while param == 0:

		#what does user want?
		#words, how many? character count
		user_input = input("Would you like a WORD count or a CHARACTER count? ")
		if user_input.lower() in ('character', 'characters'):
			param = 1
		elif user_input.lower() in ('word', 'words'):
			param = 2
			count = int(
				input("How many words would you like to see? (enter a number): "))
		#ability to surrender
		elif user_input.lower() in ('exit'):
			break
		#return to top
		else:
			print('Try Again, or type EXIT to exit')
			print(user_input)

	#send to format
	format_file(text, param, count)

#format/parse/filter file
#remove unwanted elements, only concerned with words (and characters)
#depending on if user wants words or character count
def format_file(file, param, count):

	#make text cleaner
	#remove punctuation
	translator = str.maketrans('', '', string.punctuation)
	file = file.translate(translator)

	#remove blanks and newlines, split
	lines = re.split('\s', file)
	lines = list(filter(None, lines))

	#convert to all lowercase
	lines = [w.lower() for w in lines]

	#remove integers from list
	lines = [x for x in lines if not (x.isdigit() 
									or x[0] == '-' and x[1:].isdigit)]

	#format for either word or count function
	#if word, keep count and words intact
	#if character, drop count
	if param == 1:
		char_list(lines)
	elif param == 2:
		word_count(lines, count)
	else:
		print("Something went wrong, sorry.")

#function for counting of words
#take in count to determine how verbose the result
def word_count(words, count):

	#create word count and sort by most common
	words = Counter(words)
	words.most_common()

	#order dictionary decending
	words = OrderedDict(sorted(words.items(), key=itemgetter(1), reverse = True))

	#back to list for indexing
	words = list(words.items())

	#get length and make out of range less ugly
	words_length = len(words)
	if count > words_length:
		print("There are only {} words in this file.".format(words_length))
		return

	#return the result, looks pretty meh
	print("The {} most common words are:".format(count))
	print("  |'word'|,|count|")
	for i in range(count):
		output = words[i]
		print("{}.".format(i+1), output)
	
		
#function for character count
#take filtered list of words and break into characters
#count the characters and then display results
def char_list(words):
	
	#build base list with all letters
	list_letters = []

	letters = string.ascii_lowercase

	for i in range(len(letters)):
		list_letters.append(letters[i])

	#pass to count
	char_count(list_letters, words)


def char_count(list_letters, words):

	#use sum to populate list_letters
	letter_count = ''
	final_list = []

	#iterate through char list, attach char count
	for i in range(len(list_letters)):
		char_out = list_letters[i]
		letter_count = sum(c.count(char_out) for c in words)
		final_list.append((char_out, letter_count))
		print("{}: {}".format(char_out, letter_count))


#start process
get_parameters()
