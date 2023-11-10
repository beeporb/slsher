import celery

from server.slsher.services.config import SLSHER_REDIS_URI

app = celery.Celery(
    broker=SLSHER_REDIS_URI + "/0",
    backend=SLSHER_REDIS_URI + "/1"
)