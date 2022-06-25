from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN","5583584098:AAHkB6C2oca5NAWTnAIQShJVs7bFmP8kHWE")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "AQCBQ0foPS3LItkuMBcYDOwUrSrcmmjPXL2txIPLrlUvlWAr-6Bvh19Srsey7XQswb4wgEH4UYIGGfMH17itAonFo9uoL8JFNO41xqpM1wI1KOpvezymtORzfs536eC2CHTHKi-v2KjdJtIV2pIErRpFOxy-xu8zxH519XgEV3ErWhNgGZASo0U97qGq0JaUO1oE4DHRVtiGghEw_2ExXxXTAVf5AyVQswrGaUMVmP2VFSiq0ytgyBo0fvKxg5twJTYlO34ksBwVu_n7VoGIdVFaiJdukF9fWtBd8JhXGP9_6hWTAvS8lIFeByCuNwjMIkPrk8pZJM0nm930jbiGuUjbAAAAAUgRtYEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
