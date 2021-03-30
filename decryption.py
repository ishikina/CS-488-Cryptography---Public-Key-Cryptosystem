import sys

def main():
	decrypt(sys.argv[1], sys.argv[2], sys.argv[3])

#Decrypt function
def decrypt(ciphertext_file, plaintext_file, private_key_file):

	#Obtain private key	
	key_array = []
	with open(private_key_file, 'r') as key_file:
		for line in key_file:
			key_array.extend([int(item) for item in line.split()])	
	key_file.close()	
	
	#Obtain ciphertext	
	ciphertext = []
	with open(ciphertext_file, 'r') as text_file:
		ciphertext = text_file.read().splitlines()	
	text_file.close()	

	#Private key
	p = key_array[0]
	g = key_array[1]
	d = key_array[2]

	#Decrypt ciphertext by block
	plaintext = ""
	temp = ""	
	for i in ciphertext:
		c = i.split(' ', 1)
		temp = str(hex((pow(int(c[0]), p-1-d, p) * (int(c[1]) % p)) % p))
		temp_2 = bytes.fromhex(temp[2:10])
		plaintext += temp_2.decode("ASCII")	

	#Print plaintext to shell
	print("PLAINTEXT:")
	print(plaintext)

	#Print plaintext to external
	with open(plaintext_file, 'w') as dtext_file:
			dtext_file.write(plaintext)
	dtext_file.close()	


if (__name__ == '__main__'):
	main()
