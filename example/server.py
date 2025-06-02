from PoStandartu import Server
from PoStandartu.actions import Action
from PoStandartu.actions.special_actions import MatchAction, StaticAction
from PoStandartu.http_utils import Response, Request, RequestPattern


#Созадайте сервер, а потом декларативно опишите в нём пути
server = Server("127.0.0.1", 8080)

# Легко можно создавать пути
server.action("/hello", lambda request: Response(status_code=200, content="Hello, World!"))
# Даже с параметрами, которые автоматически будет спаршены из запроса пользователя
server.action("/hello?name=<name>", lambda request: Response(status_code=200, content=f"Hello, {request.params['name']}!"))


# Нужно раздать статику?
# Не беда, достаточно использовать встроенную утилиту, которая выполнит все за вас
# Просто создайте экшен, который будет использовать файлы в вашей папке static_path
import os
static_path = os.path.join(os.getcwd(), "example", "static")
server.actions.register_action(
    StaticAction(static_path=static_path)
)

# А что если ничего не подошло и ни один паттерн не сработал?
# И здесь PoStandartu не оставит вас в беде
# Используйте специальный экшен MatchAction. Он всегда вызовется вне зависимости от того, что запросил пользователь
# Очень удобно возвращать 404
server.actions.register_action(
    MatchAction(
        lambda request: Response(status_code=404, content="404 Not Found"))
)

# Всё. Можно запускать и ждать клиентиков. Всё будет хорошо работать, наверное
server.run()