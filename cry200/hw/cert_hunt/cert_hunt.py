#!/usr/bin/python3
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