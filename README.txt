Isaiah Shikina
ishikina@pdx.edu
Program 2
CS 485
3/16/21

--Files--
main.py - File for main(), generates keys, encrypts, or decrypts depending on arguments
key_generation.py - File to generate public and private keys
encryption.py - File to encrypt the plaintext
decryption.py - File to decrypt the ciphertext

--Description--
This program encrypts and decrypts using an asymetric key system. Public and private keys are
generated using a MENEZES algorithm. To generate keys, use the '-k' flag. Both sets are composed 
of three components and share a large 32 bit prime number and a generator value (this program uses
2 as the generator). The third component is used to encrypt/decrypt. The plaintext is encrypted by 
32 bit blocks using the public key. To encrypt, use the '-e' flag. The ciphertext is decrypted 
by block using the private key. To decrypt, use the '-d' flag.

--Running the code--
To generate keys: 

(first arg is the seed, second arg is output file for public key, third arg is output file for private key)
python3 main.py -k 2 pubkey.txt prikey.txt

To encrypt:

(first arg is input file for plaintext, second arg is output file for ciphertext, third arg is to obtain public key)
python3 main.py -e ptext.txt ctext.txt pubkey.txt

To decrypt:

(first arg is input file for ciphertext, second arg is output file for plaintext, third arg is to obtain private key)
python3 main.py -d ctext.txt dtext.txt prikey.txt

--References--
Miller-Rabin: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

Example plaintext: https://en.wikipedia.org/wiki/Zino%27s_petrel
