from hashlib import sha1
from collections import Counter

def salted_sha1():
    file = "/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.sha1-salt.txt"
    hashes = [(line.rstrip('\n')).split("$")[3] for line in open(file)]
    print(len(hashes))
    hash_count = Counter(hashes)

    # common_passwords = ["123456", "12345", "123456789", "password", "iloveyou", "princess", "1234567", "rockyou",
    #                "12345678", "abc123", "nicole", "daniel", "babygirl", "monkey", "lovely", "jessica", "654321"
    #                "michael", "ashley", "qwerty", "111111", "iloveu", "000000", "michelle", "tigger"]

    common_passwords = ["123456", "12345", "123456789", "password", "iloveyou",
                        "princess", "1234567", "rockyou", "12345678", "abc123",
                        "nicole", "daniel", "babygirl", "monkey", "lovely",
                        "jessica", "654321", "michael", "ashley", "qwerty",
                        "111111", "iloveu", "000000", "michelle", "tigger"]

    write_file = open("salt-cracked.txt", "w")
    for p in common_passwords:
        encoded_pass = sha1(p.encode()).hexdigest()
        print(encoded_pass in hash_count)
        if (encoded_pass in hash_count):
            print("hello")
            write_file.write(str(hash_count[encoded_pass]) + "," + p + "\n")
    write_file.close()

if __name__ == "__main__":
    salted_sha1()
    #99996b911567c83cce17cdf194f314975c57ddf1
    #5ee22b34e4ea6b8f32dd9bdfc38ce1c73e37205d

