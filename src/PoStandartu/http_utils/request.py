class Request:
    def __init__(self, text):
        self.text = text
        request_line = text.split("\r\n")[0]
        method, path, version = request_line.split()
        self.method = method
        self.path = path
        self.version = version
        self.path, self.params = Request.parse_url(path)
        self.path_params = self.path.split('/')[1:]

    def match(self, request):
        this_keys = set(self.params.keys())
        other_keys = set(request.params.keys())
        return self.path == request.path and this_keys == other_keys
        
    @staticmethod
    def parse_url(url):
        if '?' in url:
            path, query_string = url.split('?', 1)
        else:
            path, query_string = url, ''

        params = {}
        if query_string:
            for pair in query_string.split('&'):
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    params[key] = value
                else:
                    params[pair] = None

        return path, params
    

class RequestPattern:
    @staticmethod
    def create(text):
        return Request(f"GET {text} HTTP/1.1\r\n\r\n")
