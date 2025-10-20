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
BOT_TOKEN = getenv("BOT_TOKEN", "6798679157:AAEmY9jiypsA9GAzDIoevC3fKZGZ648N5R8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://i.ibb.co/n3BJsk5/0820ba3e-d1a4-484c-a8c8-7e9eecb1ceee.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "hello")
PM_LOGGER = getenv("PM_LOGGER", "the_rebel_princess_hindi_dubbed1")
LOG_GROUP = getenv("LOG_GROUP", "the_rebel_princess_hindi_dubbed1")
GIT_TOKEN = getenv("GIT_TOKEN", "None") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Khanarman1234/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFwyGEACndwqps5TVDWFEUBs4KcrZTXkwcBQLgfyJJ3_SQX-hhV_WP54fS7A_vnQ_I6Ek-_JpU08llj54x0aUHTUhMcy5XltRBfjJ-TTgZfLRctLHRKyumeDeF4O9kdUP3_PDcImgmNcTbmdIWCIzNfM-m-thQYVsbPgQWOKCF2DPz9jAcMkf-XAuUCINmJvHjQE5SK7VgdhvSFPUpdQ-t6R8Y5y8_GC2xXVnwOc7r5EBkz86VYLw3WbORPzjOPclc-YoVRmyU5u7xngtuKFrRLm8UC223Ofa2KeBlYLqw5KeucCoeem-CzDnerHS1Ask-DC8F7t8919jq9w0ewEmOri0HqegAAAAGZBrlyAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "None")
STRING_SESSION3 = getenv("STRING_SESSION3", "None")
STRING_SESSION4 = getenv("STRING_SESSION4", "None")
STRING_SESSION5 = getenv("STRING_SESSION5", "None")
STRING_SESSION6 = getenv("STRING_SESSION6", "None")
STRING_SESSION7 = getenv("STRING_SESSION7", "None")
STRING_SESSION8 = getenv("STRING_SESSION8", "None")
STRING_SESSION9 = getenv("STRING_SESSION9", "None")
STRING_SESSION10 = getenv("STRING_SESSION10", "None")
