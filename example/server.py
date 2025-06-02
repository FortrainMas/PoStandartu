from PoStandartu import Server
from PoStandartu.actions import Action
from PoStandartu.actions.special_actions import MatchAction, StaticAction
from PoStandartu.http_utils import Response, Request, RequestPattern

import os
static_path = os.path.join(os.getcwd(), "example", "static")
print(f"Static is searched in {static_path}")

server = Server("127.0.0.1", 8080)

server.actions.register_action(
    Action("/hello", lambda request: Response(status_code=200, content="Hello, World!"))
)
server.actions.register_action(
    Action("/hello?name=<name>", lambda request: Response(status_code=200, content=f"Hello, {request.params['name']}!"))
)
server.actions.register_action(
    StaticAction(static_path=static_path)
)
server.actions.register_action(
    MatchAction(
        lambda request: Response(status_code=404, content="404 Not Found"))
)

server.run()