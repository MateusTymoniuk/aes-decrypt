## Encrypt / Decrypt files in python

This project was made as a simple example of how to encrypt a file with python's cryptography library, using the Fernet symmetric encryption.

In this example, the file which would be encrypted is nba.csv.

To start the encryption process, either just run ```python encrypt.py``` so that the code generates a valid encryption key and saves it to a file so it can be used for decrypting, or you can pass a valid key. Check out the [documentation](https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption) for more information on how to handle the key and how the algorithm works.