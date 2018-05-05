#!/usr/bin/python3
#Thomas Kelley - SecureSet - 2018
#Wed 07 Feb 2018 07:33:33 PM MST
#
########################
#
#Simple substitution cipher solver that is only partly automated
#
#########################

import re
from collections import Counter, OrderedDict
from operator import itemgetter


#global variables
char_string = ""
#order of most common english letters
eng_string = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
deciphered_text = ""


#ciphered text path
filepath = "ciphered_text.txt"
f = open(filepath)
init_text = f.read()

#strip newlines/spaces/tabs, form single string
init_text = re.sub(r"[\n\t\s]*", "", init_text)


#count characters 
#basic frequency analysis
#generate basic string for comparison
def step_1_frequency_analysis():
	global char_string

	#ordered dictionary of characters and their count
	char_text_count = Counter(init_text)
	char_text_count = OrderedDict(sorted(char_text_count.items(), key=itemgetter(1), reverse = True))

	char_string = ""

	#dict to string for first guess
	for c, n in char_text_count.items():
		char_string+=c

	return decipher(init_text)



#bigram finder and letter swap
def step_2_bigrams(bigram):  
	global eng_string

	#modify eng_string to match given bigram
	next_letter_to = ''
	for i in range (len(deciphered_text)):
		if deciphered_text[i] == bigram[0]:
			next_letter_to+=deciphered_text[i+1]

	#sum all "next letter" to bigram
	next_letter_to_count = Counter(next_letter_to)
	next_letter_to_count = OrderedDict(sorted(next_letter_to_count.items(), key=itemgetter(1), reverse = True))
	
	####
	#bigram chart for manual review
	#print("For bigram {}, most common letters RIGHT of {} are:".format(bigram, bigram[0]))
	#print(next_letter_to_count)
	####

	next_letter_to_is = [x[0] for x in next_letter_to_count]
	next_letter_to_is = next_letter_to_is[0]

	letter_swap(next_letter_to_is, bigram[1])
	

	""""
	new_find_index = eng_string.find(next_letter_to_is)
	old_index = eng_string.find(bigram[1])
	eng_string = eng_string[:new_find_index] + bigram[1] + eng_string[new_find_index + 1:]
	eng_string = eng_string[:old_index] + next_letter_to_is + eng_string[old_index + 1:]
	"""

	return decipher(init_text)


#double letter finder
def step_3_double_letters():
	global eng_string

	double_letters =''
	for i in range (len(deciphered_text)-1):
		if deciphered_text[i] == deciphered_text[i+1]:
			double_letters+=deciphered_text[i]

	dl_count = Counter(double_letters)
	dl_count = OrderedDict(sorted(dl_count.items(), key=itemgetter(1), reverse = True))

	###
	#double letter count for manual review
	#print("Most Common DOUBLE LETTERS")
	#print(dl_count)
	###

	#enter LETTER 1 to be replaced with LETTER 2
	#ex, ('I', 'S') where old_index I and S swap
	letter_swap('I', 'S')

	return decipher(init_text)


def step_4_start_guessing():
	global eng_string

	#manually change key string to make ciphered text more readable

	#try C to W, U to M
	#eng_string after frequency, bigrams, double letters
	#ETAOHNISRDLCUMWFGYPBVKJXQZ
	#eng_string = "ETAOHNISRDLWMUCFGYPBVKJXQZ"

	#try B to K, Y to G
	eng_string = "ETAOHNISRDLWMUCFYGPKVBJXQZ"

	#try C to Y, V to P
	#eng_string = "ETAOHNISRDLWMUYFCGVKPBJXQZ"

	#try C to B
	#eng_string = "ETAOHNISRDLWMUYFBGVKPCJXQZ"

	#FINAL KEY STRING
	#try V to C
	#eng_string = "ETAOHNISRDLWMUYFBGCKPVJXQZ"

	return decipher(init_text)


#swap letters
def letter_swap(let_old, let_new):
		global eng_string

		#replace I with S
		new_lo_index = eng_string.find(let_old)
		new_ln_index = eng_string.find(let_new)
		eng_string = eng_string[:new_ln_index] + let_old + eng_string[new_ln_index + 1:]

		eng_string = eng_string[:new_lo_index] + let_new + eng_string[new_lo_index + 1:]

		return eng_string


#trans table to decipher
def decipher(text):
	global deciphered_text

	#make translated table given in & out tables
	#creates dictionary for mapping
	translated_table = str.maketrans(char_string, eng_string)

	#return deciphered string based on translated table
	deciphered_text = text.translate(translated_table)

	return deciphered_text


#required
print(init_text[0:100])
step_1_frequency_analysis()
#print(deciphered_text[0:100])

#bigram to try
#ideally, left letter would be correct, try and find new right character
step_2_bigrams('TH')
#print(deciphered_text[0:100])

#double letter find
#inner function to replace
step_3_double_letters()
#print(deciphered_text[0:100])

#look at return of step 3 and make incremental string swaps (MANUAL PROCESS)
#will essentially rewrite eng_string so only steps 1 and final decipher need ran
step_4_start_guessing()
print(deciphered_text[0:100])

#HW PORTION
#use ciphered key to decipher hw string
#hwstring = "LCOGY JGFVI MVEWI"

#swap # depending on desired output
#print(decipher(hwstring))
print(deciphered_text)

#find way to take non-spaced string and insert spaces on word matches
#step_5_wizard_stuff()
