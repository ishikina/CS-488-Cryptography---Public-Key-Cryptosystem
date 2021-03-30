# CS 488: Cryptography - Public Key Cryptosystem

### Files

* main.py - main(), generates keys, encrypts, or decrypts depending on arguments

* key_generation.py - File to generate public and private keys

* encryption.py - File to encrypt the plaintext

* decryption.py - File to decrypt the ciphertext

### Description

This program is an asymetric key system in which the public and private keys are generated using an algorithm developed by Menzes from the "Handbook of Applied Cryptography." 

> RFC 4419 SSH DH Group Exchange March 2006
> 
> Appendix A: Generation of Safe Primes
> 
> The "Handbook of Applied Cryptography" [MENZES] lists the following algorithm to generate a k-bit safe prime p. It has been modified so that 2 is a generator for the multiplicative group mod p.
> 
>   1. Do the following:
>
>     1. Select a random (k-1)-bit prime q (Rabin-Miller), so that q mod 12 = 5.
>
>     2. Compute p = 2q + 1, and test whether p is prime (using, the Rabin-Miller test).
>
>   2. Repeat until p is prime.

Both key pair sets are composed of three components: the shared large 32 bit prime number, the generator value (this program uses 2 as the generator), and the encryption/decyrption component. 

Messages are encrypted using power modulus operations. The ciphertext consists of an initialization block is created using a randomly generated number and then followed by the message block, both of which are power modulated with the public prime number.

**C<sub>1</sub> = g<sup>k</sup> mod p**
**C<sub>2</sub> = e2<sup>k</sub> ∙ m mod p**

The ciphertext is decrypted by taking the inverse of the exponentiated initialized block and the message block, then power modulated with the public prime component to get the plaintext.

**(C1<sub>d</sub>)<sup>-1</sup>C<sub>2</sub> mod p = m**

## Running the code

To generate keys: 

*first arg is the seed, second arg is output file for public key, third arg is output file for private key*
```
python3 main.py -k 2 pubkey.txt prikey.tx
```

To encrypt:

*first arg is input file for plaintext, second arg is output file for ciphertext, third arg is to obtain public key*
```
python3 main.py -e ptext.txt ctext.txt pubkey.txt
```

To decrypt:

*first arg is input file for ciphertext, second arg is output file for plaintext, third arg is to obtain private key*
```
python3 main.py -d ctext.txt dtext.txt prikey.txt
```

## References

[Miller-Rabin function](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)

[Test plaintext](https://en.wikipedia.org/wiki/Zino%27s_petrel)
