import customtkinter
import os
import threading
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
import re
import cv2
from tkinter import Label, Text, Button, Menu
import random
from PIL import Image
from tkinter_webcam import webcam
import time
import sys
import socket
import re
import math

sys.path.append('Encryptions/Single-Key/Classical')
from Caesar import caesar
sys.path.append('Encryptions/Single-Key/Classical')
from Monoalphabetic import monoalphabetic
sys.path.append('Encryptions/Single-Key/Classical')
from PlayFair import playfair
sys.path.append('Encryptions/Single-Key/Classical')
from RailFence import railfence
sys.path.append('Encryptions/Single-Key/Classical')
from RowTransposition import rowtransposition
sys.path.append('Encryptions/Single-Key/Classical')
from Vigenere import vigenere
sys.path.append('Encryptions/Single-Key/DES')
from eDES import edDES
sys.path.append('Encryptions/Dual-Key/RSA')
from edRSA import rsa_keygenerator
sys.path.append('Encryptions/Single-Key/RC4')
from eRC4 import edRC4
sys.path.append('Server/TTP')
from Diffie_Hellman import Diffie_Hellman_Class
sys.path.append('Encryptions/Dual-Key/ElGamal')
from ElGamal import El_Gamal_Class

User_Logo = customtkinter.CTkImage(light_image=Image.open("Assets/person.png"),
                                  size=(100, 100))

Main = customtkinter.CTk()

