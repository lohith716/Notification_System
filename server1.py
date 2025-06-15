import socket
import threading
import ssl

CERTF = "ssl-certificate.pem"
KEYF = "private-key.pem"

IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5566
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
CLIENTS = []
NICKNAME = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]}:{addr[1]} connected.")
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        index = CLIENTS.index((conn, addr))
        # print(len(CLIENTS), len(NICKNAME), NICKNAME, sep="\n")  # Remove this line
        if msg == DISCONNECT_MSG:
            conn.send("STOP".encode(FORMAT))
            removename = NICKNAME[index]
            NICKNAME.remove(removename)
            CLIENTS.remove((conn, addr))
            connected = False
            break
        if msg[:4] == "COMS":
            conn.send("COMS received".encode(FORMAT))
        if msg[:7] == "COMS WA":
            conn.send("COMS received".encode(FORMAT))
            sendindex = NICKNAME.index("WA")
            sendconn = CLIENTS[sendindex][0]
            sendconn.send(f"Specific Client connection from {NICKNAME[index]}".encode(FORMAT))

        print(f"[{addr[0]}:{addr[1]}] {msg}")
        msg = f"Msg received from {NICKNAME[index]}: {msg}"
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting ...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERTF, keyfile=KEYF)
    server = context.wrap_socket(server_socket, server_side=True)
    
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        conn.send("NICK".encode(FORMAT))
        nick = conn.recv(SIZE).decode(FORMAT)
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        thread.start()
        active_connections_count = threading.active_count() - 1
        print(f"[ACTIVE CONNECTIONS] {active_connections_count}")
        CLIENTS.append((conn, addr))
        NICKNAME.append(nick)
        print(NICKNAME)

if __name__ == "__main__":
    main()

















