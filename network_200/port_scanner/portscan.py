#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Sun 4 Mar 2018 05:22:01 PM MST
#
###############################
#
#A painfully slow port scanner
#
###############################

import socket

host = input("IP to Scan: ")
start_port = int(input("Starting Port: "))
end_port = int(input("Ending Port: "))


for port in range(start_port, (end_port+1)):
	try:
		#print("Connecting to {} on port {}".format(host, port))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)

		result = s.connect_ex((host, port))

		if result == 0:
			print("Port {} is open".format(port))
			s.close()

		#else:
		#	print("Port {} is closed".format(port))
	
	except:
		pass
