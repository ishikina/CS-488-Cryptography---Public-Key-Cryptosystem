import sys

from key_generation import create_keys
from encryption import encrypt
from decryption import decrypt

def main():
	
	#Generate public and private keys
	#First arg is the seed, second arg is the output public key file, third arg is the output private key file	
	#eg. "python3 main.py -k 2 pubkey.txt prikey.txt"
	if sys.argv[1] == "-k":
		print("--- GENERATING PUBLIC AND PRIVATE KEYS ---")	
		create_keys(sys.argv[2], sys.argv[3], sys.argv[4])
	
	#Encrypt plaintext
	#First arg is the input(plaintext) file, second arg is the output(ciphertext) file, third arg is the public key file
	#eg. "python3 main.py -e ptext.txt ctext.txt pubkey.txt"	
	if sys.argv[1] == "-e":
		print("--- ENCRYPTING:", sys.argv[2], "---")
		
		encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
	
	#Decrypt ciphertext
	#First arg is the input(ciphertext) file, second arg is the output(plaintext) file, third arg is the private key file
	#eg. "python3 main.py -d ctext.txt dtext.txt prikey.txt"	
	if sys.argv[1] == "-d":
		print("--- DECRYPTING:", sys.argv[2], "---")	
		decrypt(sys.argv[2], sys.argv[3], sys.argv[4])

if (__name__ == '__main__'):
	main()
