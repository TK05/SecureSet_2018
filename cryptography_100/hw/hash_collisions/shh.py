#!/usr/bin/python3

import hashlib

def hexlify(byte_string):
	ret = ''
	for b in byte_string:
		ret += hex(b)[2:]
	return ret

def xor(a,b):
	assert len(a) == len(b)
	byte_list = []
	for i in range(len(a)):
		byte_list.append(a[i] ^ b[i])
	return bytes(byte_list)

def short_hash(msg):
	msg = msg.encode()
	s = hashlib.sha1()
	m = hashlib.md5()
	s.update(msg)
	m.update(msg)
	X = xor(s.digest()[:16], m.digest())
	X = X[:3]
	return hexlify(X)

	
