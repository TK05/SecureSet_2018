#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Mon 12 Feb 2018 05:22:01 PM MST
#
###############################
#
#Hash Collisions (Birthday Attack) utilizing generation from shh
#
###############################

from shh import *
from collections import Counter
from timeit import default_timer as timer

start = timer()

def default_passwords ():

	#default password list
	with open('4npass.txt') as f:
		default_passwords = f.read().splitlines()

		return default_passwords

#generate list of 1-4 character alphanumeric possibilities
def generate_passwords ():
	from random import shuffle
	import string
	import itertools

	char_num_string=''.join(string.ascii_letters+string.digits)

	passwords = []

	print('Generating passwords...')
	#Adjust range to generate all possible N length combinations
	for i in range (4):
		passwords += [''.join(n) for n in itertools.product(char_num_string, repeat =(i+1))]

	#shuffle because fun
	shuffle(passwords)

	#with open('4npass.txt', 'w') as file:
	#	for password in passwords:
	#		file.write("{}\n".format(password))

	return passwords


#birthday attack to find hash collisions
def birthday_attack (passwords, count=None):

	#default count is entirety of password length
	if count is None:
		count = len(passwords)

	pass_hash = []
	hashes = []
	pass_to_test = passwords[0:count]

	print("Generating hashes...")

	#sgenerate hash from shh.py
	#build pass and hash list to reference
	for i in range(len(pass_to_test)):
		password = pass_to_test[i]
		hasho = short_hash(password)
		hashes.append(hasho)
		pass_hash.append((password, hasho))

	#count hashes to check for collisions
	hash_col = Counter(hashes)

	#return list of collisions where hash value appeared more than once
	collisions = []
	for h, i in hash_col.items():
		if i > 1:
			collisions.append(h)

	#pair hash value with original password
	matches = []
	for match in collisions:
		matches.append([item for item in pass_hash if item[1] == match])

	#with open('collisions.txt', 'w') as file:
	#	for i in range (len(matches)):
	#		file.write("{} {} {}\n".format(matches[i][0][0], matches[i][1][0], matches[i][0][1]))

	if len(matches) > 0:
		for i in range(len(matches)):
			print('the passwords \'{}\' AND \'{}\'\t share a hash of: {} '.format(matches[i][0][0], matches[i][1][0], matches[i][0][1]))	

	print("Hashed {} passwords.".format(len(pass_to_test)))
	print("{} collisions found.".format(len(collisions)))

	stop = timer()
	print("Total time: {} seconds".format(round((stop-start), 2)))


#to generate passwords AND birthday attack
#second argument is # of hashes to generate, blank for max
#max with range 4 is 15018570

#birthday_attack(generate_passwords(), 4000)


#to use 4npass.txt supplied passwords
#second argument is # of hashes to generate, blank for max
#max is 15018570

birthday_attack(default_passwords(), 100000)

