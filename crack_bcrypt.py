#!/usr/bin/env python
from bcrypt import hashpw
import bcrypt
from collections import Counter

def crack_bcrypt():
    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.bcrypt.txt"
    # salted_hashes = [line.rstrip('\n') for line in open(file)]
    # salts = [(line.rstrip('\n')).split("$")[2] for line in salted_hashes]
    salted_hashes = [(line.rstrip('\n')).split("$")[3] for line in open(file)]
    salts = [line[:22].encode() for line in salted_hashes]
    hashes = [line[22:] for line in salted_hashes]

    password = u"123456"

    counter = 0
    write_file = open("bcrypt-lines.txt", "w")
    for idx,h in enumerate(hashes):
        if counter <= 5:
            encoded_pass = bcrypt.hashpw(password.encode(), h)
            if encoded_pass == h:
            # if bcrypt.checkpw(password.encode('utf-8'), h):
                counter += 1
                write_file.write((idx+1) + "\n")
        else:
            break
    write_file.close()

    # write_file = open("bcrypt-lines.txt", "w")
    # for idx,h in enumerate(hashes):
    #     encoded_pass = bcrypt.hashpw(password.encode(), h)
    #     if h == encoded_pass:
    #         print("hello")
    #         write_file.write((idx+1) + "\n")
    # write_file.close()

if __name__ == "__main__":
    crack_bcrypt()
    # 2b - bcrypt algorithm version
    # 12 - cost factor, 2^12 iterations of the key derivation function
    # 16 bytes (22 chars) - salt
    # 31 chars - ciphertext (password) for authentication

    #$2b$12$DpvRvjJs4pAj4LMNyFklm.Qv2hcKQgOzwAVJbfkg//mBvEXqde1mq
    #$2b$12$kzBFIef2qY7IIQE0t2UByucY8SjlI3mK lBPrpOqflykxoOpZ6sHeW