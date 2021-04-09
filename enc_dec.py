#Encryption And Decryption Algorithm
import hashlib
import os

#Add Salt
def deriveKey(passphrase: str, salt: bytes = None) -> [str, bytes]:
    if salt is None:
        salt = os.urandom(8)
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf8"), salt, 100000), salt
