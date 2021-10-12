#! /usr/bin/env pyhton
# -*- coding:utf-8 -*-


def keyGen():
    """this function generate the key map
    :return: the key map
    """
    table = {'a': 'X', 'b': 'E', 'c': 'U', 'd': 'A', 'e': 'D', 'f': 'N', 'g': 'B', 'h': 'K', 'i': 'V', 'j': 'M',
             'k': 'R', 'l': 'O', 'm': 'C', 'n': 'Q',
             'o': 'F', 'p': 'S', 'q': 'Y', 'r': 'H', 's': 'W', 't': 'G', 'u': 'L', 'v': 'Z', 'w': 'I', 'x': 'J',
             'y': 'P', 'z': 'T', }
    return table


def encryption(k, m):
    """ this function achieves the plaintext encryption and print the ciphertext.
    :param k: the encryption key
    :param m: the plaintext
    :return: the ciphertext
    """

    c = ""
    for i in m:
        c = c + k[i]
    print "ciphertext: ", c
    return c


def decryption(k, c):
    """this function achieves the ciphertext decryption and print the plaintext.
    :param k:
    :param c:
    :return: the plaintext
    """

    m = ""
    for i in c:
        m = m + getKey(k, i)
    print "plaintext: ", m
    return m


def getKey(d, value):
    """ this function will return the key according the value

    :param d: the dictionary
    :param value: the value
    :return: key
    """
    for k, v in d.items():
        if v == value:
            return k


if __name__ == "__main__":
    """code starts point"""
    k = keyGen()
    m = raw_input("please input the plaintext(lower case alphabet): ")
    c = encryption(k, m)
    m = decryption(k,c)
