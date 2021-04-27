## Digital Signature Algorithm (DSA) Key-Recovery from Nonce

Let’s recall DSA signature.

- There are public parameters (p, q, g), wherepandqare large primes;p−1 is a multiple ofq
    andgis a group generator. Also,H(·) is a cryptographic hash function.
- Key generationKeyGen generates secret keyx

```
$
←Z∗q, and public keyy ← gxmodp, and
outputs (x, y).
```
- SigningSign(m):
    - generate a random noncek
       $
←Z∗q.
    - r←

### (

```
gkmodp
```
### )

```
modq.
```
- s←(k−^1 (H(m) +xr)) modq.
- output pair (r, s).

What is the vulnerability?
It is possible that the range over which the random noncekis selected is very small. If an
attacker wants to retrieve the private key from the given signature (r, s) and the messagem, he
can exploit the fact that noncekis generated over a small range.

How does the attack work?
The attacker has access to the messagemand (r, s) pair. He can first try to recover kby
brute-force the range ofk(assuming it is small). Then withkto recover the secrete keyxfroms.

## Task

Assume instead of using the large setZ∗q, random noncekis selected randomly from a small set
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

### 1


### 2

## Collaboration & Resources

No collaboration is allowed for this homework. You are allowed to look at the examples of how to
use the API of the language and cryptographic libraries and json parsing on the internet.

## Submission

Please submit followingthreefiles (separately,notin a zip file),

- A textfilereport.txt:
    (First line)[k]
    (Second line)[x]

```
Note: replace[k]and[x]with your input. Here is an example:
```
```
29238
59732880924362433946044405794379157682704500384
```
- Your implementation source file:source.[*].
    Note: replace[*]with your file extension, e.g.,c,py.
- A textfileREADME.txt:
    List any external cryptographic library or json parsing library used in your source file.

## Penalties

- For file names with wrong formatting, we will deduct 2 points each.
- For wrong formatting ofreport.txt, we will deduct 5 points.

## References

```
[1] https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
```
```
[2] NIST.FIPS.186-4 (latest)https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.
pdf
```
