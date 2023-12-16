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

sys.path.append('Encryptions/Single-Key/Classical')
from Caesar import caesar
sys.path.append('Encryptions/Dual-Key/RSA')
from edRSA import RSA_KeyGen

User_Logo = customtkinter.CTkImage(light_image=Image.open("Assets/person.png"),
                                  size=(100, 100))

Main = customtkinter.CTk()

class MainGUI:
    def __init__(self):
        self.Main = Main
        self.start_chat = False
        self.LineCt = 0
        self.IsEncryption = False
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
        
        self.Profile_Button = customtkinter.CTkButton(self.sidebar_frame, text="Profile")
        self.Profile_Button.grid(row=2, column=0, padx=20, pady=10)
 
        self.Encryption_Box = customtkinter.CTkComboBox(self.sidebar_frame,
        values=["DES", "AES", "RSA", "RC4", "El Gammal", "Caesar", "Monoalphabetic","PlayFair","RailFence","Row Transposition", "Vigenere", "None"],command=self.Encryption_Callback)
        self.Encryption_Box.grid(row=3, column=0, padx=20, pady=(0, 0))
        self.Encryption_Box.set("Choose Encryption")
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_options = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_options.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        self.exit_button = customtkinter.CTkButton(self.sidebar_frame, text="Exit", hover_color="Red", command=self.Exit)
        self.exit_button.grid(row=7, column=0, padx=20, pady=10)
        
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

    def Encryption_Callback(self,Type):
        print("Encryption Type: ", Type)
        if Type == "Caesar":
            self.IsEncryption = True
            self.KeyEntry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Key")
            self.KeyEntry.grid(row=4, column=0, padx=(0, 0), pady=(5, 5), sticky="nsew")
            
            self.Set_Key_Button = customtkinter.CTkButton(self.sidebar_frame, text="Set", fg_color="transparent", border_width=2,
                                                    text_color=("gray10", "#DCE4EE"), command=self.Set_Key(Type))
            self.Set_Key_Button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
            # self.Caesar = caesar()
        return Type
    
    def Set_Key(self,Type):
        if Type == "None" or Type == "Choose Encryption":
            self.IsEncryption = False
            print("NO ENCRYPTION")
        elif Type == "Caesar":
            self.IsEncryption = True
            try:
                if self.KeyEntry.get():
                    key = int(self.KeyEntry.get())
                    if 0 <= key <= 26:
                        self.Caesar = caesar(key)
            except ValueError:
                print("Caesar Failed")
                pass
                

        
    def Send_Message(self):
        Send_Message = self.entry.get()
        if Send_Message:
            # self.textbox.configure(state="normal")
            if self.Encryption_Callback == "None" or not self.IsEncryption:
                self.IsEncryption = False
                client_socket.send(Send_Message.encode('utf-8'))
            if self.Encryption_Callback == "Caesar":
                Encrypted_Message = self.Caesar.encrypt(Send_Message)
                client_socket.send(Encrypted_Message.encode('utf-8'))
            elif self.Encryption_Callback == "DES":
                print("DES")
                # encrypted_message = DES.encrypt(Send_Message)
            elif self.Encryption_Callback == "AES":
                print("AES")
            elif self.Encryption_Callback == "RSA":
                print("RSA")
                Send_Message = self.Rsa_KeyGen.key_generation(1024)
                
            
            self.entry.delete(0, len(Send_Message))
            self.textbox.insert("end", f"[{self.Auth_Name}]:\n{Send_Message}\n\n")
            # self.textbox.configure(state="disabled")
        
            detailed_message = self.tabview.get() + "--" + Send_Message
            
    def Recieve_Message(self):
        while True:
            try:
                Rec_Message = client_socket.recv(1024).decode('utf-8')
                
                if self.Encryption_Callback == "None" or not self.IsEncryption:
                    self.textbox.insert("end", f"[Mina]:\n{Rec_Message}\n\n")
                if self.Encryption_Callback == "Caesar":
                    Dec_Rec_Message = self.Caesar.decrypt(Rec_Message)
                    self.textbox.insert("end", f"[Mina]:\n{Dec_Rec_Message}\n\n")
                elif self.Encryption_Callback == "DES":
                    print("DES")
                    # encrypted_message = DES.encrypt(Send_Message)
                elif self.Encryption_Callback == "AES":
                    print("AES")
                elif self.Encryption_Callback == "RSA":
                    print("RSA")
                    Send_Message = self.Rsa_KeyGen.key_generation(1024)   
                     
                if not Rec_Message:
                    break


            except Exception as e:
                print(f"Receiving Message Error: {e}")
                break
           
    def set_name(self):
        self.logo_label.configure(text=self.Auth_Name)
        
    def Check_Credentials1(self, Ltype):
        
        self.WarningLabel = customtkinter.CTkLabel(Main, text="Missing Fields...", font=customtkinter.CTkFont(size=20, weight="bold"), fg_color="red")
        self.WarningLabel2 = customtkinter.CTkLabel(Main, text="Wrong Credentials", font=customtkinter.CTkFont(size=20, weight="bold"), fg_color="red")

        if Ltype == "text":
            if self.username_entry.get() == "" or self.password_entry.get() == "":
                print("NOT ACCEPTED")
                self.username_entry.configure(bg_color="red")
                self.password_entry.configure(bg_color="red")
                self.WarningLabel.place(x=Main.winfo_screenwidth()/2 - 510, y=Main.winfo_screenheight()/2 + 25, anchor="center")
                
            if self.username_entry.get() != "" and self.password_entry.get() != "":
                for user in self.Users:
                    username = self.username_entry.get()
                    password = self.password_entry.get()
                    if user["id"] == username and user["password"] == password:
                        self.Auth_Name = user["name"]
                        print("Login User:", self.Auth_Name)
                        self.start_chat = True
                        self.Get_Dashboard()
                        break
            else:
                self.WarningLabel2.place(x=Main.winfo_screenwidth()/2 - 510, y=Main.winfo_screenheight()/2 + 25, anchor="center")


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

receive_thread = threading.Thread(target=gui.Recieve_Message)
receive_thread.start()

Main.mainloop()
