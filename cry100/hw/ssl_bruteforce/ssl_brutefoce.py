#!/usr/bin/python3
#Thomas Kelley - SecureSet - 2018
#Thu Feb  8 20:25:48 MST 2018
#
##########################################
#
#OpenSSL AES-256-CBC bruteforce given key is 3 characters (upper, lower, digit)
#
##########################################

import subprocess
import sys
import string
import itertools
import re
from timeit import default_timer as timer
from random import shuffle

start = timer()

in_file = 'enc_message.data'

#create list of all possible 3 letter upper/lower/digit combinations
def generate_passwords ():

	char_num_string=''.join(string.ascii_letters+string.digits)
	passwords = [''.join(i) for i in itertools.product(char_num_string, repeat =3)]

	#shuffle because fun
	#shuffle(passwords)

	#FULL BRUTEFORCE
	#brutefoce_ssl(passwords)

	#EASY 20 SECOND SOLVE
	brutefoce_ssl(passwords[36000:43764])


#test each key for match
def brutefoce_ssl (passwords):

	poss_pass = []

	for i in range(len(passwords)):

		#make terminal interesting while this happens
		sys.stdout.write('KEY TRY: {}    {} of {}\r'.format(passwords[i], (i+1), len(passwords)))
		sys.stdout.flush()

		#CHECKOUT SUBPROCESS RETURNCODE

		#subprocess popen to run commands in shell
		bash_com = subprocess.Popen('openssl aes-256-cbc -d -a -in {} -k {}'.format(in_file, passwords[i]), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		stdout, stderr = bash_com.communicate()
		stderr = stderr.decode("utf-8")
		#print(type(stderr))
		#print(type(stdout))

		#first test if stderr is empty
		if stderr == "":

			#then test if stdout is unicode
			try:
				stdout.decode('utf-8')			
				break

			except UnicodeError:
				continue

		else:
			continue

	end = timer()
	print("")
	print('KEY FOUND: {}\t SOLVE TIME: {} seconds'.format(passwords[i], round((end-start), 2)))
	print("")
	print("DECRYPTED MESSAGE: ", stdout.decode('utf-8'))


generate_passwords()