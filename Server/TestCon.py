# client.py
import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

def send_message():
    message = entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            chat_box.insert(tk.END, f"{message}\n")
        except Exception as e:
            print(f"Error: {e}")
            break

def on_closing():
    client_socket.close()
    root.destroy()

root = tk.Tk()
root.title("Simple Chat App")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
