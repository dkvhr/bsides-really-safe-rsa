from Crypto.Util.number import getPrime, isPrime
from private import p, q

# p é um Sophie Germain prime
# q é o safe prime number associado

e = 65537
assert isPrime(p), isPrime(q)
n = p*q
n_file = open("n_value.py", "w")
n_file.write(f"n = {str(n)}")
n_file.close()
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
