#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Mon 19 Feb 2018 05:22:01 PM MST
#
###############################
#
#Convert Cert Hex to Integer
#
###############################

import re


#cert.hex format will be hex values, MODULUS FIRST
#seperated by a colon
with open('cert.hex') as f:
	cert = f.read()
	cert = re.sub(r"[\n\t\s]*", "", cert)
	cert = re.split(':', cert)

print("MODULUS")
modulus_int = cert[0]
print(int(modulus_int, 16))


print("EXPONENT")
exponent_int = cert[1]
print(int(exponent_int, 16))