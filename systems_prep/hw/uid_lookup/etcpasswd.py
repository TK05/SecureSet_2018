#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Sun 04 Feb 2018 05:22:01 PM MST
#
###############################
#
#Take in username or uid, lookup in /etc/passwd, return
#corresponding uid or username
#
###############################

#open /etc/passwd and split on newline
f = open("/etc/passwd")
text = f.read()
lines = text.split('\n')

#delete empty last value
del lines[-1]

#initialize usernames and uid
names_uid = []

#further splice each item
for line in lines:
	t = line.split(':')
	username = t[0]
	uid = t[2]
	names_uid.append((username, uid))

#print(names_uid[0][0])

#user input, either username or uid
def get_input():
	print("")
	print("Enter a USERNAME to return that user's UID")
	print("or enter a UID to return that user's USERNAME")
	print("")

	user_input = input("")

	#determine UID or name based on input
	if user_input.isdigit():

		#check if uid is in list
		for uid in names_uid:
			if uid[1] == user_input:
				print("{} is UID for {}".format(user_input, uid[0]))
				break
		else:
			print("{} UID NOT FOUND in /etc/passwd".format(user_input))

	else:
		#check if username is in list
		for name in names_uid:
			if name[0] == user_input:
				print("{} is UID for {}".format(name[1], user_input))
				break
		else:
			print("{} USERNAME NOT FOUND in /etc/passwd".format(user_input))
	

get_input()
