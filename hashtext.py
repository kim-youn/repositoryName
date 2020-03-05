
#hashing in Python

import hashlib

print(hashlib.sha256("hello world".encode('utf-8')).hexdigest())

print(hashlib.sha512("hello world".encode('utf-8')).hexdigest())
