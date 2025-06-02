class MatchAction:
    def __init__(self, action):
        self.action = action
    def match(self, request):
        return True
    def action(self, request):
        return self.action