import socket
import selectors

from .client import Client

class ServerSocket:
    def __init__(self, host, port, server):
        self.host = host
        self.port = port
        self.server = server
        self.selector = self.server.selector
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.server_socket.setblocking(False)
        self.selector.register(self.server_socket, selectors.EVENT_READ, data=None)
    
    def accept(self):
        conn, addr = self.server_socket.accept()
        print(f"Accepted connection from {addr}")
        conn_obj = Client(conn, self.server)
        self.selector.register(conn, selectors.EVENT_READ, data=conn_obj)

