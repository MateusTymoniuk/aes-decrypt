
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# opening the key
# with open('filekey.key', 'rb') as filekey:
#     key = filekey.read()

key = os.urandom(32)
iv = os.urandom(16)

# string the key in a file
with open('filekey-aes.key', 'wb') as filekey:
    filekey.write(key)

# string the iv in a file
with open('aes.iv', 'wb') as fileiv:
    fileiv.write(iv)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()

# opening the original file to encrypt
with open('nba.csv', 'rb') as file:
	original = file.read()

ct = encryptor.update(original)

# opening the file in write mode and
# writing the encrypted data
with open('nba-aes.csv', 'wb') as encrypted_file:
	encrypted_file.write(ct)

# # decryptor = cipher.decryptor()
# # decryptor.update(ct) + decryptor.finalize()
# # b'a secret message'