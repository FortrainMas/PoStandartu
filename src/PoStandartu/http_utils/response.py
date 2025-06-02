class Response:
    def __init__(self, status_code=200, content="", headers={}):
        self.status_code = status_code
        self.content = content
        self.headers = headers
    
    def encode(self):
        reason = {
            200: "OK",
            404: "Not Found",
            500: "Internal Server Error"
        }.get(self.status_code, "Unknown")

        body = self.content.encode('utf-8')
        self.headers.setdefault("Content-Length", str(len(body)))
        self.headers.setdefault("Content-Type", "text/plain; charset=utf-8")

        response_line = f"HTTP/1.1 {self.status_code} {reason}\r\n"
        header_lines = ''.join(f"{k}: {v}\r\n" for k, v in self.headers.items())
        return (response_line + header_lines + "\r\n").encode('utf-8') + body
