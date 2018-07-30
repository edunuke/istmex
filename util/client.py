# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:49:52 2018

@author: eduperez
"""

#%%
import json
from Crypto.PublicKey import RSA



with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pub.pem','rb') as file:
    pubkey = RSA.importKey(file.read())


a = json.dumps(pubkey.publickey().exportKey(format='PEM').decode('utf-8'))
#print (json.loads(resp.encode('utf-8')))

#%%
import requests
import json
yourparams = {'key' : '8f85b16c9348b536720ca94fc4729013a00119a7bb122303c8d495e4e79fb42e6ecec14d6b1abc44ebe189d9e40156081cc15890a837955eae4ef24d4f7acc381c2e2a9169c2125ed8b80d42c5b1bb214754008d3adfed80dc0af210f0d3c0fb3a989f60743e653098b9974d13de152ec9e8f3de29eca53c722a79af210abd5d'}

test = requests.get('http://10.0.75.1:5000/key', params=yourparams)
test.json()



#%%

import json
from pathlib import Path
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from bitcoinrpc.authproxy import AuthServiceProxy


priv = ('C:\\Users\\eduperez\\Desktop\\walletapi\\btcapi\\app\\common\\auth\\utils\\priv.pem')
pub = ('C:\\Users\\eduperez\\Desktop\\walletapi\\btcapi\\app\\common\\auth\\utils\\pub.pem')
enc = ('C:\\Users\\eduperez\\Desktop\\walletapi\\btcapi\\app\\common\\auth\\utils\\enc_cred')
class RsaResource(object):

    def __init__(self):
        with open(priv, 'rb') as file:
            self.privkey = RSA.importKey(file.read())

        with open(enc, 'rb') as file:
            self.enc_cred = file.readlines()[0]

        with open(pub, 'rb') as file:
            self.validpubkey = RSA.importKey(file.read())
        
        with open(pub, 'rb') as file:
            self.message = RSA.importKey(file.read())        

    def getCredentials(self, message):

        msg = hex(self.enc_cred.decode('utf-8'))
        print(msg)
        digest = SHA256.new()
        digest.update(message.encode('utf-8'))
        signer = PKCS1_v1_5.new(self.privkey)
        signed_message = signer.sign(digest).fromhex(msg)
        verifier = PKCS1_v1_5.new(self.validpubkey.publickey())
        verified = verifier.verify(digest, signed_message)
        if verified:
            dec_enc_msg = base64.b64decode(self.enc_cred)
            dec_dec_msg = self.privkey.decrypt(dec_enc_msg)
            return dec_dec_msg.decode('utf-8')

        else:
            return json.dumps({"error": "you have an eror"})


credentials = RsaResource().getCredentials("getcredentials")