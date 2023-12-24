class AES:
    def __init__(self):
        self.block=[]
        self.key=[]
        self.r_con = (
                        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
                        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
                        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
                        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
                    )
        self.encrypted_matrix=[]
        self.s_box = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],
        ]
    def set_block(self,block):
        self.block=block
    
    def set_key(self,key):
        self.key=key
    
    def add_round_key(self):
        if len(self.block) != len(self.key):
            raise ValueError("Block and key lengths don't match")
        encrypted_matrix = []
        for i in range(len(self.block)):
            encrypted_row = []
            for j in range(len(self.block[i])):
                block_byte = int(self.block[i][j], 16)
                key_byte = int(self.key[i][j], 16)
                result_byte = block_byte ^ key_byte
                encrypted_row.append('{:02X}'.format(result_byte))
            encrypted_matrix.append(encrypted_row)
        self.encrypted_matrix = encrypted_matrix
        self.block = self.encrypted_matrix
        return encrypted_matrix

    
    
    def byte_subs(self):
        # self.block=[['EA','04','65','85'],['83','45','5D','96'],['5C','33','98','B0'],['F0','2D','AD','C5']]
        self.encrypted_matrix = self.block
        for i in range(len(self.encrypted_matrix)):
            for k in range(len(self.encrypted_matrix[i])):
                row = self.encrypted_matrix[i][k][0]
                col = self.encrypted_matrix[i][k][1]
                row = int(row, 16)
                col = int(col, 16)
                # print(row," ",col)
                substituted_value = self.s_box[row][col] 
                self.encrypted_matrix[i][k] = hex(substituted_value)
        self.block=self.encrypted_matrix
        return(self.encrypted_matrix)
    
    def shift_rows(self):
        # self.block = [
        #     ['87', 'F2', '4D', '97'],
        #     ['EC', '6E', '4C', '90'],
        #     ['4A', 'C3', '46', 'E7'],
        #     ['8C', 'D8', '95', 'A6']
        # ] 
        self.encrypted_matrix=self.block
        for i in range(1, len(self.encrypted_matrix)):
            value=[]
            for j in range (i):
                value.append(self.encrypted_matrix[i][j])
            # print(value)
            array=[]
            for k in range (j+1,len(self.encrypted_matrix[i])):
                # print(self.encrypted_matrix[i][k])
                array.append(self.encrypted_matrix[i][k])
            array+=(value)
            # print(array)
            self.encrypted_matrix[i]=array
        self.block=self.encrypted_matrix
        return self.encrypted_matrix
    
    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b  # Reduction polynomial
            b >>= 1
        return result
    
    
    
    def mix_columns(self):
        state = self.block
        mixed_state = []
        for i in range(4):
            column = [int(state[j][i], 16) for j in range(4)]
            mixed_column = []
            for _ in range(4):
                mixed_value = (
                    self.multiply(0x02, column[0])
                    ^ self.multiply(0x03, column[1])
                    ^ column[2]
                    ^ column[3]
                )
                mixed_column.append(mixed_value)
                column = column[1:] + [column[0]]
            mixed_state.append(mixed_column)
        transposed_mixed_state = [list(row) for row in zip(*mixed_state)]
        hex_transposed_mixed_state = [
            ['{:02X}'.format(value) for value in row] for row in transposed_mixed_state
        ]
        self.block = hex_transposed_mixed_state
        return hex_transposed_mixed_state
    
    
    def encrypt(self, rounds=10):
        key_schedule = []
        state_rounds = []

        # Generate the keys
        self.get_keys()

        # Initial round: Add Round Key
        key_schedule.append(self.key)
        state_rounds.append(self.block)

        # Rounds 1 to Round 9
        for i in range(1, rounds):
            # Set the key for the current round
            self.set_key(globals()[f'key{i - 1}'])
            
            self.add_round_key()
            key_schedule.append(self.key)
            state_rounds.append(self.block)
            self.byte_subs()
            self.shift_rows()
            self.mix_columns()

        # Round 10
        self.set_key(globals()[f'key{rounds - 1}'])
        self.add_round_key()
        key_schedule.append(self.key)
        state_rounds.append(self.block)
        self.byte_subs()
        self.shift_rows()

        return key_schedule, state_rounds
    
    







aes = AES()
aes.set_block([
    ["01", "89", "fe", "76"],
    ["23", "AB", "dc", "54"],
    ["45", "cd", "BA", "32"],
    ["67", "ef", "98", "10"],
])

aes.set_key([
    ["0F", "47", "0c", "af"],
    ["15", "D9", "b7", "7f"],
    ["71", "e8", "AD", "67"],
    ["c9", "59", "d6", "98"],
])


key_schedule, state_rounds = aes.encrypt()

# Display key and state for each round
for i in range(len(key_schedule)):
    print(f"Round {i + 1} - Key:")
    for row in key_schedule[i]:
        print(" ".join(row))
    print(f"\nRound {i + 1} - State:")
    for row in state_rounds[i]:
        print(" ".join(row))
    print("\n")