class MainGUI:
    def __init__(self):
        self.Main = Main
        self.start_chat = False
        self.LineCt = 0
        self.IsEncryption = False
        self.Loaded_Dashboard = False
        self.Rec_Message = None
        self.Auth_Name = ""
        self.Rec_Type = None
        self.DoOnceBob = False
        self.DoOnceAlice = False
        self.ReceivedQA = False
        self.CurEnc_Stat = "None"
        self.IsChanged = False
        self.loaded_dashboard_event = threading.Event()
        self.Encryptions = ["#DES", "#AES", "#RSA", "#RC4", "#El Gammal", "#Caesar", "#Monoalphabetic","#PlayFair","#RailFence","#Row Transposition", "#Vigenere", "#None"]
        self.Enc_Structure = r"#([^#]+)#([^#]+)$"
        self.Private_Key = None
        self.Private_Key2 = None
        # self.sendQA_Structure = r'#(\d+),(\d+)#'
        # self.KeyBox = None
        # self.KeyEntry = None

        # self.Rsa_KeyGen = RSA_KeyGen()
        # self.Caesar = caesar()
        
        self.Users = [
        {"id": "211777", "password": "1234","name": "Youssef"},
        {"id": "212257", "password": "1234","name": "Mina"},
        ]
        
    @staticmethod
    def DestroyAll():
        widgets = Main.winfo_children()
        for widget in widgets:
            widget.destroy()

    def Continue(self):
        self.DestroyAll()
        self.Login_Page()

    def Exit(self):
        os._exit(0)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def Get_Dashboard(self):
        self.DestroyAll()
        
        self.sent_message = None
        self.received_message = None
        self.message_counter = 1
        self.chat_counter = 2
        self.Main.resizable(width=False, height=False)
        self.Main.title("Dashboard")
        self.Main.geometry(f"{1100}x{570}")
        self.Main.grid_columnconfigure(1, weight=1)
        self.app_logo = customtkinter.CTkImage(light_image=Image.open("Assets/person.png"), size=(100, 100))
        self.sidebar_frame = customtkinter.CTkFrame(self.Main, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo = customtkinter.CTkLabel(self.sidebar_frame, image=self.app_logo, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Nurse", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20)
        
        # self.Profile_Button = customtkinter.CTkButton(self.sidebar_frame, text="Profile")
        # self.Profile_Button.grid(row=2, column=0, padx=20, pady=10)
 
        self.Encryption_Box = customtkinter.CTkComboBox(self.sidebar_frame,
        values=["DES", "AES", "RSA", "RC4", "El Gammal", "Caesar", "Monoalphabetic","PlayFair","RailFence","Row Transposition", "Vigenere", "None"],command=self.Encryption_Callback)
        self.Encryption_Box.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.Encryption_Box.set("Encryptions")
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_options = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_options.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        self.exit_button = customtkinter.CTkButton(self.sidebar_frame, text="Exit", hover_color="Red", command=self.Exit)
        self.exit_button.grid(row=7, column=0, padx=20, pady=5)
        
        self.set_name()
        
        self.tabview = customtkinter.CTkTabview(master=self.Main, width=250, height=490)
        self.tabview.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(10, 0), sticky="nsew")
        self.tabview.add("All")
        self.tabview.set("All")
        
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("All"), width=840, height=420)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.textbox.configure(state="disabled")

        self.entry = customtkinter.CTkEntry(self.Main, placeholder_text="Type a message")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Send_Button = customtkinter.CTkButton(self.Main, text="Send", fg_color="transparent", border_width=2,
                                                text_color=("gray10", "#DCE4EE"), command=self.Send_Message)
        self.Send_Button.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        self.Loaded_Dashboard = True
        #BOB
        if not self.ReceivedQA:
            self.Q = self.generate_random_prime(100, 999)
            self.A = random.randint(2, self.Q - 1)
            self.Private_Key = random.randint(1, self.Q - 1)
            
            
            print(f"Created Initial: ",self.Q ,self.A)
            print("pk:", self.Private_Key)
            
            self.Deff = Diffie_Hellman_Class(self.Q, self.A, self.Private_Key)
            if self.Deff.Problem == "No Problem":
                self.Public_Key = self.Deff.Generate_Public_Keys(self.Q, self.A, self.Private_Key)
                print("Public Key OLD: ", self.Public_Key)
        
                self.Send_QA()
                self.Send_Public(1,self.Public_Key)
        
    def Send_QA(self):
        self.sentQA_Structure = "#" + str(self.Q) + "," + str(self.A) + "#"
        client_socket.send(self.sentQA_Structure.encode('utf-8'))
        
    def Send_Public(self,i,pub):
        self.sentPUBStructure = f"#p{i}"+ str(pub) + "#"
        client_socket.send(self.sentPUBStructure.encode('utf-8'))
        
    def Generate_Session_Key(self, Q, Private_Key, Public_Key):
        Session_Key = Public_Key ** Private_Key % Q
        return Session_Key
    
    def Is_Prime(self,Q):
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

    def generate_random_prime(self,start, end):
        while True:
            candidate = random.randint(start, end)
            if self.Is_Prime(candidate):
                return candidate
            
    def Fix_Spacing(self,message,target):
        if target == 1:
            return message.replace(' ', 'x')
        else:
            return message.replace('x', ' ')
        
    def digits_to_letters(self,input_string):
        digit_to_letter = {str(i): chr(ord('A') + i) for i in range(10)}
        input_string = str(input_string)
        result = ''.join(digit_to_letter[digit] for digit in input_string if digit in digit_to_letter)
        return result
    
    def format_to_64_bits(self,number):
        binary_representation = bin(number)[2:]

        if len(binary_representation) < 64:
            duplicated_bits = binary_representation * ((64 // len(binary_representation)) + 1)
            formatted_binary = duplicated_bits[:64]
        else:
            formatted_binary = binary_representation[:64]
        return formatted_binary
    
    def Encryption_Callback(self,Type):
        print("\n\nEncryption Type: ", Type)
        
        try:
            self.Final_Session_Key = self.Session_Key1
        except:
            pass
        
        try:
            self.Final_Session_Key = self.Session_Key2
        except:
            pass
        # print(self.Encryption_Box.get())
        self.Rec_Type = self.Encryption_Box.get()
        Type = self.Encryption_Box.get()
        if Type == "None":
            self.IsEncryption = False
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
        elif Type == "Caesar":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Key")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
            #Special_Case_Caesar
            self.KeyEntry.insert(0,self.Final_Session_Key)


            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
        elif Type == "Monoalphabetic":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            self.KeyBox = customtkinter.CTkTextbox(self.sidebar_frame, width=140, height=150)
            self.KeyBox.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
            Alter = self.digits_to_letters(self.Final_Session_Key)
            self.KeyBox.insert("0.0",Alter)
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
        elif Type == "PlayFair":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyBox = customtkinter.CTkTextbox(self.sidebar_frame, width=140, height=150)
            self.KeyBox.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
            
            Alter = self.digits_to_letters(self.Final_Session_Key)
            self.KeyBox.insert("0.0",Alter)
            
        elif Type == "RailFence": ###FIX REILFENCE 123245 NUMBER TOO BIG
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Key")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
       
            # Alter = self.digits_to_letters(self.Final_Session_Key)
            self.KeyEntry.insert(0,self.Final_Session_Key)
            
            
        elif Type == "Row Transposition": ##FIX SORTED numbers
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Key")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
            
            self.KeyEntry.insert(0,self.Final_Session_Key)

            
        elif Type == "Vigenere":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyBox = customtkinter.CTkTextbox(self.sidebar_frame, width=140, height=150)
            self.KeyBox.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
            
            Alter = self.digits_to_letters(self.Final_Session_Key)
            self.KeyBox.insert("0.0",Alter)
            
        elif Type == "DES":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Key (56)")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
            self.KeyEntry.insert(0,self.Final_Session_Key)

        elif Type == "RC4":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter key-gen int")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))
            
            
        elif Type == "RSA":
            self.IsEncryption = True
            try:
                self.KeyBox.destroy()
                self.KeyEntry.destroy()
                self.Set_Key_Button.destroy()
            except:
                pass
            
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="key-gen")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5))
                
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                        text_color=("gray10", "#DCE4EE"), command=self.Set_Key)
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))

    def normalize_to_64_bit_binary(self,input_str):
        binary_str = ''.join(format(ord(char), '08b') for char in input_str)
        binary_str = binary_str[:64]
        binary_str = binary_str.ljust(64, '0')
        return binary_str
    
    def Set_Key(self):
        self.WarningLabel3 = customtkinter.CTkLabel(Main, text="Incorrect Key", font=customtkinter.CTkFont(size=12, weight="bold"), text_color="red")
        
        self.Type = self.Encryption_Box.get()
        
        if self.Type == "None" or self.Type == "Choose Encryption":
            self.IsEncryption = False
            self.IsChanged = True
        elif self.Type == "Caesar":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = int(self.KeyEntry.get())
                self.Caesar = caesar(self.Enc_Key)
                print("Caesar Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("Caesar Error", e)
        elif self.Type == "Monoalphabetic":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyBox.get("0.0", "end")
                self.Mono = monoalphabetic(self.Enc_Key)
                print("Monoalphabetic Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("Monoalphabetic Error:",e)
        elif self.Type == "PlayFair":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyBox.get("0.0", "end")
                self.PlayFair = playfair(self.Enc_Key)
                print("PlayFair Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("PlayFair Error:",e)
        elif self.Type == "RailFence":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = int(self.KeyEntry.get())
                self.RailFence = railfence(self.Enc_Key)
                print("RailFence Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("RailFence Error", e)
        elif self.Type == "Row Transposition":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyEntry.get()
                self.RowTrans = rowtransposition(self.Enc_Key)
                print("Row Transposition Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("Row Transposition Error", e)
        elif self.Type == "Vigenere":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyBox.get("0.0", "end")
                self.Vigenere = vigenere(self.Enc_Key)
                print("Vigenere Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("Vigenere Error", e)
        elif self.Type == "DES":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyEntry.get()
                self.EncDES = edDES()
                self.Enc_Key = self.normalize_to_64_bit_binary(self.Enc_Key)
                print("DES Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("DES Error", e)
                    
        elif self.Type == "RC4": ###FIXXX KEY DISTRO
            self.IsEncryption = True
            self.IsChanged = True
            # try:
            digit = self.KeyEntry.get()
            digit = int(digit)
            self.Enc_Key = edRC4.generate_key(digit)
            self.EncRC4 = edRC4(self.Enc_Key,digit)
            digit = str(digit)
            
            self.Enc_Key = str(self.Enc_Key)
            client_socket.send("#RC#"+digit+ "#"+ self.Enc_Key.encode('utf-8'))
            print("RC4 Loaded Key: ", self.Enc_Key,"\n")
           
        elif self.Type == "El Gammal":
            self.IsEncryption = True
            self.IsChanged = True
  
        elif self.Type == "RSA":
            self.IsEncryption = True
            self.IsChanged = True
            try:
                self.Enc_Key = self.KeyEntry.get()
                self.EncRSA = rsa_keygenerator()
                
                print("RSA Loaded Key: ", self.Enc_Key,"\n")
            except Exception as e:
                print("RSA Error", e)
        #FOR SYNC ENCRYPTIONS
        # self.CurEnc_Stat = "#"+self.Type+"#"+str(self.Enc_Key)
        # print("Current Encryption: ",self.CurEnc_Stat)
        
        # client_socket.send(self.CurEnc_Stat.encode('utf-8'))


    
    def Send_Message(self):
        Send_Message = self.entry.get()
        Type = self.Encryption_Box.get()
        
        # if(self.Private_Key):
        #     print("Curr Q:",self.Q, "Curr A:", self.A, "Curr PK:", self.Private_Key, "Curr Public: ",self.Public_Key)
        # elif(self.Private_Key2):
        #     print("Curr Q:",self.Q, "Curr A:", self.A, "Curr PK:", self.Private_Key2, "Curr Public: ",self.Public_Key)

                 
        if Send_Message:
             
            self.entry.delete(0, len(Send_Message))
            self.textbox.insert("end", f"[{self.Auth_Name}]:\n{Send_Message}\n\n")
            
            print("Original Message: ",Send_Message)
            # self.textbox.configure(state="normal")
            if Type == "None" or not self.IsEncryption:
                client_socket.send(Send_Message.encode('utf-8'))
            elif Type == "Caesar":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.Caesar.encrypt(Send_Message)
                print("Caesar Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "Monoalphabetic":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.Mono.encrypt(Send_Message)
                print("Monoalphabetic Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "PlayFair":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.PlayFair.encrypt(Send_Message)
                print("PlayFair Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "RailFence":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.RailFence.encrypt(Send_Message)
                print("RailFence Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "Row Transposition":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.RowTrans.encrypt(Send_Message)
                print("Row Transposition Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "Vigenere":
                Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = self.Vigenere.encrypt(Send_Message)
                print("Vigenere Message:", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "DES":
                # Send_Message = self.Fix_Spacing(Send_Message, 1)
                Send_Message = self.EncDES.Pad_Characters(Send_Message)
                Send_Message = ''.join(format(ord(char), '08b') for char in Send_Message)
                Key_BN = ''.join(format(ord(char), '08b') for char in self.Enc_Key)
                Encrypted_Message = self.EncDES.Encrypt(Send_Message, Key_BN)
                print("Encrypted_Message", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif Type == "RC4":###KEY DISTRO
                # Send_Message = self.Fix_Spacing(Send_Message, 1)
                Encrypted_Message = str(self.EncRC4.encrypt_and_decrypt(Send_Message))
                print("Encrypted_Message", Encrypted_Message,"\n\n")
                client_socket.send(Encrypted_Message.encode('utf-8'))
            
            ##RC44444444444444444
            
            # self.textbox.configure(state="disabled")
                    
    def Recieve_Message(self):
        while True:
            
            self.Rec_Message = None

            self.Rec_Message = client_socket.recv(1024).decode('utf-8')
            print("Received Encrypted:",self.Rec_Message,"\n")

            #ALICE
            Match_QA = re.fullmatch(r'#(\d+),(\d+)#',self.Rec_Message)
            Match_Pu = re.search(r'#p1(\d+)#',self.Rec_Message)
            Match_Pu2 = re.search(r'#p2(\d+)#',self.Rec_Message)
            Match_RC4 = re.search(r"#RC#(\d+)",self.Rec_Message)
            Match_Method = re.match(r"#([^#]+)#([^#]+)$", self.Rec_Message)
            
            
            if Match_RC4 and self.Type == "RC4":
                digit = int(Match_RC4.group(1))
                key = self.Rec_Message
                self.RC4Zena = edRC4(key,digit) 
                
            if Match_Pu:
                #Recieved My key
                self.OppoPublic_Key = int(Match_Pu.group(1))
                print("Swapped PUKEY: ", self.OppoPublic_Key)
                self.Send_Public(2,self.Public_Key)
                self.Session_Key1 = self.Generate_Session_Key(self.Q, self.Private_Key2, self.OppoPublic_Key)
                print("FINAL SESSION KEY1:",self.Session_Key1)
                
            elif Match_Pu2:
                self.OppoPublic_Key2 = int(Match_Pu2.group(1))
                print("Swapped PUKEY2: ", self.OppoPublic_Key2)
                self.Session_Key2 = self.Generate_Session_Key(self.Q, self.Private_Key, self.OppoPublic_Key2)
                print("FINAL SESSION KEY2:",self.Session_Key2)
                
            elif Match_QA and not self.DoOnceAlice:
                self.Q, self.A = Match_QA.groups()
                self.Q = int(self.Q)
                self.A = int(self.A)
                self.Private_Key2 = random.randint(1, self.Q - 1)
                print("----TRANSFERED QA----")
                print("Recieved QA:", self.Q, self.A)
                print("Created PK: ", self.Private_Key2)
            
                self.Deff = Diffie_Hellman_Class(self.Q, self.A, self.Private_Key2)
                if self.Deff.Problem == "No Problem":
                    self.Public_Key = self.Deff.Generate_Public_Keys(self.Q, self.A, self.Private_Key2)
                    print("Public Key OLD: ", self.Public_Key)
                    # self.Public_Structure = "#pu"+str(self.Public_Key)
                    
                self.ReceivedQA = True
                self.DoOnceAlice = True
                
            elif Match_Method:
                self.Rec_Type = Match_Method.group(1)
                self.Enc_Key = Match_Method.group(2)
                
                self.Enc_Key = str(self.Enc_Key)
                
                self.Encryption_Box.set(self.Rec_Type)
                self.Encryption_Callback(self.Rec_Type)
                try:
                    self.KeyEntry.delete(0,"end")
                    self.KeyEntry.insert(self.Enc_Key)
                except Exception as e:
                    print(e)
                
                try:
                    self.KeyBox.delete("0.0","end")
                    self.KeyBox.insert(self.Enc_Key)
                except Exception as e:
                    print(e)
                    
                self.Set_Key()
                
            else:
                print("Received Encrypted:",self.Rec_Message,"\n")
                  
                if self.Rec_Type == "None" or not self.IsEncryption:
                    try:
                        self.textbox.insert("end", f"[Mina]:\n{self.Rec_Message}\n\n")
                    except:
                        pass
                elif self.Rec_Type == "Caesar":
                    Dec_Rec_Message = self.Caesar.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "Monoalphabetic":
                    Dec_Rec_Message = self.Mono.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "PlayFair":
                    Dec_Rec_Message = self.PlayFair.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "RailFence":
                    Dec_Rec_Message = self.RailFence.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "Row Transposition":
                    Dec_Rec_Message = self.RowTrans.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "Vigenere":
                    Dec_Rec_Message = self.Vigenere.decrypt(self.Rec_Message)
                    Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "DES":
                    Key_BN = ''.join(format(ord(char), '08b') for char in self.Enc_Key)
                    Dec_Rec_Message = self.EncDES.Decrypt(self.Rec_Message,Key_BN)
                    Dec_Rec_Message = self.EncDES.Remove_Padding(Dec_Rec_Message)
                    # Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Rec_Type == "RC4":
                    # Dec_Rec_Message = self.Fix_Spacing(Dec_Rec_Message, 2)
                    Dec_Rec_Message = self.RC4Zena.encrypt_and_decrypt(self.Rec_Message)
                    print("Received Decrypted:",Dec_Rec_Message,"\n\n")
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
            

            if not self.Rec_Message:
                break
                
           
    def set_name(self):
        self.logo_label.configure(text=self.Auth_Name)
        
    def Check_Credentials1(self, Ltype):
        
        self.WarningLabel = customtkinter.CTkLabel(Main, text="Missing Fields...", font=customtkinter.CTkFont(size=20, weight="bold"), fg_color="red")
        self.WarningLabel2 = customtkinter.CTkLabel(Main, text="Wrong Credentials", font=customtkinter.CTkFont(size=20, weight="bold"), fg_color="red")

        if Ltype == "text":
            if self.username_entry.get() == "" or self.password_entry.get() == "":
                print("Login Error\n\n")
                self.username_entry.configure(bg_color="red")
                self.password_entry.configure(bg_color="red")
                self.WarningLabel.place(x=Main.winfo_screenwidth()/2 - 510, y=Main.winfo_screenheight()/2 + 25, anchor="center")
                
            if self.username_entry.get() != "" and self.password_entry.get() != "":
                for user in self.Users:
                    username = self.username_entry.get()
                    password = self.password_entry.get()
                    if user["id"] == username and user["password"] == password:
                        self.Auth_Name = user["name"]
                        print('\n\n'"Login User:", self.Auth_Name,"\n\n")
                        self.start_chat = True
                        self.Get_Dashboard()
                        break
            else:
                self.WarningLabel2.place(x=Main.winfo_screenwidth()/2 - 510, y=Main.winfo_screenheight()/2 + 25, anchor="center")
        
        # self.Get_Dashboard()

    def GoBack_Home(self):
        self.DestroyAll()
        Main.geometry("700x580".format(self.ScreenWidth, self.ScreenHeight))
        self.Main_Screen()
        
    def Login_Page(self):
        self.DestroyAll()
        
        self.width = 900
        self.height = 600
        Main.geometry(f"{self.width}x{self.height}")
        Main.resizable(False, False)
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(self.current_path + "/Assets/bg1.jpg"),size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(Main, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.login_frame = customtkinter.CTkFrame(Main, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="ETE Chat\nLogin",
                                                  font=customtkinter.CTkFont("System",size=40, weight="bold"))
        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.login_image = customtkinter.CTkImage(Image.open(self.current_path + "\Assets\logo1.png"),size=(200, 200))
        self.login_img_Label = customtkinter.CTkLabel(self.login_frame, image=self.login_image,text = "")
        
        
        self.login_label.grid(row=0, column=0, padx=30, pady=(40, 20))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.login_img_Label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=lambda:self.Check_Credentials1("text"), width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

        self.Back_Btn = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:self.GoBack_Home())
        self.Back_Btn.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")


    def Main_Screen(self):
        self.DestroyAll()

        Main.title("ETE Chat App")
        Main.attributes("-topmost", True)

        self.ScreenWidth = Main.winfo_screenwidth()
        self.ScreenHeight = Main.winfo_screenheight()
        Main.geometry("700x580".format(self.ScreenWidth, self.ScreenHeight))

        self.WelcomeLabel = customtkinter.CTkLabel(Main, text="ETE Chat", font=("System", 40, "bold"))
        self.ContinueButton = customtkinter.CTkButton(Main, text="Continue", command=lambda: self.Continue(),  width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen")
        self.QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen")
        self.WelcomeLabel.place(x=self.ScreenWidth/2-610, y=self.ScreenHeight/2 - 450, anchor="center")
        self.ContinueButton.place(x=self.ScreenWidth/2 - 610, y=self.ScreenHeight/2 - 250, anchor="center")
        self.QuitButton.place(x=self.ScreenWidth/2 - 610, y=self.ScreenHeight/2 - 100, anchor="center")

gui = MainGUI()
gui_thread = threading.Thread(target=gui.Main_Screen)
gui_thread.start()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
# client_socket.connect(('192.168.1.8', 5000))

receive_thread = threading.Thread(target=gui.Recieve_Message)
# time.sleep(2)
receive_thread.daemon = True
receive_thread.start()

Main.mainloop()
