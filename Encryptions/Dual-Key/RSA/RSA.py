import random
from sympy import isprime
import math

class Keys_storing:
    def __init__(self, private = [], public = []) -> None:
        self.private = private
        self.public = public
        
class rsa_keygenerator:
    def __init__(self) -> None:
        self.p = None    # Done
        self.q = None    # Done
        self.e = None    # Done
        self.n = None    # Done
        self.phyn = None # Done
        self.d = None    # Done
        self.Keys = None # Done

    def generate_large_prime(self, bits):
        while True:
            potential_prime = random.getrandbits(bits)
            # adding a one at the end of the bits to make sure it is odd as all primes are odd
            potential_prime |= 1
            if isprime(potential_prime):
                return potential_prime

    def generate_large_primes(self, num_bits, num_primes):
        primes = []
        while len(primes) < num_primes:
            prime_candidate = self.generate_large_prime(num_bits)
            if prime_candidate not in primes:
                primes.append(prime_candidate)
        return primes
    
    def calculate_n(self):
        self.n = self.p * self.q
        return self.n
    
    def phy(self):
        self.phyn = (self.p - 1) * (self.q - 1)
        return self.phyn
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def e_picker(self):
        '''
        Select an integer e such that 1<e<ϕ(n) and e is coprime with ϕ(n) (i.e., e and ϕ(n) share no factors other than 1).
        '''
        self.e = 65537  # Commonly used value for 'e'
        while True:
            self.e = random.randint(3, self.phyn - 1)
            if self.gcd(self.e, self.phyn) == 1:
                break
        return self.e

    def mod_inverse(self, a, m):
        """
        Calculate the modular inverse of 'a' modulo 'm' using the Extended Euclidean Algorithm.
        """
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if a != 1:
            return None  # Modular inverse does not exist
        if x1 < 0:
            x1 += m0
        return x1

    def d_picker(self):
        """
        Calculate the decryption exponent 'd' using the Extended Euclidean Algorithm.
        """
        self.d = self.mod_inverse(self.e, self.phyn)
        return self.d

    
    def key_generation(self, bits):
        self.p, self.q = self.generate_large_primes(bits, 2)
        self.calculate_n()
        self.phy()
        self.e_picker()
        self.d_picker()
        self.Keys = Keys_storing([self.e, self.n], [self.d, self.n])
        return self.Keys

class rsa_enc_and_dec:
    def __init__(self, sender:Keys_storing, receiver:Keys_storing) -> None:
        self.me = sender
        self.other = receiver

    def custom_pow(self, base, exponent, modulus):
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
        return result

    def encrypt(self, plaintext = ""):
        """
        (Send) Encrypt the plaintext message using the public key (e, n).
        """
        # Convert plaintext to numeric representation
        numeric_representation = int.from_bytes(plaintext.encode(), byteorder='big')
        # Encryption
        ciphertext = self.custom_pow(numeric_representation, self.other.public[0], self.other.public[1])
        return ciphertext
    
    def decrypt(self, ciphertext):
        """
        (Receive) Decrypt the ciphertext using the private key (d, n).
        """
        # decryption
        decrypted_numeric = self.custom_pow(ciphertext, self.me.private[0], self.me.private[1])

        # Convert numeric representation back to plaintext
        plaintext = decrypted_numeric.to_bytes((decrypted_numeric.bit_length()+7) // 8, byteorder='big').decode()
        return plaintext


#example usage
if __name__ == "__main__":
    keys_gen = rsa_keygenerator()

    Bob = keys_gen.key_generation(1024)
    Alice = keys_gen.key_generation(1024)

    Bob_app = rsa_enc_and_dec(Bob, Alice)
    Alice_app = rsa_enc_and_dec(Alice, Bob)

    # Bob will send a message to Alice
    c = Bob_app.encrypt("Hello Alice, I am Bob.")
    p = Alice_app.decrypt(c)
    print(f"Encrypted Message (Bob to Alice):\n{c}\nDecrypted Message (Alice received):\n{p}")

    # Alice will send a message to Bob
    c = Alice_app.encrypt("Hello Bob, How are you?")
    p = Bob_app.decrypt(c)
    print(f"Encrypted Message (Alice to Bob):\n{c}\nDecrypted Message (Bob received):\n{p}")


    # Bob will send a message to Alice
    c = Bob_app.encrypt("I am fine. hbu?")
    p = Alice_app.decrypt(c)
    print(f"Encrypted Message (Bob to Alice):\n{c}\nDecrypted Message (Alice received):\n{p}")

    # Alice will send a message to Bob
    c = Alice_app.encrypt("am okay. but I am stuck in the Grad project")
    p = Bob_app.decrypt(c)
    print(f"Encrypted Message (Alice to Bob):\n{c}\nDecrypted Message (Bob received):\n{p}")


    # Bob will send a message to Alice
    c = Bob_app.encrypt("I know, me too. I hope every thing goes fine.")
    p = Alice_app.decrypt(c)
    print(f"Encrypted Message (Bob to Alice):\n{c}\nDecrypted Message (Alice received):\n{p}")

    # Alice will send a message to Bob
    c = Alice_app.encrypt("yeah me too :(")
    p = Bob_app.decrypt(c)
    print(f"Encrypted Message (Alice to Bob):\n{c}\nDecrypted Message (Bob received):\n{p}")
