import bcrypt

if __name__ == "__main__":
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw('secret'.encode(), salt)
    print(hashed.find(salt))
    print(hashed == bcrypt.hashpw('secret'.encode(), hashed))