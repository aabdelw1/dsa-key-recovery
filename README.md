## Digital Signature Algorithm (DSA) Key-Recovery from Nonce

Let’s recall DSA signature.

- There are public parameters (p, q, g), where p and q are large primes; p−1 is a multiple of q
    and g is a group generator. Also, H(·) is a cryptographic hash function.
- Key generationKeyGen generates secret key x

```
←Z∗q, and public key y ← gx mod p, and
outputs (x, y).
```
- SigningSign(m):
    - generate a random nonce k 

``` 
k ← Z_q^*. 
```
``` 
r ← g^k mod p 
```
``` 
s ← (k^-1 (H(m) +xr)) mod q. 
```
``` 
output pair (r, s) 
```

What is the vulnerability?
It is possible that the range over which the random nonce k is selected is very small. If an
attacker wants to retrieve the private key from the given signature (r, s) and the messagem, he
can exploit the fact that noncekis generated over a small range.

How does the attack work?
The attacker has access to the messagemand (r, s) pair. He can first try to recover kby
brute-force the range ofk(assuming it is small). Then with k to recover the secret key x from s.

## Task

Assume instead of using the large set Z∗q, random nonce k is selected randomly from a small set
{ 1 , 2 ,... , 216 − 1 }. You are provided with an input.json file containing:

- Public parameters: (p, q, g), where|q|= 160,|p|= 1024; for simplicity we instantiate H(·)
    with SHA-1.
- Public key y: = gx mod p
- Message m and its signature pair (r, s) signed with x and k
- Hashh= SHA-1(m) in hexadecimal representation


This algorithm computes k and produces the private key x that was used to sign the
message m. 


## References

```
[1] https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
```
```
[2] NIST.FIPS.186-4 (latest)https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.
pdf
```
