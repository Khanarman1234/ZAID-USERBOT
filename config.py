import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "80d223dd670503fa6f017359f328cfe3") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6753033991").split()))
OWNER_ID = int(getenv("OWNER_ID" ,"6753033991"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://minhazan990:minhaz@cluster0.r2okalv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "None")
ALIVE_PIC = getenv("ALIVE_PIC", 'None')
ALIVE_TEXT = getenv("ALIVE_TEXT", "hello")
PM_LOGGER = getenv("PM_LOGGER", "https://t.me/+4LY3zUaqV_szZTQ1")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/+4LY3zUaqV_szZTQ1")
GIT_TOKEN = getenv("GIT_TOKEN", "None") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Khanarman1234/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "None")
STRING_SESSION2 = getenv("STRING_SESSION2", "None")
STRING_SESSION3 = getenv("STRING_SESSION3", "None")
STRING_SESSION4 = getenv("STRING_SESSION4", "None")
STRING_SESSION5 = getenv("STRING_SESSION5", "None")
STRING_SESSION6 = getenv("STRING_SESSION6", "None")
STRING_SESSION7 = getenv("STRING_SESSION7", "None")
STRING_SESSION8 = getenv("STRING_SESSION8", "None")
STRING_SESSION9 = getenv("STRING_SESSION9", "None")
STRING_SESSION10 = getenv("STRING_SESSION10", "None")
