"""
INSTALLING REQUIRED PACKAGES
Run the following two commands to install all required packages.
python -m pip install --upgrade pip
python -m pip install --upgrade bcrypt argon2-cffi passlib cryptography
"""

from cryptography.fernet import Fernet
from passlib.hash import argon2
from passlib.hash import bcrypt_sha256

# run a few simple tests in a main function
def main():
    password = "Melorine"
    hasher = DropboxHasher("string")
    hash = hasher.hash(hasher, password)
    print(hash)

class DropboxHasher:
    def __init__(self, pepper_key):
        self.pepper = Fernet(pepper_key)

    def hash(self, pwd):
        # hash with sha256 then run 12 rounds of bcrypt
        # a random salt is generated per-password automatically
        hash = bcrypt_sha256.using(rounds=12).hash(pwd)
        # convert this unicode hash string into bytes before encryption
        hashb = hash.encode('utf-8')
        # encrypt this hash using the global pepper
        pep_hash = self.pepper.encrypt(hashb)
        return pep_hash

    def check(self, pwd, pep_hash):
        # decrypt the hash using the global pepper
        hashb = self.pepper.decrypt(pep_hash)
        # convert this hash back into a unicode string
        hash = hashb.decode('utf-8')
        # check if the given password matches this hash
        return bcrypt_sha256.verify(pwd, hash)

    @staticmethod
    def random_pepper():
        return Fernet.generate_key()

class UpdatedHasher:
    def __init__(self, pepper_key):
        self.pepper = Fernet(pepper_key)

    def hash(self, pwd):
        # hash with argon2
        hash = argon2.using(rounds=10).hash(pwd)
        # convert this unicode hash string into bytes before encryption
        hashb = hash.encode('utf-8')
        # encrypt this hash using the global pepper
        pep_hash = self.pepper.encrypt(hashb)
        return pep_hash

    def check(self, pwd, pep_hash):
        # decrypt the hash using the global pepper
        hashb = self.pepper.decrypt(pep_hash)
        # convert this hash back into a unicode string
        hash = hashb.decode('utf-8')
        # check if the given password matches this hash
        return argon2.verify(pwd, hash)

    @staticmethod
    def random_pepper():
        return Fernet.generate_key()

# run main after definitions when run directly as a script
if __name__=='__main__': main()