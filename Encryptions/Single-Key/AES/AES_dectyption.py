from AES_key_gen import AES_key_expansion as key_exp

class aes_decryption:
    def __init__(self):
        self.block=[]
        self.key=[]
        self.r_con = (
                        "0x00",' 0x01', '0x02', '0x04', '0x08', '0x10', '0x20', '0x40',
                        "0x80",' 0x1B', '0x36', '0x6C', '0xD8', '0xAB', '0x4D', '0x9A',
                        "0x2F",' 0x5E', '0xBC', '0x63', '0xC6', '0x97', '0x35', '0x6A',
                        "0xD4",' 0xB3', '0x7D', '0xFA', '0xEF', '0xC5', '0x91', '0x39',
                    )
        self.encrypted_matrix=[]
        self.inv_s_box = [
            [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
            [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
            [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
            [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
            [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
            [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
            [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
            [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
            [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
            [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
            [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
            [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
            [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
            [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
            [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
            [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
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
    
    def decrypt(self):
        # Initial AddRoundKey operation with the last round key

        self.add_round_key()
        exp = key_exp(self.inv_s_box, self.r_con)
         
        
        round_keys = exp.key_expansion(self.key)
        self.set_key(round_keys[10])
        self.add_round_key()

        # Perform 9 rounds of decryption operations in reverse order
        for round in range(9, 0, -1):
            # Inverse ShiftRows step
            self.inv_shift_rows()

            # Inverse SubBytes step
            self.inv_byte_subs()

            # AddRoundKey step with the current round key
            self.set_key(round_keys[round])
            self.add_round_key()

            # Inverse MixColumns step (except for the final round)
            if round > 1:
                self.inv_mix_columns()

        return self.block  # Return the decrypted block
