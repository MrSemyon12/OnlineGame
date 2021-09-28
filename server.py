import socket
from _thread import *
import sys

server = "192.168.0.11"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Server started, waiting for a connection")


def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break

            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break


while True:
    connection, address = s.accept()
    print("Connected to: ", address)

    start_new_thread(threaded_client, (connection,))

