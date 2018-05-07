#!/usr/bin/python3
#Tommy Kelley - SecureSet - 2018
#Fri Mar  9 00:37:06 MST 2018
#
#################################
#
#Script to find both world writeable files and setuids given
#a starting path from the user. Replicate something similar to
#pstree to format printing. (OS.WALK NOT ALLOWED)
#
#################################

import os
from stat import *
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
		return('none')
	if i == 1:
		return('WORLD WRITEABLE')
	if i == 2:
		return('SETUID')
	if i == 3:
		return('BOTH')

#create path history (relatively long for index assignment)
#to compare current path with last path
path_buffer = [''] * 100
last_depth = 0

#loop through files, starting with starting path
for file in pathlib.Path(start_dir).glob('**/*'):

	if os.path.isfile(file):

		i = checkfile(file)

		if i != "none":

			file = str(file)
			path = file.split('/')
			del path[0]
			depth = 0

			#check if current path is same as previous path
			for x in range(len(path) - 1):
				try:
					if path[x] == path_buffer[x]:
						depth+=1
						pass

					else:
						print('__________' * depth, "/", path[x], sep='')
						depth+=1
						path_buffer[x] = path[x]

				except IndexError:
					pass

			last_depth = len(path)
			print('__________' * (last_depth - 1), "/", path[-1], ' - ', i, sep='')	