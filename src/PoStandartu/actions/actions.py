class Actions():
    def __init__(self):
        self.actions = []

    def register_action(self, action):
        self.actions.append(action)

    def run_action(self, request):
        for action in self.actions:
            if action.match(request):
                return action.action(request)