# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubts on Telegram @KingVJ01

import re
import os
from os import environ
from Script import script

# Regular expression for validating IDs
id_pattern = re.compile(r'^.\d+$')

# Function to check and convert environment variable values to boolean
def is_enabled(value, default=False):
    value = value.lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value in ["false", "no", "0", "disable", "n"]:
        return False
    return default

# Channel Authentication
AUTH_CHANNEL = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get('AUTH_CHANNEL', '-1002394633791').split()
]

# Bot Information
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Bot Start Picture(s)
PICS = environ.get('PICS', 'https://telegra.ph/file/f198e9233986d61549659.jpg').split()

# Admin Information
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get('ADMINS', '1029462448').split()
]
BOT_USERNAME = environ.get("BOT_USERNAME", "Anime_X_sharing_Bot")  # without @
PORT = environ.get("PORT", "8080")

# Clone Configuration
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "false"))
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Configuration
DB_URI = environ.get(
    "DB_URI",
    "mongodb+srv://totipa4210:xlWOaPYnIKXmAaEq@cluster0.zbd31.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = environ.get("DB_NAME", "Xeonfilestore01")

# Auto Delete Configuration
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "true"))
AUTO_DELETE = int(environ.get("AUTO_DELETE", "40"))  # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "2400"))  # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002243581329"))

# File Caption
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Public File Store Option
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "false"))

# Verification Configuration
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "true"))
SHORTLINK_URL = environ.get("SHORTLINK_URL", "yummyurl.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "5b8a506ee7f14be30c8a4dea951afaee8a340712")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/hentai_Hanime_Update_Channel/40")

# Website Mode
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "true"))
WEBSITE_URL = environ.get(
    "WEBSITE_URL",
    "https://www.personalurl.in.net/2025/03/kaise-le-personal-loan.html"
)

# File Stream Configuration
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "true"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://select-evanne-vishalwankhede123-bb083bcf.koyeb.app/")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubts on Telegram @KingVJ01
