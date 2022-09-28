## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCK6OEpAfLQ65YuqXjEHK4l6E_MdSRh-JHO2c7YhbteOYiAhtefIrwLOeoUJYu_MWmKgTsiz9NNFVtk0OHdp7DjPQSclF7PjwiPLSKcjxhaBtiDRqVR2CJBL0PhbPZZB_xWHF-dvXKDdhu4vNIJDSu_J9Byhx8dpRJh4b5N37JihEyc41bjXIonGTR5rIJqTBWyE9oTmuDxH_VfoleuaYEQXznjHb4ezl2PCAvLvzzlixOu7tlDVYhW8EJSWTnK0ez8U2CiTnwwdP7Wb3ym9LWg2HcA5_T72Mr5MNTTGG-377CeV5uaMdszX7cHXjo4xVM6A90N9u1c8f67w5vvjt1KAAAAAThX180A")
BOT_TOKEN = getenv("BOT_TOKEN""5791501037:AAFnwviJwYh4EEglueU5juKEW7CmIgaJH5E")
BOT_NAME = getenv("BOT_NAME"ShivuXmusic7x")
API_ID = int(getenv("API_ID", "15462970"))
API_HASH = getenv("API_HASH", "818af3b1235f9d87c53fd54e540c886f")
OWNER_NAME = getenv("OWNER_NAME", "Shivam")
ALIVE_NAME = getenv("ALIVE_NAME", "Queen")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Assistant_of_Shivu")
BOT_USERNAME = getenv("BOT_USERNAME""ShivuXmusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Queen")
GROUP_SUPPORT = getenv("GROUP_SUPPORT""https://t.me/disscussting")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL""https://t.me/techSquad7x")
SUDO_USERS = list(map(int, getenv("SUDO_USERS""1930739461").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
