#!/usr/bin/env python
import bcrypt
from collections import Counter

def crack_bcrypt():
    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.bcrypt.txt"
    hashes = [line.rstrip('\n') for line in open(file)]
    # print(hashes)

    password = "123456"

    # salt = bcrypt.gensalt()
    # hashed = bcrypt.hashpw('secret'.encode(), salt)
    # print(hashed.find(salt))
    
    # print(hashed == bcrypt.hashpw('secret'.encode(), hashed))

    # encoded_pass = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    write_file = open("bcrypt-lines.txt", "w")
    for idx,h in enumerate(hashes):
        encoded_pass = bcrypt.hashpw(password.encode(), h)
        if h == encoded_pass:
            print("hello")
            write_file.write((idx+1) + "\n")
    write_file.close()

if __name__ == "__main__":
    crack_bcrypt()
    #$2b$12$NC7sY22M87uYqIxfcpkpfue/JXmlg4AgkZuhdkupaL2KixENhAUl2