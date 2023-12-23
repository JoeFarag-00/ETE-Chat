from Diffie_Hellman import Diffie_Hellman_Class
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
Private_Key = random.randint(1, Q - 1)

Client_Socket.send(str(Q).encode('utf-8'))
print(f"Q sent: {Q}")

Response = Client_Socket.recv(1024).decode('utf-8')
print(Response)

Client_Socket.send(str(A).encode('utf-8'))
print(f"A sent: {A}")

Diffie_Hellman_Object = Diffie_Hellman_Class(Q, A, Private_Key)

if Diffie_Hellman_Object.Problem == "No Problem":
    Public_Key = Diffie_Hellman_Object.Generate_Public_Keys(Q, A, Private_Key)
    print(Public_Key)

    Client_Socket.send(str(Public_Key).encode('utf-8'))
    print(f"Public key sent: {Public_Key}")

    Other_User_Public_Key = Client_Socket.recv(1024).decode('utf-8')
    Other_User_Public_Key = int(Other_User_Public_Key)
    print(f"Other user public key: {Other_User_Public_Key}")

    Session_Key = Diffie_Hellman_Object.Generate_Session_Key(Q, Private_Key, Other_User_Public_Key)
    print(f"Session Key: {Session_Key}")

    Binary_Key = Diffie_Hellman_Object.Convert_to_Binary(Session_Key)
    Expansion = Diffie_Hellman_Object.Generate_Expansion(Binary_Key, 64)
    Client_Socket.send(str(Expansion).encode('utf-8'))
    Final_Key = Diffie_Hellman_Object.Expand(Binary_Key, Expansion)

    print(f"Final Key: {Final_Key}")
    print(f"Final Key Length: {len(str(Final_Key))}")
else:
    print(Diffie_Hellman_Object.Problem, Diffie_Hellman_Object.Details)