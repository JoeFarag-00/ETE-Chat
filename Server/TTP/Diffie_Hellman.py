import math
import random

class Diffie_Hellman_Class:
    def __init__(self, Q, A, Private_Key):
        self.Problem, self.Details = self.Check_Validity(Q, A, Private_Key)
        print(self.Problem, self.Details)
    def Is_Prime(self, Q):
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
    
    def Is_Primitive_Root(self, Q, A):
        if (A ** (Q - 1)) % Q == 1:

            for N in range(1, Q):
                Value = A ** N % Q

                if Value < 1 or Value > Q - 1:
                    return False

            return True
        else:
            return False

    def Is_Private_Key_Valid(self, Q, Private_Key):
        if Private_Key < Q:
            return True
        else:
            return False

    def Generate_Public_Keys(self, Q, A, Private_Key):
        Public_Key = A ** Private_Key % Q
        return Public_Key
    
    def Generate_Session_Key(self, Q, Private_Key, Public_Key):
        Session_Key = Public_Key ** Private_Key % Q
        return Session_Key

    def Convert_to_Binary(self, Session_Key):
        Binary_Representation = bin(Session_Key)[2:]
        return Binary_Representation
    
    def Generate_Expansion(self, Binary_Representation, Number_of_Bits):
        Expansion = [random.randint(0, len(str(Binary_Representation)) - 1) for _ in range(Number_of_Bits)]
        return Expansion

    def Expand(self, Binary_Representation, Expansion):  
        Session_Key_Bits = str(Binary_Representation)
        Expanded_Binary = ""
        for Position in Expansion:
            Expanded_Binary += Session_Key_Bits[Position]

        return Expanded_Binary.zfill(64)

    def Check_Validity(self, Q, A, Private_Key):
        if not self.Is_Prime(Q):
            return "Problem", f"The Q value {Q} is not a prime number"
        elif not self.Is_Primitive_Root(Q, A):
            return "Problem", f"The A value {A} is not a Primitive Root number"
        elif not self.Is_Private_Key_Valid(Q, Private_Key):
            return "Problem", f"The Private key value {Private_Key} is greater than or equal Q"
        else:
            return "No Problem", "All Good"