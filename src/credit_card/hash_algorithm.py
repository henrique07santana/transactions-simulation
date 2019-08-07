import hashlib 

#h = hashlib.new('ripemd160')
h = hashlib.sha1()

def encrypt(string: str) -> str:
    h.update(str(string).encode("utf8")) 
    return h.hexdigest()

if __name__ == '__main__':
    print(encrypt('A'))