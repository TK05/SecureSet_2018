#!/usr/bin/python3
#Fri 16 Feb 2018 05:22:01 PM MST
#
###############################
#
#Verify HMACs, output non matches
#
###############################

import hmac

#generate tag given msg (from tags.txt) and key (master.key)
def gen_tag(msg, key):
    hm = hmac.new(key.encode())
    hm.update(msg.encode())
    return hm.hexdigest()

#open original tags (string and hash) for comparison
with open('tags.txt') as f:
	tags = f.read().splitlines()

with open("master.key") as f:
    key = f.read()

string_and_hash = []

#split tags.txt into listed tuples 
for tag in tags:
	new_line = tag.split(":")
	string_and_hash.append((new_line[0], new_line[1]))


#take string from tags.txt and generate new tag
#compare gen tag to given tag
#collect non-matches, print to screen and write to file
newfile = open('non_hmac_matches.txt', 'w')
print("NON MATCHES")

for line in string_and_hash:
	hashn = gen_tag(line[0], key)
	if hashn != line[1]:
		print("String: \t{}".format(line[0]))
		print("Given Hash: \t{}".format(line[1]))
		print("Gen Hash: \t{}".format(hashn))
		newfile.write("{}\n".format(line[0]))

newfile.close()





	


