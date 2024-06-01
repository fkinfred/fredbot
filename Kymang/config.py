#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "17131033"))
API_HASH = os.environ.get("API_HASH", "7768488c115ac09684bb38e608c47997")
MONGO_URL = os.environ.get("MONGO_URL", "")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-100"))
BOT_ID = int(os.environ.get("BOT_ID", ""))

KITA = [int(x) for x in (os.environ.get("KITA", "1668766845").split())]
