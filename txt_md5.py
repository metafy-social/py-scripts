import hashlib
mystring = input('Enter string to hash: ')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())