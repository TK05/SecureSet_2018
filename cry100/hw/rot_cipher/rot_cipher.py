#!/usr/bin/python3
#Thomas Kelley - SecureSet 2018 
#Sun 04 Feb 2018 05:22:01 PM MST
#
###############################
#
#Rotation cipher given single word and # to rotate by
#
###############################
import string
 
 
def get_input():
 
    #see if we can limit to alpha only
    text_to_cipher = input("Text to be encoded: ")
 
    while not text_to_cipher.isalpha():
        print("INVALID CHARACTERS")
        text_to_cipher = input("Text to be encoded: ")
 
    #see if we can limit to int only
    rot_num = input("Number to rotate by: ")
 
    while not rot_num.isdigit():
        print("NUMBERS ONLY")
        rot_num = input("Number to rotate by: ")
 
   
    rot_cipher(text_to_cipher, int(rot_num))
 
 
def rot_cipher(text, num):
 
    #modulo for num's > 26 to allow for large shifts
    n = num % 26
 
    #a-z, A-Z tables (IN TABLE)
    uc = string.ascii_uppercase
    lc = string.ascii_lowercase
 
    #uc/lc tables TRANSLATED by ROT N (OUT TABLE)
    #shifts lc&uc by rot#
    rotted_table = (lc[n:] + lc[:n] + uc[n:] + uc[:n])
 
    #make translated table given in & out tables
    #creates dictionary for mapping
    translated_table = str.maketrans((lc+uc), rotted_table)
 
    #cipher with translate on input string
    #text referenced to new ordinal mapping and output is new char
    ciphered_string = text.translate(translated_table)
 
    print("{} --> ROT{} --> {}".format(text, n, ciphered_string))
 
 
get_input()