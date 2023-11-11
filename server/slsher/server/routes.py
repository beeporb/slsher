from slsher.server.api import api


@api.get("/")
def index() -> str:
    return "Hello World - this is slsher."
