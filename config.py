from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN","5583584098:AAH8GrxqqdwnkCKALmTYONkEJQU98j_OYiQ")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "AQBQFOp8vQcY_1G6QCThL06LpRrPgi7ZaJtHw67_PKmAEuVKHqzzkqFThXpQpMaJKWjcyShNicSg3MkUQQ9pJxgxlJWnQfwSkAv3tlH8cYraFrOhhQ3bZbb0sMHQueGPmjvhpAR9PMKOnPbtc-PI_Tdbm6IjC7pWSm-16HQmVUzTkm8N-7oEq6m1wubqrJbd8Y5EDYpWsnBEkHH5CLw3zVdHznfMhCOLPqOSuh784kM9v8oLkhFWCg3qKnru44Q-DRC4NVAwjY_vb5D0tj524GEu6PNyVCAxI3OmbsiLm8vGjAr1wY-jgYnh-7KFQkctCOt_62MjjLjQZ6DHqrQBZFouAAAAATGMW3kA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
