class AES_key_expansion:
    def __init__(self, sbox, rcon):
        self.s_box = sbox
        self.r_con = rcon
        pass
    def root_word(self,word):
        shifted_word = word[1:] + [word[0]]
        return shifted_word

    def sub_word(self,word):
        for i in range(len(word)):
            row = int(word[i][0], 16)
            col = int(word[i][1], 16)
            substituted_value = self.s_box[row][col]
            word[i] = hex(substituted_value)[2:].zfill(2)
        return word

    def g_function(self,word, index):
        word = self.root_word(word)
        word = self.sub_word(word)
        word = self.round_constant_step(word, index)
        return word

    def round_constant_step(self,word, index):
        Round_contant = [int(self.r_con[index], 16), 0, 0, 0]
        word = [int(x, 16) for x in word]
        result = [Round_contant[i] ^ word[i] for i in range(len(Round_contant))]
        result = [hex(val)[2:].zfill(2) for val in result]
        return result

    def xor_maker(self,first_operand,second_operand):
        result = [int(first_operand[i],16) ^ int(second_operand[i],16) for i in range(len(first_operand))]
        result = [hex(val)[2:].zfill(2) for val in result]
        return result

    def words_maker(self,words):
        round_index=0
        g_output=self.g_function(words[-1],round_index)
        new_words=[]
        for i in range (0,4):
            g_output=self.xor_maker(g_output,words[i])
            new_words.append(g_output)
        return new_words

    def key_expansion(self, key):
        transposed_key = key#[list(row) for row in zip(*key)]
        columns = list(map(list, zip(*transposed_key)))
        words = []
        for col in columns:
            words.append(col)
        print('words in orgin ',words)
        key_array = []
        key_array.append(words)
        # print("before g function ",words[len(words) - 1])
        # print("after g_function ",g_function(words[len(words) - 1],8))
        i=0
        while i<10:
            key_array.append(self.words_maker(key_array[-1]))
            i+=1


        return key_array