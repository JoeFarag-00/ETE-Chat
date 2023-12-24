from AES_Encryption import AES as enc
from AES_dectyption import aes_decryption as dec





# Create an instance of AES and call the encrypt function
aes = enc()
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

encrypted_block = aes.encrypt()
print("Encrypted Block:")
for row in encrypted_block:
    print(row)

#Create an instance of aes_decryption and call the decrypt function
aes_decryptor = dec()
aes_decryptor.set_block(encrypted_block)  # Use the encrypted block obtained from encryption
aes_decryptor.set_key([
    ["0F", "47", "0c", "af"],
    ["15", "D9", "b7", "7f"],
    ["71", "e8", "AD", "67"],
    ["c9", "59", "d6", "98"],
])

decrypted_block = aes_decryptor.decrypt()
print("Decrypted Block:")
for row in decrypted_block:
    print(row)



# Display key and state for each round
# for i in range(len(key_schedule)):
#     print(f"Round {i + 1} - Key:")
#     for row in key_schedule[i]:
#         print(" ".join(row))
#     print(f"\nRound {i + 1} - State:")
#     for row in state_rounds[i]:
#         print(" ".join(row))
#     print("\n")

# # add_round_key_value=aes.add_round_key()
# # print('add_round_key_vallue ',add_round_key_value)
# bytes_subs_value=aes.byte_subs()
# # print('bytes_subs_value ', bytes_subs_value)
# shift_row_value=aes.shift_rows()
# # print('shift_row_value ',shift_row_value)
# mix_columns_value=aes.mix_columns()
# # print('mix_columns_value ',mix_columns_value)









