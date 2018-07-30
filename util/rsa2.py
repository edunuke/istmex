# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:26:00 2018

@author: eduperez
"""

#%%
import json
from Crypto.PublicKey import RSA
import base64
import zerorpc

def decrypt_message(encoded_encrypted_msg, privatekey):
	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    
	return decoded_decrypted_msg
class RequestHandler(object):
    
    def __init__(self):
        with open('C:\\Users\\eduperez\\Desktop\\walletapi\\priv.pem','rb') as file:
            self.privkey = RSA.importKey(file.read())
        with open('C:\\Users\\eduperez\\Desktop\\walletapi\\.enc_cred', 'rb') as file:
            self.enc_cred = file.readlines()[0]
        with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pub.pem','rb') as file:
            self.validpubkey = RSA.importKey(file.read()).publickey().exportKey(format='PEM')

    def getCredentials(self, pubkey):
        try:
            pubkey = json.loads(pubkey).encode('utf-8')
            if pubkey == self.validpubkey:
                decoded_encrypted_msg= base64.b64decode(self.enc_cred)
                decoded_decrypted_msg = self.privkey.decrypt(decoded_encrypted_msg)

                return json.dumps(decoded_decrypted_msg.decode('utf-8'))
        except:

  
            return json.dumps({"error":"you have an eror"})

s = zerorpc.Server(RequestHandler())
s.bind("tcp://127.0.0.1:5000")

try:
    s.run()
except KeyboardInterrupt:
    s.close()