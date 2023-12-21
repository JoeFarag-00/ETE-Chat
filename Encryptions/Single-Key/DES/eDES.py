class edDES:
    def __init__(self):
        self.ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]

        self.fp_table = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

        self.e_table = [32, 1, 2, 3, 4, 5, 4, 5,
                6, 7, 8, 9, 8, 9, 10, 11,
                12, 13, 12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21, 20, 21,
                22, 23, 24, 25, 24, 25, 26, 27,
                28, 29, 28, 29, 30, 31, 32, 1]

        self.p_table = [16, 7, 20, 21, 29, 12, 28, 17,
                1, 15, 23, 26, 5, 18, 31, 10,
                2, 8, 24, 14, 32, 27, 3, 9,
                19, 13, 30, 6, 22, 11, 4, 25]

        self.s_boxes = [
            # S1
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
            ],

            # S2
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            ],

            # S3
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
            ],

            # S4
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
            ],

            # S5
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
            ],

            # S6
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
            ],

            # S7
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
            ],

            # S8
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
            ],
                
        ]

        self.pc1_table = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]

        self.pc2_table = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

        self.ipc_table = [57, 49, 41, 33, 25, 17, 9, 1,
                    58, 50, 42, 34, 26, 18, 10, 2,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    60, 52, 44, 36, 63, 55, 47, 39,
                    31, 23, 15, 7, 62, 54, 46, 38,
                    30, 22, 14, 6, 61, 53, 45, 37,
                    29, 21, 13, 5, 28, 20, 12, 4]

        self.shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        

    def Permutate(self, data, table):
        print(f"Data: {data}, Table: {table}")
        result = ''
        
        for i in table:
            if 1 <= i <= len(data):
                result += data[i - 1]
            else:
                print(f"Warning: Index {i} is out of range for data '{data}'")
                
        return result

    def Generate_Subkeys(self, key):
        key = self.Permutate(key, self.pc1_table)
        left, right = key[:28], key[28:]
        subkeys = []

        for shift in self.shifts:
            left = left[shift:] + left[:shift]
            right = right[shift:] + right[:shift]
            combined = left + right
            subkeys.append(self.Permutate(combined, self.pc2_table))

        return subkeys

    def Feistel_Function(self, right, subkey):
        expanded = self.Permutate(right, self.e_table)
        xor_result = bin(int(expanded, 2) ^ int(subkey, 2))[2:].zfill(48)

        sbox_result = ''
        for i in range(0, 48, 6):
            block = xor_result[i:i + 6]
            row = int(block[0] + block[-1], 2)
            col = int(block[1:5], 2)
            sbox_result += format(self.s_boxes[i // 6][row][col], '04b')

        result = self.Permutate(sbox_result, self.p_table)
        return result

    def Encrypt(self, plain_text, key):
        blocks = [plain_text[i:i+64] for i in range(0, len(plain_text), 64)]
        encrypted_blocks = []

        for block in blocks:
            block = self.Permutate(block, self.ip_table)

            subkeys = self.Generate_Subkeys(key)

            left, right = block[:32], block[32:]

            for subkey in subkeys:
                new_right = bin(int(left, 2) ^ int(self.Feistel_Function(right, subkey), 2))[2:].zfill(32)
                left = right
                right = new_right

            encrypted_block = self.Permutate(right + left, self.fp_table)
            encrypted_blocks.append(encrypted_block)

        return ''.join(encrypted_blocks)

    def Decrypt(self, cipher_text, key):
        blocks = [cipher_text[i:i+64] for i in range(0, len(cipher_text), 64)]
        decrypted_blocks = []

        for block in blocks:
            block = self.Permutate(block, self.ip_table)

            subkeys = self.Generate_Subkeys(key)[::-1]

            left, right = block[:32], block[32:]

            for subkey in subkeys:
                new_right = bin(int(left, 2) ^ int(self.Feistel_Function(right, subkey), 2))[2:].zfill(32)
                left = right
                right = new_right

            plain_text_binary = self.Permutate(right + left, self.fp_table)

            plain_text = ''.join(chr(int(plain_text_binary[i:i + 8], 2)) for i in range(0, len(plain_text_binary), 8))
            decrypted_blocks.append(plain_text)

        return ''.join(decrypted_blocks)
    
    def Pad_Characters(self,input_string):
        character_count = len(input_string)
        spaces_needed = (8 - character_count % 8) % 8
        padded_string = input_string + " " * spaces_needed
        return character_count, padded_string
    
    def Remove_Padding(self,input_string):
        unpadded_string = input_string.rstrip()
        return unpadded_string


if __name__ == "__main__":
    
    plaintext = "Hello, I am king Youssef the Great."
    key = "secretke"

    des_instance = edDES()
    
    Cct, plaintext = des_instance.Pad_Characters(plaintext)
    plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext)
    key_binary = ''.join(format(ord(char), '08b') for char in key)

    encrypted_text = des_instance.Encrypt(plaintext_binary, key_binary)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = des_instance.Decrypt(encrypted_text, key_binary)
    decrypted_text = des_instance.Remove_Padding(decrypted_text)
    
    print(f"Decrypted Text: {decrypted_text}")
    
    
