#! /usr/bin/env python
# -*- coding:utf-8 -*-


def keyGen():
    """generate the key"""

    key = raw_input("please input the key(lower case alphabet): ")
    k = []
    for letter in key:
        index = ord(letter) - 97
        k.append(index)
    return k


def encryption(k, m):
    """the function achieves the plaintext encryption and print the ciphertext.
    :param k: the key
    :param m: the plaintext
    :return: the ciphertext
    """

    c = ""
    k_ = k
    klen = len(k)
    k_len = len(k)
    m_len = len(m)

    while m_len > k_len:
        k += k_
        k_len += klen

    index = 0
    for letter in m:
        letter_index = (ord(letter) - 97 + k[index]) % 26
        c += chr(letter_index + 65)
        index += 1
    print "ciphertext: ", c
    return c


def decryption(k, c):
    """the function achieves the ciphertext decryption and print the plaintext.
    :param k: the key
    :param c: the ciphertext
    :return:  the plaintext
    """

    m = ""
    k_ = k
    klen = len(k)
    k_len = len(k)
    c_len = len(c)

    while c_len > k_len:
        k += k_
        k_len += klen

    index = 0
    for letter in c:
        letter_index = (ord(letter) - 65 - k[index]) % 26
        m += chr(letter_index + 97)
        index += 1
    print "plaintext: ", m
    return m


if __name__ == "__main__":
    """the code start point"""
    k = keyGen()
    m = raw_input("please input the plaintext(lower case alphabet): ")
    c = encryption(k, m)
    m_ = decryption(k, c)
    if m == m_:
        print "success"
