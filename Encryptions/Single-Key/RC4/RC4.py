import numpy as np
import copy
import secrets
class RC4:
    def __init__(self, key: str, key_num_digits: int) -> None:
        """
        Initialize the RC4 class.

        Args:
            key (str): The key to use for encryption/decryption.
            key_num_digits (int): The size of the key, in bits.
        """
        self.key = key
        self.key_num_digits = key_num_digits
        self.set_key()
        
    def set_key(self):
        """
        Initialize the s and t arrays used in the RC4 algorithm.

        The s array is used to store the state of the RC4 algorithm, while the t array is used to
        generate the keystream. The key is used to generate the s and t arrays by computing a
        series of modulo operations and bit shifts.

        The key is converted to an integer and then divided into individual digits. These digits are
        used to populate the t array. The s array is initialized with a range of integers from 0 to
        the key bit size, minus 1.

        The t array is used to generate the keystream by performing a series of modulo and bit shift
        operations on each element of the s array. The s and t arrays are then swapped to ensure that
        the keystream is generated in reverse order.

        Args:
            self (RC4): The RC4 object.
        """
        self.s = np.arange(self.key_num_digits, dtype=np.uint8)
        self.t = np.zeros(self.key_num_digits)
        self.key = int(self.key)
        
        j = 0
        key_len = len(str(self.key))
        for i in range(0, self.t.__len__()):
            key_mod = 10**(key_len - j)
            self.t[i] = ((self.key%(key_mod))) // (key_mod // 10)
            if j >= key_len - 1:
                j = -1
            j+=1

        j = 0
        for i in range(self.t.__len__()):
            j = int((j + self.s[i] + self.t[i]) % self.key_num_digits)
            self.s[i], self.s[j] = self.s[j], self.s[i]

    def encrypt_and_decrypt(self, plaintext = ""):
        """
        Encrypts and decrypts the given plaintext using the RC4 algorithm.

        Args:
            plaintext (str, optional): The plaintext to encrypt/decrypt. Defaults to "".

        Returns:
            str: The encrypted/decrypted plaintext.
        """
        j = 0
        k = ""
        ciphertext = ""
        s = copy.copy(self.s)

        for i in range(len(plaintext)):
            i =  (i + 1) % self.key_num_digits
            j = (j + s[i]) % self.key_num_digits
            s[i], s[j] = s[j], s[i]
            t = (s[i] + s[j]) % self.key_num_digits
            k += str(s[t])
        keystream = np.array(list(k), dtype=int)
        # XORing the plaintext with the keystream to get ciphertext
        for i in range(len(plaintext)):
            ciphertext += chr(ord(plaintext[i]) ^ keystream[i])
        return ciphertext

    def generate_key(key_num_digits):
        """
        Generates a key with a specific number of decimal digits.

        Args:
            key_num_digits (int): The number of decimal digits in the key.

        Returns:
            int: The generated key.
        """
        # Generate a random number with the specified number of digits
        min_value = 10 ** (key_num_digits - 1)
        max_value = (10 ** key_num_digits) - 1
        return secrets.randbelow(max_value - min_value) + min_value  


if __name__ == "__main__":
    key = RC4.generate_key(256)
    #print(key)
    cipher = RC4(key, 256)
    
    c = cipher.encrypt_and_decrypt("cypher: Hello, world! I am a cypher")
    p = cipher.encrypt_and_decrypt(c)
    #print(c)
    print(p)


    key = RC4.generate_key(40)
    #print(key)
    cipher = RC4(key, 40)
    
    c = cipher.encrypt_and_decrypt("World: Hello, Nice to meet you! What type of cyphers are you?")
    p = cipher.encrypt_and_decrypt(c)
    #print(c)
    print(p)


    key = RC4.generate_key(700)
    #print(key)
    cipher = RC4(key, 700)
    
    c = cipher.encrypt_and_decrypt("cypher: Nice to meet you too, I am a RC4 cypher")
    p = cipher.encrypt_and_decrypt(c)
    #print(c)
    print(p)
    
    key = RC4.generate_key(200)
    #print(key)
    cipher = RC4(key, 200)
    c = cipher.encrypt_and_decrypt("World: Wow you are increadable")
    p = cipher.encrypt_and_decrypt(c)
    #print(c)
    print(p)
