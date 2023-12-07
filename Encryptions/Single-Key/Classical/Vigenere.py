import Coding
import numpy as np

class vigenere(Coding.coding):
    def __init__(self, Key):
        '''
        This class applies Vigenère Encryption and Decryption, You Need To Send The KEY
        '''
        self.set_key(Key)
    
    def encrypt(self, plain_text):
        '''
        This function apply the Vigenère encryption on a plain text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        encryption = ""
        temp = []
        dic_i = 0
        for i in txt:
            if dic_i >= len(self.dic):
                dic_i = 0
            for j in range(0, len(self.alphabet)):
                if self.alphabet[j] == i:
                    temp.append((j + self.dic[dic_i]) if (j + self.dic[dic_i]) < 26 else (j + self.dic[dic_i] - len(self.alphabet)))
                    break
            dic_i += 1
        for i in range(0, len(temp)):
            for j in range(0, len(self.alphabet)):
                if temp[i] == j:
                    encryption += self.alphabet[j]
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the Vigenère decryption on an Encrypted text.
        '''
        txt = self.splitter(encrypted_text)
        decryption = ""
        temp = []
        dic_i = 0
        for i in txt:
            if dic_i >= len(self.dic):
                dic_i = 0
            for j in range(0, len(self.alphabet)):
                if self.alphabet[j] == i:
                    temp.append((j - self.dic[dic_i]) if (j - self.dic[dic_i]) >= 0  else (j - self.dic[dic_i] + len(self.alphabet)))
                    break
            dic_i += 1
        for i in range(0, len(temp)):
            for j in range(0, len(self.alphabet)):
                if temp[i] == j:
                    decryption += self.alphabet[j]
        return decryption


    def set_key(self, key):
        key = str(key)
        self.key = self.splitter(key)
        self.dic = []
        for i in self.key:
            for j in range(0, len(self.alphabet)):
                if self.alphabet[j] == i:
                    self.dic.append(j)

if __name__ == "__main__":
    cypher = vigenere("MaTH")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))
    print(cypher.encrypt("Make it happen."))
    print(cypher.decrypt(cypher.encrypt("Make it happen.")))

    cypher = vigenere("deceptivedeceptivedeceptive")
    print(cypher.dic)
    print(cypher.encrypt("wearediscoveredsaveyourself"))
    print(cypher.decrypt(cypher.encrypt("wearediscoveredsaveyourself")))