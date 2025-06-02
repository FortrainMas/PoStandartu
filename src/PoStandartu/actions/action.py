from PoStandartu.http_utils import RequestPattern

class Action:
    def __init__(self, pattern, action):
        self.pattern = RequestPattern.create(pattern)
        self.action = action
    
    def match(self, request):
        return self.pattern.match(request)