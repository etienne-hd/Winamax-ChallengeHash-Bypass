import random
import hashlib
import base64

def convert_to_base64(string):
    bytes_string = string.encode('utf-8')
    base64_bytes = base64.b64encode(bytes_string)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def hash256(challenge):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(challenge.encode('utf-8'))
    return sha256_hash.hexdigest()

def S4():
    random_number = int((1 + random.random()) * 0x10000) & 0xFFFF
    hex_string = hex(random_number)[2:]
    return hex_string.zfill(4)

def guid():
    return S4() + S4() + S4() + S4() + S4() + S4() + S4() + S4()

challenge = guid()
challenge_hash = hash256(guid())
challenge_hash_base64 = convert_to_base64(challenge_hash)
print(challenge)
print(challenge_hash)
print(challenge_hash_base64) # This is the result (challenge_hash)
