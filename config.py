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
SESSION_NAME = getenv("SESSION_NAME", "BQC4uxbF2in9YlvlxcIv8rE3ezY3FZDI9iWDQhtEfYOHNvq0M2N1ySt377DsF7rEa8rp6IynfUKSGSXj_Qhs7_X9ZB-fvCyIuiRfwijqZcEACJc9isTmQJ-N6DLEmew6dn76jfLJPJgS3cb3KcpVh_aK0OQgelwoD-U8DoaUTw-Ox4QAfd_sxyJ12s2Wkf_eY2scxTB4JYRWv9wGV9Q3cUWch969pguj-jGxsa19q8csUP9FUzGTYoYs6n4jsZipuUXEch-c5BBxhhGUQPCg6AgyLnjUsG-gk0msJTlRTkPbDjtt3yoSNFEtmc9wgZrfqrbgd6u3FmNLTVmvP16za9wLAAAAAUTDWqkA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
