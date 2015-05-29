# -*- coding: utf-8
"""
encode a message using rot13
"""

from __future__ import print_function


message="Why did the chicken cross the road?"
wikipedia_result="Jul qvg gur puvpxra pebff gur ebnq?"

def encode_to_rot13(message):
    """ accepts a string, encodes it and returns a result."""

    alphabet ="abcdefghijklmnopqrstuvwxyz"

    result = list()
    for character in message:
        if character.lower() in alphabet:
            rotated_index = (alphabet.index(character.lower()) + 13) % 26
            if character.isupper():
                result.append(alphabet[rotated_index].upper())
            else:
                result.append(alphabet[rotated_index])
        else:
            result.append(character)

    result = ''.join(result)
    return result

print(encode_to_rot13(message))
