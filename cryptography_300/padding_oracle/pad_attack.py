#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Sun 1 Apr 2018 05:22:01 PM MST
#
###############################
#
#Padding Oracle Attack
#
###############################

from socket import *
import sys
import time

HOST = '0.0.0.0'
PORT = 5000
iv = bytearray(b"\x85\xD4\x85\x6F\x17\x35\xF5\x96\xB7\x26\x6C\x93\xA4\x83\x6C\x8C")
start = time.time()

def run():
    
    f = open('cipher.txt', 'rb')
    orig_cipher = f.read()
    orig_cipher = bytearray(iv + orig_cipher)

    #check for easy incorrect block size error
    if len(orig_cipher) % 16 != 0:
        print("Ciphertext and IV: Incorrect Size")
        return

    else:       
        num_blocks = len(orig_cipher) // 16

    #known_ints will be decoded plaintext as integer
    known_ints = bytearray()

    #known_xor is known plaintext XOR appropriate ciphertext
    #for easy XOR by padding 
    known_xor = bytearray()

    #ignore last block, start at [-2], ignore first block
    for i in range((num_blocks-1), 1, -1):
        hi = i * 16
        lo = (i-1) * 16

        #orig_block is unmodified block sent to oracle
        orig_block = orig_cipher[lo:hi]

        #orig_c is block to be sliced and edited
        orig_c = orig_cipher[(lo-16):(hi-16)]

        for padding in range(1, 17):

            #build left, working, and right portions of new block
            current_byte = orig_c[-padding]
            left_of_byte = orig_c[:-padding]
            right_of_byte = bytearray()

            if padding > 1:

                #build right_of_byte; known_xor XOR padding
                for each in range(1, padding):
                    right_of_byte.append(known_xor[-each] ^ padding)
                
            
            current = time.time()
            print("Time:\t{}, Bytes:{}\tMessage: {}".format(round((current-start), 1), len(known_ints), known_ints.decode(encoding="utf-8", errors="ignore").strip('\r\t\n')), end="\r", flush=True)            
            
            for number in range(256):

                working_byte = number

                test_block = bytearray()
                test_block.extend(left_of_byte)
                test_block.append(working_byte)
                test_block.extend(right_of_byte)
                test_block.extend(orig_block)
                        
                response = test_cipher(test_block)

                if "Hello".encode() in response:
                    
                    #known_int is Pn decoded
                    known_int = padding ^ number ^ current_byte
                    known_ints.insert(0, known_int)

                    #known_xor is known_int XOR chunk_num, easily XOR with padding for future
                    known_xor.append(known_int ^ current_byte)
                    break


    current = time.time()
    print("")
    print("Total Time:\t{} \t Total Bytes Found: {}".format(round((current-start), 1), len(known_ints), known_ints.decode(encoding="utf-8", errors="ignore").strip('\r\t\n')))
    print("Decoded Message: {}".format(known_ints.decode(encoding="utf-8", errors="ignore").strip('\r\t\n')))


# Test some bytes against the padding oracle
def test_cipher(cipher):
    # Make a socket
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST,PORT))

    # Send the ciphertext
    s.send(cipher)

    # Get a response back
    resp = s.recv(1024)
    s.close()
    return resp


#run main program, sys.argv[1] for HOST IP
if __name__ == '__main__':
    if not sys.argv[1:]:
        sys.exit("Need host")
    HOST = sys.argv[1]
    run()