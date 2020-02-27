import string
from itertools import product
from hashlib import md5
from collections import Counter

def brute_force():
    # Generate 5-length passwords
    ascii_chars = string.ascii_lowercase + string.digits
    passwords = [''.join(i) for i in product(ascii_chars, repeat=5)]

    # Multiset of password hashes in the text file
    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.md5.txt"
    hashes = [line.rstrip('\n') for line in open(file)]
    hash_count = Counter(hashes)

    # Check if our generated passwords match any password hashes in the file
    write_file = open("md5-cracked.txt", "w")
    for p in passwords:
        encoded_pass = md5(p.encode()).hexdigest()
        if (encoded_pass in hash_count):
            write_file.write(str(hash_count[encoded_pass]) + "," + p + "\n")
    write_file.close() 

if __name__ == "__main__":
    brute_force()
    
