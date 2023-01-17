
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# opening the key
with open('filekey-aes.key', 'rb') as filekey:
    key = filekey.read()

with open('aes.iv', 'rb') as fileiv:
	iv = fileiv.read()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()

# opening the original file to encrypt
with open('nba-aes.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

ct = decryptor.update(encrypted)

# opening the file in write mode and
# writing the encrypted data
with open('nba-aes.csv', 'wb') as encrypted_file:
	encrypted_file.write(ct)

# # decryptor = cipher.decryptor()
# # decryptor.update(ct) + decryptor.finalize()
# # b'a secret message'