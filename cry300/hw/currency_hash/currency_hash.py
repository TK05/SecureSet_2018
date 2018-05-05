#!/usr/bin/python
#Thomas Kelley - SecureSet 2018 
#Thur 15 Mar 2018 05:22:01 PM MST
#
###############################
#
#Take in transaction as string, take in target as difficulty
#random starting nonce, compute hashes until less than target
#
###############################

from random import *
import hashlib
import sys

def hash_check (transaction, target):

	#random 32 bit nonce
	nonce = getrandbits(32)

	#using sha256 hashing algorithm
	hash_1 = hashlib.sha256()

	#loop, cat new string, new hash of string, nonce+=1, etc.
	while 1:
		string_to_test = transaction + str(nonce)
		hash_1.update(string_to_test)
		hash_digest = hash_1.hexdigest()

		if int(hash_digest, 16) < target:
			print(hash_digest)

			#i was told to return so i will return
			return(hash_digest)
			break

		else:
			nonce+=1


hash_check(str(sys.argv[1]), int(sys.argv[2]))