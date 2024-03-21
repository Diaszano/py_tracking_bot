from sys import stderr

from config.enviroments import LOG_LEVEl
from loguru import logger

logger.add(sink=stderr, level=LOG_LEVEl, enqueue=True)
logger.add("PyTrackingBot_{time}.log", enqueue=True, serialize=True)
