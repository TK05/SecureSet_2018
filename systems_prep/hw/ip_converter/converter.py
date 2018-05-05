#!/usr/bin/python3
# Thomas Kelley - SecureSet - 2018
# Wed 07 Feb 2018 09:48:44 PM MST
#
#####################################
#
# Convert IP address to a number, and a number to an
# ip address
#
#####################################


# check if active, stop infinite loop
class Active(Exception): pass


# check int between 0 and 4294967295
# create 32 bits, convert int to binary
# format appropriately
def num_to_ipv4(number):

	if 0 <= number <= 4294967295:
		num = bin(number)[2:]
		digits = len(num)
		remain = 32 - digits
		start = '0'*remain
		binary = start + num
		ip1 = int(binary[0:8], 2)
		ip2 = int(binary[8:16], 2)
		ip3 = int(binary[16:24], 2)
		ip4 = int(binary[24:32], 2)

		result = ("{}.{}.{}.{}".format(ip1, ip2, ip3, ip4))
		print("{} as an IPv4 address is: {}".format(number, result))
		raise Active
			
	elif number < 0:
		print('The integer cannot be negative.')
	else:
		print('The integer cannot be larger than 4294967295.')

#turn ip addres into an integer
def ipv4_to_num(ip):

	#split string on .
	splitted = ip.split('.')
	
	#check valid IPv4 format
	#build binary octets
	#convert octets to number
	if len(splitted) == 4:

		#this is sloppy
		oct1 = int((splitted[0]))
		oct2 = int((splitted[1]))	
		oct3 = int((splitted[2]))		
		oct4 = int((splitted[3]))

		#check validity
		if oct1 > 255 or oct2 > 255 or oct3 > 255 or oct4 > 255:
			print('{} is not a valid IPv4 address.'. format(ip))

		elif oct1 < 0 or oct2 < 0 or oct3 < 0 or oct4 < 0:
				print('{} is not a valid IPv4 address.'. format(ip))
			
		else:
			oct1 = "{0:08b}".format(oct1)
			oct2 = "{0:08b}".format(oct2)
			oct3 = "{0:08b}".format(oct3)
			oct4 = "{0:08b}".format(oct4)
			num = int(("{}{}{}{}".format(oct1, oct2, oct3, oct4)), 2)

			print("{} in binary as a number is: {}".format(ip, num))
			raise Active

	else:
		print('{} is not a valid IPv4 address.'.format(ip))


#take user input
#check if either a number or an ip address
#pass to appropriate function
def int_or_binary():
	
	iob = input("Enter an integer or an IPv4 address (type EXIT to exit):")
	
	if iob.lower() == 'exit':
		raise Active
	elif iob.count('.') == 3:
		iob = str(iob)
		ipv4_to_num(iob)
	elif iob.count('.') != 3 and iob.count('.') == 0:
		num_to_ipv4(int(iob))
	else:
		print('This is neither an integer nor a valid IPv4 address.')

#initial function
def whole_shabang():

	#only print this at the beginning, once
	print("")
	print("The CONVERTER will convert and integer into an IPv4 address")
	print("or convert an IPv4 address into an integer.")
	print("")

	#continue asking if input not valid
	try:
		while True:
			int_or_binary()

	except Active:
		pass

#runnnnnnnnnnnn it
whole_shabang()
