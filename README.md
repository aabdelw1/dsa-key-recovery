## Digital Signature Algorithm (DSA) Key-Recovery from Nonce

Let’s recall DSA signature.

- There are public parameters (p, q, g), wherepandqare large primes; p−1 is a multiple of q
    and g is a group generator. Also, H(·) is a cryptographic hash function.
- Key generationKeyGen generates secret keyx

```
←Z∗q, and public keyy ← gxmodp, and
outputs (x, y).
```
- SigningSign(m):
    - generate a random noncek 

''' 
k ← Z_q^*. 
'''
''' 
r ← g^k mod p 
'''
''' 
s ← (k^-1 (H(m) +xr)) mod q. 
'''
''' 
output pair (r, s) 
'''

What is the vulnerability?
It is possible that the range over which the random noncekis selected is very small. If an
attacker wants to retrieve the private key from the given signature (r, s) and the messagem, he
can exploit the fact that noncekis generated over a small range.

How does the attack work?
The attacker has access to the messagemand (r, s) pair. He can first try to recover kby
brute-force the range ofk(assuming it is small). Then withkto recover the secrete keyxfroms.

## Task

Assume instead of using the large set Z∗q, random noncekis selected randomly from a small set
{ 1 , 2 ,... , 216 − 1 }. You are provided with aninput.jsonfile containing:

- Public parameters: (p, q, g), where|q|= 160,|p|= 1024; for simplicity we instantiateH(·)
    with SHA-1.
- Public keyy:=gxmodp
- Messagemand its signature pair (r, s) signed withxandk
- Hashh= SHA-1(m) in hexadecimal representation
You are expected to computek and produce the private keyx that was used to sign the
messagem. There is no restriction on the language nor external cryptographic library (e.g., Crypto,
OpenSSL) used for your attack. Note that we run key generation algorithm independently for each
student.


## References

```
[1] https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
```
```
[2] NIST.FIPS.186-4 (latest)https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.
pdf
```
