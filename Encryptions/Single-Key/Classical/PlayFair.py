import Coding
import numpy as np
class playfair(Coding.coding):

    def __init__(self, Key):
        '''
        This class applies Playfair Encryption and Decryption, You Need To Send The KEY
        '''
        self.set_key(Key)
    
    def take_each_two(self, txt):
        '''
        This function is for the inner code only. it takes each two charaters in the plain text and group them by the playfair rules.
        '''
        temp = []
        i = 0
        x = ""
        for ch in txt:
            if i == 1:
                if x != ch:
                    temp.append(x+ch)
                    i=-1
                else:
                    temp.append( x + "x")
                    i = 0
            x = ch
            i+=1
        if i == 1:
            temp.append( x + "x")

        return temp
    
    def encrypt(self, plain_text):
        '''
        This function apply the Play fair encryption on a plain text.
        '''
        # Removing spaces
        txt = self.splitter(plain_text)
        txt = self.take_each_two(txt)
        encryption = ""
        for group in txt:
                temp1 = (-1, -1)
                temp2 = (-1, -1)
                for r in range(len(self.dic)):
                    for c in range(len(self.dic[r])):
                        if group[0] == 'j':
                            group = self.replace(0, 'i', group)
                        if group[1] == 'j':
                            group = self.replace(1, 'i', group)

                        if self.dic[r][c] == group[0]:
                            temp1 = (r, c)
                        elif self.dic[r][c] == group[1]:
                            temp2 = (r, c)
                        if temp1[0] != -1 and temp2[0] != -1:
                            break
                if temp1[0] == temp2[0]:
                    if temp1[1] >= 4:
                        temp1 = (temp1[0], -1)
                    if temp2[1] >= 4:
                        temp2 = (temp2[0], -1)
                    encryption += self.dic[temp1[0]][temp1[1] + 1] + self.dic[temp2[0]][temp2[1] + 1]
                elif temp1[1] == temp2[1]:
                    if temp1[0] >= 4:
                        temp1 = (-1, temp1[1])
                    if temp2[0] >= 4:
                        temp2 = (-1, temp2[1])
                    encryption += self.dic[temp1[0] + 1][temp1[1]] + self.dic[temp2[0] + 1][temp2[1]]
                else:        
                    encryption += self.dic[temp1[0]][temp2[1]] + self.dic[temp2[0]][temp1[1]]
        return encryption

    def decrypt(self, encrypted_text):
        '''
        This function apply the Play fair decryption on a Encrypted text.
        '''
        txt = self.splitter(encrypted_text)
        txt = self.take_each_two(txt)
        decryption = ""
        for group in txt:
                temp1 = (-1, -1)
                temp2 = (-1, -1)
                for r in range(len(self.dic)):
                    for c in range(len(self.dic[r])):
                        if group[0] == 'j':
                            group = self.replace(0, 'i', group)
                        if group[1] == 'j':
                            group = self.replace(1, 'i', group)

                        if self.dic[r][c] == group[0]:
                            temp1 = (r, c)
                        elif self.dic[r][c] == group[1]:
                            temp2 = (r, c)
                        if temp1[0] != -1 and temp2[0] != -1:
                            break
                if temp1[0] == temp2[0]:
                    if temp1[1] <= 0:
                        temp1 = (temp1[0], 5)
                    if temp2[1] <= 0:
                        temp2 = (temp2[0], 5)
                    decryption += self.dic[temp1[0]][temp1[1] - 1] + self.dic[temp2[0]][temp2[1] - 1]
                elif temp1[1] == temp2[1]:
                    if temp1[0] <= 0:
                        temp1 = (5, temp1[1])
                    if temp2[0] <= 0:
                        temp2 = (5, temp2[1])
                    decryption += self.dic[temp1[0] - 1][temp1[1]] + self.dic[temp2[0] - 1][temp2[1]]
                else:        
                    decryption += self.dic[temp1[0]][temp2[1]] + self.dic[temp2[0]][temp1[1]]
        return decryption

    def set_key(self, key):
        '''
        This function removes the repetition from the key and sets the key then build the matrix (dicitionary).
        '''
        key = str(key)
        self.key = self.remove_repetition(key)
        self.dic = []

        #This loop puts the key into the dicitionary
        i = 0
        j = 0
        x = []
        for ch in key:
            if ch == 'j':
                ch = 'i'
            if ch != 'i' or 'i' not in x and 'i' not in self.dic:
                x.append(ch)
                j+=1
            if j >= 5:
                j=0
                self.dic.append(x)
                x = []
                if i < 4:
                    i+=1
                else:
                    break
            
        for ch in self.alphabet:
            if ch not in key:
                if ch == 'j':
                    ch = 'i'
                if ch != 'i' or ch == 'i' and 'i' not in x and 'i' not in self.dic:
                    x.append(ch)
                    j+=1

            if j >= 5:
                j=0
                self.dic.append(x)
                x = []
                if i < 4:
                    i+=1
                else:
                    break
        self.dic = np.array(self.dic)
        
if __name__ == "__main__" :       
    cypher = playfair("word")
    print(cypher.key)
    print(cypher.dic)
    print(cypher.encrypt("Hello World, I am a cypher"))
    print(cypher.decrypt(cypher.encrypt("Hello World, I am a cypher")))
    print(cypher.encrypt("what the are you doing"))
    print(cypher.decrypt(cypher.encrypt("what the are you doing")))