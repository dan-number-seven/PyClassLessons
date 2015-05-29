# -*- coding: utf-8
"""
encode a message using rot13
"""

#import sys
from __future__ import print_function

# where is the message going to be coming from
#input = raw_input("Enter message: ")

message="Why did the chicken cross the road?"
wikipedia_result="Jul qvg gur puvpxra pebff gur ebnq?"

print("The input message is : " + message)

def encode_to_rot13(message):
    """
    """
    INPUT_ARRAY ="ABCDEFGHIJKLMNOPQRSTUVWXYZ".split()
    OUTPUT_ARRAY="NOPQRSTUVWXYZABCDEFGHIJKLM".split()

    for letter in message:
        printf('%s', letter)

encode_to_rot13(message)





