#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/21 1:43 AM
# @Author : Archer
# @File : aes_demo.py
# @desc : pip install pycryptodemo
"""
import hashlib
from Crypto.Cipher import AES
import base64

class prpcrypt():
 def __init__(self, key):
  self.key = key # 因为在python3中AES传入参数的参数类型存在问题，需要更换为 bytearray , 所以使用encode编码格式将其转为字节格式（linux系统可不用指定编码）
  IV = 16 * '\x00'
  self.iv=IV.encode("utf-8")
  self.mode = AES.MODE_CBC
  self.BS = AES.block_size
  #pkcs5padding方式，当数据并非16倍数时，末尾添加padding进行补齐
  self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
  self.unpad = lambda s: s[0:-ord(s[-1])]

 # 加密
 def encrypt(self, text):
  text = self.pad(text).encode('utf-8')
  cryptor = AES.new(self.key, self.mode, self.iv)
  # 目前AES-128 足够目前使用(CBC加密)
  ciphertext = cryptor.encrypt(text)
  # base64加密
  return base64.b64encode(bytes(ciphertext))

 # 解密
 def decrypt(self, text):
  # base64解密
  text = base64.b64decode(text)
  cryptor = AES.new(self.key, self.mode, self.iv)
  # CBC解密
  plain_text = cryptor.decrypt(text)
  # 去掉补足的空格用strip() 去掉
  return self.unpad(bytes.decode(plain_text).rstrip('\0')) # 解密字节？？？
  # return bytes.decode(plain_text).rstrip('\0') # 解密字节？？？


def gen_binsha(data):
 shavalue = hashlib.sha256()
 shavalue.update(data)
 return shavalue.digest()

if __name__ == '__main__':
 key = b'SixteenabytebkeySixteenabytebkey'
 # 根据不同密钥长度选择不同加密方式
 # AES-128  key:128bits
 # AES-192  key:192bits
 # AES-256  key:256bits
 pc = prpcrypt(key=key) # 初始化密钥 和 iv
 text='qwerqwerkkk1hhhh1234'
 print(len(text))
 e = pc.encrypt(text) # 加密
 d = pc.decrypt(e) # 解密
 print("加密:%s" % e)
 print("解密:%s"% d)
 print("长度:%s"% len(d))