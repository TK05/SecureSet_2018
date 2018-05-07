#!/usr/bin/python3
#Tommy Kelley - SecureSet - 2018
#Fri Mar  9 00:37:06 MST 2018
#
#################################
#
#Script to find both world writeable files and setuids given
#a starting path from the user. (OS.WALK NOT ALLOWED)
#
#################################

import os
from stat import *
from termcolor import colored
import pathlib

#user input to define starting directory, default for /
start_dir = input("Path to start (default is / ): ") or "/"


#function to check permissions after isfile type confirmed
#return appropriate text color, black if no match
def checkfile(path):
	i = 0
	if oct(os.stat(file)[ST_MODE])[-1] == '7':
		i+=1
	if oct(os.stat(file)[ST_MODE])[-4] == '4':
		i+=2
	if i == 0:
		return('black')
	if i == 1:
		return('red')
	if i == 2:
		return('blue')
	if i == 3:
		return('yellow')

#print color key for file type matches
print("{} | {} | {}".format(colored('WORLD WRITEABLE IN RED', 'red'),\
					 colored('SETUID IN BLUE', 'blue'),\
					 colored('BOTH IN YELLOW', 'yellow')))

#create path history (relatively long for index assignment)
#to compare current path with last path
path_buffer = [''] * 100
last_depth = 0


#loop through files, starting with starting path
for file in pathlib.Path(start_dir).glob('**/*'):

	#check each file, only care for isfile matches
	if os.path.isfile(file):

		#pass to checkfile to check if match and return which match
		i = checkfile(file)

		#no reason to do anything else unless the file is a match
		if i != "black":

			#path object needs to be a string for pretty printing
			file = str(file)

			#split on / to get depth
			path = file.split('/')
			del path[0]
			depth = 0

			#check if current path is same as previous path
			for x in range(len(path)-1):
				try:
					if path[x] == path_buffer[x]:
						break

					else:
						print('----------' * depth, "/", path[x], sep='')
						depth+=1

				except IndexError:
					pass


				path_buffer[x] = path[x]

			last_depth = len(path)
			print('----------' * (last_depth - 1), colored(path[-1], i))
			print(path)	


			





"""
			#for loop to print "tree"
			for x in range(len(path) - 1):

				#print final element with appropriate color
				if x == (len(path) - 2):
					#print('\t' * depth, colored(path[-1], i))
					print('\t' * depth, path[-1], i)
				else:
					#print('\t' * depth, "/", (path[x+1]), sep='')
					print('\t' * depth, "/", path[x+1], sep='')

				depth+=1
"""		
