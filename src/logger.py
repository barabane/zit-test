import logging
from src.config import settings


logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)

console_handler = logging.StreamHandler()
console_handler.setLevel(settings.LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def get_logger():
    return logger