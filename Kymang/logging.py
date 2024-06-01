import logging
from os import execvp
from sys import executable
import os

class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSError"]:
            if X in record.getMessage():
                execvp(executable, [executable, "-m", "Kymang"])


logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)


logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
