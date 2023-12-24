import math

class El_Gamal_Class:
    def __init__(self, Q, A, k, Private_Key):
        self.Problem, self.Details = self.Check_Validity(Q, A, k, Private_Key)

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

    def Is_k_Valid(self, Q, k):
        if k < Q:
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
    
    def Generate_K_Key(self, Q, Power, Base):
        Value = Base ** Power % Q
        return Value

    def Generate_Cipher_1(self, Q, A, k):
        Value = A ** k % Q
        return Value

    def Generate_Cipher_2(self, Q, K, Message):
        Value = K * Message % Q
        return Value
    
    def K_Inverse(self, Q, K):
        Left = Q
        Right = K

        while(True):
            Value = Left % Right
            
            if Value == 1:
                break
            else:
                Left = Right
                Right = Value

    def Extended_GCD(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.Extended_GCD(b % a, a)
            return (g, y - (b // a) * x, x)

    def Mod_Inv(self, a, m):
        g, x, y = self.Extended_GCD(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def Decrypt_Message(self, Q, K_Inverse, Cipher_2):
        Value = Cipher_2 * K_Inverse % Q
        return Value

    def Check_Validity(self, Q, A, k, User_A_Private_Key):
        if not self.Is_Prime(Q):
            return "Problem", f"The Q value {Q} is not a prime number"
        elif not self.Is_Primitive_Root(Q, A):
            return "Problem", f"The A value {A} is not a Primitive Root number"
        elif not self.Is_k_Valid(Q, k):
            return "Problem", f"The k value {Q, k} is greater than or equal Q"
        elif not self.Is_Private_Key_Valid(Q, User_A_Private_Key):
            return "Problem", f"The Private key value {User_A_Private_Key} is greater than or equal Q"
        else:
            return "No Problem", "All Good"