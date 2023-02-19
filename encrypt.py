# import required module
from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# if key is empty, generate new one
if key == b'':
	# key generation
	key = Fernet.generate_key()

	# store the generated key in a file
	with open('filekey.key', 'wb') as filekey:
 	   filekey.write(key)

# using the key
fernet = Fernet(key)

# opening the original file to encrypt
with open('nba.csv', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('nba.csv', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
