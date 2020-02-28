from hashlib import sha1
from collections import Counter

def salted_sha1():
    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.sha1-salt.txt"
    salted_hash = [line.rstrip('\n') for line in open(file)]
    salts = [(line.rstrip('\n')).split("$")[2] for line in salted_hash]
    hashes = [(line.rstrip('\n')).split("$")[3] for line in salted_hash]
    # TODO: all counters are 1???
    hash_count = Counter(hashes)

    common_passwords = ["123456", "12345", "123456789", "password", "iloveyou",
                        "princess", "1234567", "rockyou", "12345678", "abc123",
                        "nicole", "daniel", "babygirl", "monkey", "lovely",
                        "jessica", "654321", "michael", "ashley", "qwerty",
                        "111111", "iloveu", "000000", "michelle", "tigger"]

    # All possible pairs of salts and passwords
    salted_passwords = [[salt, pwd] for salt in salts for pwd in common_passwords]

    # write_file = open("salt-cracked.txt", "w")
    # for (s, p) in salted_passwords:
    #     encoded_pass = sha1((s + p).encode()).hexdigest()
    #     if (encoded_pass in hash_count):
    #         write_file.write(str(hash_count[encoded_pass]) + "," + p + "\n")
    # write_file.close()

    counts = {i:0 for i in common_passwords}
    write_file = open("salt-cracked.txt", "w")
    for (s, p) in salted_passwords:
        encoded_pass = sha1((s + p).encode()).hexdigest()
        if (encoded_pass in hash_count):
            counts[p] += 1
    for password in counts:
        write_file.write(str(counts[password]) + "," + password + "\n")
    write_file.close()


if __name__ == "__main__":
    salted_sha1()