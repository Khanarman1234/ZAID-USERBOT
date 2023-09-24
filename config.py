import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6516561672").split()))
OWNER_ID = int(getenv("OWNER_ID" ,"6516561672"))
MONGO_URL = getenv("MONGO_URL", "None")
BOT_TOKEN = getenv("BOT_TOKEN", "6689017907:AAGvzvyYdRC_71p4PTlYKGEv6Jg9TNe4Bps")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "hello")
PM_LOGGER = getenv("PM_LOGGER", "the_rebel_princess_hindi_dubbed1")
LOG_GROUP = getenv("LOG_GROUP", "the_rebel_princess_hindi_dubbed1")
GIT_TOKEN = getenv("GIT_TOKEN", "None") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCPOD2gQoFVcRJ0Q3QNS36-zzu1nLMwKBqXvu2-iAE5mMLypfcBccWCQr8FIhxKcRqydw5t0M0rkzm88k3xPWZeuRcb8X-kYJPvESRBQocg4rr_PouyCYO_MyYi4tC8BKlvcpnLyRnsi-Wc0t4cbwBBud39rZFPfEsXXDabRdt034QC8IMU9I8IhS3BM_0OXdsp-xUDJaRRuQfEcscURZMXG-z_Y0an7HzvCMiqrjBROmqJfJXu8RZc4mfyLVvogTrbvi1B3hgQTPxm48O_T3Jgq0NUblD368jOBgQQT3m6fPBu7GN7iVNAvZ0N777isCdYwYteZt-52FeedyZPyOMAAAAAAYRq1wgA")
STRING_SESSION2 = getenv("STRING_SESSION2", "None")
STRING_SESSION3 = getenv("STRING_SESSION3", "None")
STRING_SESSION4 = getenv("STRING_SESSION4", "None")
STRING_SESSION5 = getenv("STRING_SESSION5", "None")
STRING_SESSION6 = getenv("STRING_SESSION6", "None")
STRING_SESSION7 = getenv("STRING_SESSION7", "None")
STRING_SESSION8 = getenv("STRING_SESSION8", "None")
STRING_SESSION9 = getenv("STRING_SESSION9", "None")
STRING_SESSION10 = getenv("STRING_SESSION10", "None")
