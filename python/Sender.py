import socket as s
import json
from dataclasses import asdict
from TestObject import TestObject

HOST = "127.0.0.1"
PORT = 1234

def main():
    obj = TestObject(12345, "Hello World from Python!")
    obj_dict = asdict(obj)
    serialized_obj_str = json.dumps(obj_dict)
    serialized_obj = bytes(serialized_obj_str, "utf-8")

    # open socket
    sock = s.socket()
    sock.connect((HOST, PORT))

    print("sending object:")
    print(obj)
    sock.sendall(serialized_obj)
    sock.close()

if __name__ == "__main__":
    main()
