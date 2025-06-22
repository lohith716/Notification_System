import socket
import threading
import ssl
import tkinter as tk
from tkinter import ttk
   
FORMAT = "utf-8"
nickname = input("Choose Your Nickname:")
port = 5566
CA_CERTF = "ssl-certificate.pem"

stop_thread = False

def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            elif message == 'STOP':
                stop_thread = True
                client.close()
                break
            else:
                update_chat_window(message)
        except socket.error:
            print('Error Occurred while Connecting')
            client.close()
            break

def write():
    while True:
        global stop_thread
        if stop_thread:
            break
        message = f'{input(">")}'
        client.send(message.encode(FORMAT))

def update_chat_window(message):
    chat_history_text.config(state=tk.NORMAL)
    chat_history_text.insert(tk.END, message + '\n')
    chat_history_text.config(state=tk.DISABLED)
    chat_history_text.see(tk.END) 

def connect_to_server():
    global client, receive_thread
    ip = ip_entry.get()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False 
    context.load_verify_locations(CA_CERTF)
    client = context.wrap_socket(client_socket, server_hostname=ip)
    try:
        client.connect((ip, port))
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        connect_button.config(state=tk.DISABLED)
    except Exception as e:
        print(f"Error connecting to server: {e}")

root = tk.Tk()
root.title("Chat Client")
root.geometry("400x300")

ip_entry = ttk.Entry(root, width=40)
ip_entry.pack(pady=10)
ip_entry.insert(tk.END, "127.0.0.1")  
connect_button = ttk.Button(root, text="Connect", command=connect_to_server)
connect_button.pack(pady=5)

chat_history_text = tk.Text(root, height=10, width=50)
chat_history_text.config(state=tk.DISABLED)
chat_history_text.pack(pady=10)
chat_scroll = ttk.Scrollbar(root, command=chat_history_text.yview)
chat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
chat_history_text.config(yscrollcommand=chat_scroll.set)

entry_field = ttk.Entry(root, width=40)
entry_field.pack(pady=5)
entry_field.focus_set()
send_button = ttk.Button(root, text="Send", command=lambda: send_message(entry_field.get()))
send_button.pack(pady=5)

def send_message(message):
    if message.strip(): 
        client.send(message.encode(FORMAT))
        entry_field.delete(0, tk.END)

root.mainloop()
