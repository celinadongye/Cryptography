import string
from itertools import product
from hashlib import md5
from collections import Counter

def brute_force():
    # Generate 5-length passwords
    ascii_chars = string.ascii_lowercase + string.digits
    passwords = [''.join(i) for i in product(ascii_chars, repeat=5)]

    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.md5.txt"
    hashes = [line.rstrip('\n') for line in open(file)]
    pass_hash = Counter(hashes)

    write_file = open("md5-cracked.txt", "w")
    for p in passwords:
        encoded_pass = md5(p.encode()).hexdigest()
        if (encoded_pass in pass_hash):
            write_file.write(str(pass_hash[encoded_pass]) + "," + p + "\n")
    # print(pass_hash.__len__)
    
    write_file.close() 

if __name__ == "__main__":
    brute_force()
    
