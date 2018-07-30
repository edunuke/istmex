import json
from pathlib import Path
import falcon
from Crypto.PublicKey import RSA
import base64
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5


class CredentialResource(object):

    def __init__(self):
        with open(Path.cwd()
                      .joinpath('utils')
                      .joinpath('priv')
                      .with_suffix('.pem'), 'rb') as file:
            self.privkey = RSA.importKey(file.read())

        with open(Path.cwd()
                      .joinpath('utils')
                      .joinpath('enc_cred'), 'rb') as file:
            self.enc_cred = file.readlines()[0]

        with open(Path.cwd()
                      .joinpath('utils')
                      .joinpath('pub')
                      .with_suffix('.pem'), 'rb') as file:
            self.validpubkey = RSA.importKey(file.read())

    def on_get(self, req, resp):
        msg = req.get_param('key')
        digest = SHA256.new()
        password = "getcredentials"
        digest.update(password.encode('utf-8'))
        signer = PKCS1_v1_5.new(self.privkey) 
        signed_message = signer.sign(digest).fromhex(msg)
        verifier = PKCS1_v1_5.new(self.validpubkey.publickey())
        verified = verifier.verify(digest, signed_message)
        if verified:
            dec_enc_msg = base64.b64decode(self.enc_cred)
            dec_dec_msg = self.privkey.decrypt(dec_enc_msg)
            resp.body = json.dumps(dec_dec_msg.decode('utf-8'))
            resp.status = falcon.HTTP_200
        else:
            resp.body = json.dumps({"status": "error"})
            resp.status = falcon.HTTP_404


app = falcon.API()
app.add_route('/validate', CredentialResource())
