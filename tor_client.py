import socket
import json

class TorClient:
    def __init__(self, host="127.0.0.1", port=9050):
        self.host = host
        self.port = port

    def send_message(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(json.dumps(data).encode())

    def receive_message(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, _ = s.accept()
            with conn:
                data = conn.recv(1024)
                return json.loads(data.decode())