import os
import uuid
import hashlib
import string  # for string ops such as delete the unnecessary content


def make_random_password(length=12, symbols='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$^_+&'):
    password = []
    for i in map(lambda x: int(len(symbols) * x / 255.0), os.urandom(length)):
        password.append(symbols[i])
    return ''.join(password)


uuid3_dns = uuid.uuid3(uuid.NAMESPACE_DNS, 'zjrmyy' + make_random_password())
uuid3_url = uuid.uuid3(uuid.NAMESPACE_URL, 'zjrmyy' + make_random_password())


i = 'Hello, how are you!'
i.translate(str.maketrans('', '', string.punctuation))

print(str(uuid3_dns))
print(str(uuid3_url))
print(i)