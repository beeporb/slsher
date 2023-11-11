import celery

from slsher.config import SLSHER_REDIS_URI

app = celery.Celery(broker=SLSHER_REDIS_URI + "/0",
                    backend=SLSHER_REDIS_URI + "/1")
app.conf.event_serializer = "pickle"
app.conf.task_serializer = "pickle"
app.conf.result_serializer = "pickle"
app.conf.accept_content = [
    "application/json", "application/x-python-serialize"
]
