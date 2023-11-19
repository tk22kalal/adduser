import os
import logging
from logging.handlers import RotatingFileHandler

SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID", ""))

DESTINATION_CHANNEL_ID = int(os.environ.get("DESTINATION_CHANNEL_ID", ""))

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nIT IS OFFICIAL BOT OF PAVOLADDER AND TERALADDER LINK GENERATOR OWNER.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(1447438514)
