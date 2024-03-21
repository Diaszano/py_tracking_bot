from sys import stderr

try:
    from config.enviroments import LOG_LEVEl
except ImportError:
    from ..config.enviroments import LOG_LEVEl
from loguru import logger

logger.add(sink=stderr, level=LOG_LEVEl, enqueue=True)
logger.add('PyTrackingBot_{time}.log', enqueue=True, serialize=True)
