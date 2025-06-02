import socket
import selectors
from PoStandartu.server_utils import ServerSocket
from PoStandartu.actions import Actions, Action

HOST, PORT = '127.0.0.1', 8080


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.selector = selectors.DefaultSelector()
        self.actions = Actions()
    def action(self, pattern, action):
        self.actions.register_action(Action(pattern, action))
    def run(self):
        server_socket = ServerSocket(HOST, PORT, self)
        print(f"Serving on http://{HOST}:{PORT}")

        try:
            while True:
                events = self.selector.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        server_socket.accept()
                    elif mask & selectors.EVENT_READ:
                        conn_obj = key.data
                        conn_obj.read()
                    else:
                        conn_obj = key.data
                        conn_obj.write()
        except KeyboardInterrupt:
            print("Shutting down.")
        finally:
            self.selector.close()