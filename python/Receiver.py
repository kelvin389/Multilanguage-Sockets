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
    received_data = bytes()
    while True:
        data = con.recv(1024)
        if not data:
            break
        received_data += data
    con.close()
    sock.close()
	
    unserialized_obj = json.loads(received_data)
    obj = TestObject(**unserialized_obj)
    print("received object:")
    print(obj)

if __name__ == "__main__":
    main()
