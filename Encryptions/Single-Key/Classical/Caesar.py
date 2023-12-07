import Coding
import numpy as np
import re

class caesar(Coding.coding):
    def __init__(self, Key):
        '''
        This class applies Caesar Encryption and Decryption, You Need To Send The KEY, Note: key starting from 0
        '''
        self.set_key(Key)
    
    def encrypt(self, plain_text):
        '''
        This function apply the Caesar encryption on a Encrypted text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        encryption = ""
        for i in txt:
            for j in self.dic:
                if j[0] == i:
                    encryption += j[1]
                    break
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the Caesar decryption on a plain text.
        '''
        txt = self.splitter(encrypted_text)
        decryption = ""
        for i in txt:
            for j in self.dic:
                if j[1] == i:
                    decryption += j[0]
                    break
        return decryption


    def set_key(self, key):
        key = str(key)
        self.key = int(re.sub(r'[^0-9]', '', key))
        self.dic = []
        if self.key > 25:
            self.key = self.key % 25
        j = self.key
        for i in range(len(self.alphabet)):
            if(j >= 26):
                j = 0
            self.dic.append([self.alphabet[i], self.alphabet[j]])
            j+=1

if __name__ == "__main__":
    cypher = caesar("3")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))