#!/usr/bin/env python

import sys

import argparse 

def palindrome_check(string_to_check):
    letters_to_check = len(string_to_check)
    if letters_to_check % 2 == 0:
        letters_to_check = letters_to_check/2
    else:
        letters_to_check = (letters_to_check -1)/2
    print letters_to_check
    samma = 0
    for i in range(letters_to_check):
        if string_to_check[i] == string_to_check[len(string_to_check)-1-i]:
            samma = samma +1
    if letters_to_check == samma:
        print "True"
        return True
    else:
        print "False"
        return False

def encrypt(number, string_to_encrypt):
    new_string = ""
    for i in range(len(string_to_encrypt)):
        new_char = ord(string_to_encrypt[i]) + int(number)
        new_letter = chr(new_char)
        new_string = new_string + new_letter
    print new_string
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Different string handling functions')
    parser.add_argument("-e", "--encrypt", nargs = "+", help="use the encrypt function")
    parser.add_argument("-p", "--palindrome", help="use the palindrome function")
    
    args = parser.parse_args()
    
    if args.encrypt:
        encrypt(args.encrypt[1], args.encrypt[0])
    elif args.palindrome:
        palindrome_check(args.palindrome)
    else:
        print "no arguments"

    
