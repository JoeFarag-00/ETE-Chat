import Coding
import numpy as np
import re
import copy

class rowtransposition(Coding.coding):
    def __init__(self, Key : int):
        '''
        This class applies Row Transposition Encryption and Decryption, You Need To Send The KEY
        '''
        self.set_key(Key)
    
    def encrypt(self, plain_text):
        '''
        This function apply the Row Transposition encryption on a plain text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        encryption = ""
        dic = copy.deepcopy(self.dic)

        for i in range(0, len(txt)):
            if i % len(self.key) == 0:
                x = []
                dic.append(x)
            x.append(txt[i])

        for i in range(0, len(self.key) - len(dic[-1])):
            dic[-1].append(self.alphabet[-1])
        for i in range(0, len(self.key)):
            for c in range(0, len(self.key)):
                if dic[0][c] == i:
                    for r in range(1, len(dic)):
                        encryption += dic[r][c]
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the Row Transposition decryption on an Encrypted text.
        '''
        txt = self.splitter(encrypted_text)
        decryption = ""

        dic = copy.deepcopy(self.dic)
        rows = len(txt) // len(self.key)

        for r in range(0, rows):
            dic.append(["" for c in range(0, len(self.key))])

        j = 0
        for i in range(0, len(self.key)):
            for c in range(0, len(self.key)):
                if dic[0][c] == i:
                    for r in range(1, len(dic)):
                        dic[r][c] = txt[j]
                        if j < len(txt) -1:
                            j+=1
        
        for r in range(1, len(dic)):
            for c in dic[r]:
                decryption += c        
        return decryption

    def sortme(self):
        temp = []
        for i in range(0, len(self.key)):
            temp.append(int(self.key[i]))
        if max(temp) == len(temp): return
        
        for i in range(1, max(temp)):
            if i not in temp:
                for j in range(0, len(temp)):
                    if i < temp[j]:
                        temp.insert(j, i)
                        break
        self.key = ""
        for i in temp:
            self.key += str(i)

    def set_key(self, key : int):

        key = str(key)
        self.key = re.sub(r'[^0-9]', '', key)
        self.sortme()
        self.dic = [[int(i) - 1 for i in self.key]]


if __name__ == "__main__":
    cypher = rowtransposition("15679")
    print("Dic: ",cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))

    print(cypher.encrypt("attack postponed until two am."))
    print(cypher.decrypt(cypher.encrypt("attack postponed until two am.")))
