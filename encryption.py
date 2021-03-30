import sys
import random

def main():
	encrypt(sys.argv[1], sys.argv[2], sys.argv[3])

#Encrypt function
def encrypt(plaintext_file, ciphertext_file, public_key_file):
	
	#Obtain public key	
	key_array = []
	with open(public_key_file, 'r') as key_file:
		for line in key_file:
			key_array.extend([int(item) for item in line.split()])
	key_file.close()	

	#Obtain plaintext	
	with open(plaintext_file, 'r') as ptext_file:
		plaintext = ptext_file.read()
	ptext_file.close()	
	plaintext = plaintext[0:len(plaintext) - 1]

	#Divide plaintext into blocks	
	blocks = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]

	#Convert characters to hex blocks
	hex_blocks = []	
	counter = 0
	temp_2 = ""
	temp = ""
	for i in blocks:
		for j in i:
			counter = counter + 1	
			temp = (str(hex(ord(j))))
			temp_2 += temp[2:4]
			if counter == 4:
				hex_blocks.append(temp_2)
				temp_2 = ""	
				counter = 0

	#Padding	
	if len(temp_2) == 2:
		temp_2 += "000000"
		hex_blocks.append(temp_2)
	if len(temp_2) == 4:
		temp_2 += "0000"
		hex_blocks.append(temp_2)
	if len(temp_2) == 6:
		temp_2 += "00"
		hex_blocks.append(temp_2)

	#Convert hex to decimal
	dec_blocks = []	
	for i in hex_blocks:
		dec_blocks.append(int(i, 16))

	#Public key
	p = key_array[0]	
	g = key_array[1]
	e2 = key_array[2]

	#Encrypt plaintext by block
	ciphertext = []
	for i in dec_blocks:
		k = random.randint(0, p - 1)
		ciphertext.append(str(pow(g, k, p)) + " " + str((pow(e2, k, p) * i) % p))

	#Print ciphertext in shell
	print("CIPHERTEXT")
	print("C1         C2")	
	for i in ciphertext:
		print(i)

	#Print ciphertext to external	
	with open(ciphertext_file, 'w') as ctext_file:
		for i in ciphertext:
			ctext_file.write(i)
			ctext_file.write('\n')
	ctext_file.close()	

if (__name__ == '__main__'):
	main()
