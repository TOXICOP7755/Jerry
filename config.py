from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16841147"))
API_HASH = getenv("API_HASH", "724367ca3534a7e37594fcf3512dc8ad")
BOT_TOKEN = getenv("BOT_TOKEN","5202259558:AAFaciT7JtNtLGb7CF5CKu5kGsY2rJZm1Bg")
BOT_NAME = getenv("BOT_NAME","꓅꒑ꋊ ℳɄƧꂑᏣ β๏꓅")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQBO-8Eb45YkqUn6d4tieDsIRQI-gNbZbnsNhaNpZYfGWjf8odtX4bzrztR_VW4lt-RmfF2DXHx8gJApoRZp1qyDW8SS80EN-dWQp9dshkMZY1sB8Y-vayoqHicE6CMiGGxrX3ODdzE1FeBn25eahJZkdEM2KElozkin-40iC1KtrgCBWlRHcp4sEfr2wVImCy_qbXNArHnrwJBXzqLs4lGQVRdVVR5xExGhjnk9KuHRztfV168a7OBdS0JwzaK9YIgQcsT35cfp0ACwgyACfVyTIvdVKEC1n4NbvioXQOKU7vM4kg34Vt7Y8sMBG3xSBe2fTztmSgr9NDasypPzyNxJAAAAATYcS3oA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607400360 5222883210").split()))
