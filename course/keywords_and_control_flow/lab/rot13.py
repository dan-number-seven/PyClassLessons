# -*- coding: utf-8
"""
encode a message using rot13
"""

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

message = raw_input("Enter your message: ")
print(encode_to_rot13(message))
