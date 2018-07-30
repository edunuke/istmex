# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:54:36 2018

@author: eduperez
"""
#%%
import json
fname = 'C:\\Users\\eduperez\\Desktop\\walletapi\\key'
with open(fname) as f:
    content = json.loads(f.readlines()[0])

#%%
from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_keys():
	# RSA modulus length must be a multiple of 256 and >= 1024
	modulus_length = 256*4 # use larger value in production
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey

def encrypt_message(a_message , publickey):
	encrypted_msg = publickey.encrypt(a_message, 32)[0]
	encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
	return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
	return decoded_decrypted_msg

#%%
            
a_message = "{'rpc_user': 'edunuke', 'rpc_password': 'mysupersecretpwd', 'host': 'localhost', 'port': '18443'}".encode('utf-8')
privatekey , publickey = generate_keys()
encrypted_msg = encrypt_message(a_message , publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey).decode('utf-8')

#%%


with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pub.pem', 'wb') as file:
    file.write(privatekey.exportKey())
#%%
    
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\priv.pem', 'wb') as file:
    file.write(privatekey.exportKey())
#%%

with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pub.pem','rb') as file:
    pubkey = RSA.importKey(file.read())

encrypted_msg = encrypt_message(a_message , pubkey)
#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\priv.pem','rb') as file:
    privkey = RSA.importKey(file.read())

decrypted_msg = decrypt_message(encrypted_msg, privkey).decode('utf-8')

#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\key_enc', 'wb') as file:
    file.write(encrypted_msg)
    
#%%
f = open('C:\\Users\\eduperez\\Desktop\\walletapi\\priv.pem','rb') as file:
privkey = RSA.importKey(file.read())
