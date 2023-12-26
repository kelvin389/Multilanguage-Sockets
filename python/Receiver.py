import socket as s
import json
from TestObject import TestObject

HOST = "127.0.0.1"
PORT = 1234

def main():
    # open socket
    sock = s.socket()
    sock.bind((HOST, PORT))
    sock.listen()

    con, addr = sock.accept()
    print(f"binding to: {addr}")
    recieved_data = bytes()
    while True:
        data = con.recv(1024)
        if not data:
            break
        recieved_data += data
    con.close()
    sock.close()

    serialized_obj = json.loads(recieved_data)
    print("received object:")
    print(serialized_obj)

if __name__ == "__main__":
    main()