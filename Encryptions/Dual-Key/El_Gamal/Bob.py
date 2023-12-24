from El_Gamal import El_Gamal_Class
import socket
import random
import math

Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host = '127.0.0.1'
Port = 12345
Client_Socket.connect((Host, Port))

def Is_Prime(Q):
        if Q < 2:
            return False
        elif Q == 2:
            return True
        elif Q % 2 == 0:
            return False

        Sqrt_Number = int(math.sqrt(Q)) + 1
        for i in range(3, Sqrt_Number, 2):
            if Q % i == 0:
                return False
        return True

def generate_random_prime(start, end):
    while True:
        candidate = random.randint(start, end)
        if Is_Prime(candidate):
            return candidate

Q = generate_random_prime(100, 999)
A = random.randint(2, Q - 1)
k = random.randint(1, Q - 1)
Private_Key = random.randint(1, Q - 1)

# Q = 19
# A = 10
# k = 6
# Private_Key = 5

Client_Socket.send(str(Q).encode('utf-8'))
print(f"Q sent: {Q}")

Response = Client_Socket.recv(1024).decode('utf-8')
print(Response)

Client_Socket.send(str(A).encode('utf-8'))
print(f"A sent: {A}")

Response = Client_Socket.recv(1024).decode('utf-8')
print(Response)

Client_Socket.send(str(k).encode('utf-8'))
print(f"k sent: {k}")

Response = Client_Socket.recv(1024).decode('utf-8')
print(Response)

Diffie_Hellman_Object = El_Gamal_Class(Q, A, k, Private_Key)

if Diffie_Hellman_Object.Problem == "No Problem":
    Public_Key = Diffie_Hellman_Object.Generate_Public_Keys(Q, A, Private_Key)
    print(f"Public Key: {Public_Key}")

    Client_Socket.send(str(Public_Key).encode('utf-8'))
    print(f"Public key sent: {Public_Key}")

    Cipher_1 = Client_Socket.recv(1024).decode('utf-8')
    Cipher_1 = int(Cipher_1)
    print(f"Recieved Cipher_1: {Cipher_1}")
    Response = f"Cipher_1 Recieved: {Cipher_1}"
    Client_Socket.send(Response.encode('utf-8'))
    print(f"Response sent")

    Cipher_2 = Client_Socket.recv(1024).decode('utf-8')
    Cipher_2 = int(Cipher_2)
    print(f"Recieved Cipher_2: {Cipher_2}")
    Response = f"Cipher_2 Recieved: {Cipher_2}"
    Client_Socket.send(Response.encode('utf-8'))
    print(f"Response sent")

    K = Diffie_Hellman_Object.Generate_K_Key(Q, Private_Key, Cipher_1)
    print(f"K value: {K}")
    K_Inverse = Diffie_Hellman_Object.Mod_Inv(K, Q)
    print(f"K_Inverse value: {K_Inverse}")
    Message_Integer = Diffie_Hellman_Object.Decrypt_Message(Q, K_Inverse, Cipher_2)
    print(f"M value: {Message_Integer}")

    # Message_Text = Message_Integer.to_bytes((Message_Integer.bit_length()+7) // 8, byteorder='big').decode()
    # print(f"M value: {Message_Text}")
else:
    print(Diffie_Hellman_Object.Problem, Diffie_Hellman_Object.Details)