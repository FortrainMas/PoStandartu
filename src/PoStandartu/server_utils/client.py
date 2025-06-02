import selectors

from PoStandartu.http_utils import Request

class Client:
    def __init__(self, sock, server):
        self.sock = sock
        self.sock.setblocking(False)
        self.recv_buffer = b""
        self.send_buffer = b""
        self.request = None
        self.response = None
        self.server = server
        self.selector = self.server.selector
    
    def read(self):
        try:
            data = self.sock.recv(4096)
            if not data:
                self.destroy()
            self.recv_buffer += data

            if b"\r\n\r\n" in self.recv_buffer:
                headers, _ = self.recv_buffer.split(b"\r\n\r\n", 1)
                self.request = Request(headers.decode())
                response = self.server.actions.run_action(self)
                self.send_buffer = response.encode()
                self.selector.register(self.sock, selectors.EVENT_WRITE, data=self)
        except ConnectionResetError:
            self.destroy()
        return None
    
    def write(self):
        if self.send_buffer:
            sent = self.sock.send(self.send_buffer)
            self.send_buffer = self.send_buffer[sent:]
        return len(self.send_buffer) == 0
    
    def destroy(self):
        self.selector.unregister(self.sock)
        self.sock.close()