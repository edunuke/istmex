# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:07:09 2018

@author: eduperez
"""
#%%
from pathlib import Path
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


with open(Path.cwd()
              .joinpath('Desktop')
              .joinpath('walletapi')
              .joinpath('btcvalidator')
              .joinpath('app')
              .joinpath('utils')
              .joinpath('pub').with_suffix('.pem'),'rb') as file:
    pub_key = RSA.importKey(file.read())
# Read shared key from file
with open(Path.cwd()
              .joinpath('Desktop')
              .joinpath('walletapi')
              .joinpath('btcvalidator')
              .joinpath('app')
              .joinpath('utils')
              .joinpath('priv').with_suffix('.pem'),'rb') as file:
    private_key = RSA.importKey(file.read())
    
#%%
message = "getcredentials"
digest = SHA256.new()
digest.update(message.encode('utf-8'))
#%%
# Load private key and sign message
signer = PKCS1_v1_5.new(private_key)
signed_message = signer.sign(digest)
#%%


# Load public key and verify message
verifier = PKCS1_v1_5.new(pub_key.publickey())
verified = verifier.verify(digest, signed_message)


#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pubmessage.txt', 'w') as file:
    file.write(signed_message.hex())

#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\btcapi\\app\\pubmessage.txt', 'r') as file:
    a = file.readlines()[0]
#%%

#%%
import psycopg2

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='mysecretpassword'")
print(conn)
conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

#%%

from sqlalchemy import create_engine

db_string = "postgresql://postgres:test@localhost/postgres"

db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")


result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)




