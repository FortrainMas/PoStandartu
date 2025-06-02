from PoStandartu.http_utils import Request

class Action:
    def __init__(self, pattern, action):
        self.pattern = Request(pattern)
        self.action = action
    
    def match(self, request):
        return self.pattern.match(request)