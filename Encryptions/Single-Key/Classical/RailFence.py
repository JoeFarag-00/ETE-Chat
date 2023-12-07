import Coding
import numpy as np
import copy
import re

class railfence(Coding.coding):
    def __init__(self, Key : int):
        '''
        This class applies RailFence Encryption and Decryption, You Need To Send The KEY
        '''
        self.set_key(Key)
    
    def get_zigzag(self, txt = "", encrypt = True):
        l = len(txt)
        dic = copy.deepcopy(self.dic)
        rr = 0
        down = True
        i = 0
        
        for c in range(0, l):
            for r in range(0, len(dic)):
                temp = txt[i] if encrypt else "-"
                dic[r].append(temp if r == rr else "")
            if i < len(txt):
                i+=1
            
            if rr == 0:
                down = True
            elif rr == len(dic) - 1:
                down = False
            rr += 1 if down else -1
        
        if not encrypt:
            i = 0
            for r in range(0, len(dic)):
                for c in range(0, len(dic[r])):
                    if dic[r][c] == "-":
                        dic[r][c] = txt[i]
                        if i < len(txt)-1:
                            i+=1
        return dic

    def encrypt(self, plain_text):
        '''
        This function apply the RailFence encryption on a plain text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        encryption = ""
        dic = self.get_zigzag(txt, True)
        for r in dic:
            for c in r:
                if c != "":
                    encryption += c
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the RailFence decryption on an Encrypted text.
        '''
        txt = self.splitter(encrypted_text)
        decryption = ""
        dic = self.get_zigzag(txt, False)
        
        for c in range(0, len(encrypted_text)):
            for r in range(0, len(dic)):
                if dic[r][c] != "":
                    decryption += dic[r][c]
        return decryption


    def set_key(self, key : int):
        key = str(key)
        self.key = int(re.sub(r'[^0-9]', '', key))
        self.dic = []
        for i in range(0, self.key):
            x = []
            self.dic.append(x)

if __name__ == "__main__":
    cypher = railfence("11")
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    cypher = railfence(2)
    print(cypher.dic)
    print(cypher.encrypt("This is a secret message."))
    print(cypher.decrypt(cypher.encrypt("This is a secret message.")))

    cypher = railfence(4)
    print(cypher.dic)
    print(cypher.encrypt("They are attacking from the north"))
    print(cypher.decrypt(cypher.encrypt("They are attacking from the north")))