# add_round_key_value=aes.add_round_key()
# # print('add_round_key_vallue ',add_round_key_value)
# bytes_subs_value=aes.byte_subs()
# # print('bytes_subs_value ', bytes_subs_value)
# shift_row_value=aes.shift_rows()
# # print('shift_row_value ',shift_row_value)
# mix_columns_value=aes.mix_columns()
# # print('mix_columns_value ',mix_columns_value)


class AES_key_expansion:
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




    def key_expansion(self,key):
        transposed_key = [list(row) for row in zip(*key)]
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
    







class aes_decryption:
    def __init__(self):
        self.block=[]
        self.key=[]
        self.r_con = (
                        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
                        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
                        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
                        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
                    )
        self.encrypted_matrix=[]
        self.inv_s_box = [
            ['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
            ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
            ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
            ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
            ['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
            ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
            ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
            ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
            ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
            ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
            ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
            ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
            ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
            ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
            ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
            ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']
        ]
        
    def set_block(self,block):
        self.block=block
    
    def set_key(self,key):
        self.key=key
    
    def add_round_key(self):
        if len(self.block) != len(self.key):
            raise ValueError("Block and key lengths don't match")
        encrypted_matrix = []
        for i in range(len(self.block)):
            encrypted_row = []
            for j in range(len(self.block[i])):
                block_byte = int(self.block[i][j], 16)
                key_byte = int(self.key[i][j], 16)
                result_byte = block_byte ^ key_byte
                encrypted_row.append('{:02X}'.format(result_byte))
            encrypted_matrix.append(encrypted_row)
        self.encrypted_matrix = encrypted_matrix
        self.block = self.encrypted_matrix
        return encrypted_matrix

    
    
    def inv_byte_subs(self):
        # Use the inverse S-box for byte substitution
        self.encrypted_matrix = self.block
        for i in range(len(self.encrypted_matrix)):
            for k in range(len(self.encrypted_matrix[i])):
                row = self.encrypted_matrix[i][k][0]
                col = self.encrypted_matrix[i][k][1]
                row = int(row, 16)
                col = int(col, 16)
                substituted_value = self.inv_s_box[row][col]  # Use inverse S-box
                self.encrypted_matrix[i][k] = hex(substituted_value)
        self.block = self.encrypted_matrix
        return self.encrypted_matrix
    
    def inv_shift_rows(self):
        # Similar to shift_rows but in the inverse direction
        self.encrypted_matrix = self.block
        for i in range(1, len(self.encrypted_matrix)):
            value = []
            for j in range(len(self.encrypted_matrix[i]))[::-1]:
                value.append(self.encrypted_matrix[i][j])
            array = value[-i:] + value[:-i]
            self.encrypted_matrix[i] = array
        self.block = self.encrypted_matrix
        return self.encrypted_matrix
    
    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b  # Reduction polynomial
            b >>= 1
        return result
    
    
    
    def inv_mix_columns(self):
        state = self.block
        inv_mixed_state = []
        for i in range(4):
            column = [int(state[j][i], 16) for j in range(4)]
            inv_mixed_column = []
            for _ in range(4):
                inv_mixed_value = (
                    self.multiply(0x0e, column[0])
                    ^ self.multiply(0x0b, column[1])
                    ^ self.multiply(0x0d, column[2])
                    ^ self.multiply(0x09, column[3])
                )
                inv_mixed_column.append(inv_mixed_value)
                column = column[1:] + [column[0]]
            inv_mixed_state.append(inv_mixed_column)
        transposed_inv_mixed_state = [list(row) for row in zip(*inv_mixed_state)]
        hex_transposed_inv_mixed_state = [
            ['{:02X}'.format(value) for value in row] for row in transposed_inv_mixed_state
        ]
        self.block = hex_transposed_inv_mixed_state
        return hex_transposed_inv_mixed_state
    
    
    def decrypt(self, rounds=10):
        # Reversing the order of operations
        key_schedule = []
        state_rounds = []

        # AddRoundKey for Round 10
        self.set_key(globals()[f'key{rounds - 1}'])
        self.add_round_key()
        state_rounds.append(self.block)

        # Inverse ShiftRows and Inverse ByteSubs for Rounds 9 to 1
        for i in range(rounds - 1, 0, -1):
            self.inv_shift_rows()
            self.inv_byte_subs()
            self.set_key(globals()[f'key{i - 1}'])
            self.add_round_key()
            key_schedule.insert(0, self.key)
            state_rounds.insert(0, self.block)
            self.inv_mix_columns()

        # Final Inverse ShiftRows and Inverse ByteSubs for Round 0
        self.inv_shift_rows()
        self.inv_byte_subs()
        self.set_key(globals()['key0'])
        self.add_round_key()
        state_rounds.insert(0, self.block)

        return key_schedule, state_rounds