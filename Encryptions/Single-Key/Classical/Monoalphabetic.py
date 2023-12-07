import Coding
import numpy as np

class monoalphabetic(Coding.coding):
    def __init__(self, Key):
        '''
        This class applies Monoalphabetic Encryption and Decryption, You Need To Send The KEY
        '''
        self.set_key(Key)
    
    def encrypt(self, plain_text):
        '''
        This function apply the Monoalphabetic encryption on a plain text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        encryption = ""
        for i in txt:
            for j in self.dic:
                if j[0] == i:
                    encryption += j[1]
                    break
            pass
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the Monoalphabetic decryption on an Encrypted text.
        '''
        txt = self.splitter(encrypted_text)
        decryption = ""
        for i in txt:
            for j in self.dic:
                if j[1] == i:
                    decryption += j[0]
                    break
            pass
        return decryption


    def set_key(self, key):
        key = str(key)
        self.key = self.splitter(self.remove_repetition(key))
        self.dic = []
        j = 0
        for i in self.key:
            self.dic.append([self.alphabet[j], i])
            j+=1
        for i in self.alphabet:
            if i not in self.key:
                self.dic.append([self.alphabet[j], i])
                j+=1


if __name__ == "__main__":
    cypher = monoalphabetic("What are you doing back here! lets go away; we have so many things to do.")
    print(cypher.key)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))