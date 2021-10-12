#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
just achieve the Caesar Cipher, user can choose the random number between 0 to 25 to encrypt the message by lowercase letters.
"""

def keyGen():
    """ user inputs the shift_number as the encryption key."""
    shift_number = raw_input('please input the key(interger, must between 0 to 25): ')
    return int(shift_number)

def encrption(k,m):
    """ this function achieves the message encryption and print the ciphertext.
    :param k: the encryption key
    :param m: the plaintext
    """
    c = ""
    for letter in m:
        c_letter_index = (ord(letter) + k - 97) % 26
        c = c + chr(c_letter_index + 97)
    print "ciphertext: ",c
    return c




def decription(k,c):
    """ this function achieves the message decryption and print the plaintext.
        :param k: the decryption key
        :param c: the ciphertext
        """
    m = ""
    for letter in c:
        m_letter_index = ((ord(letter) - 97) - k) % 26
        m = m + chr(m_letter_index + 97)
    print "plaintext: ",m
    return m


if __name__ == '__main__':
    """code start point"""
    k = keyGen()
    m = raw_input("please input the plaintext(lower case alphabet): ")
    c = encrption(k,m)
    m_ = decription(k,c)



