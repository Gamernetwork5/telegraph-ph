import re, os, time
from dotenv import load_dotenv
load_dotenv("config.env")
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyrogram client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config get this from mongodb
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","") 
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    #the channel which need to force subscribed, channel username without @
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    #the log channel id must start in -100 this channel will be were the bot send logs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration
    #if your bot is web required give True or else False
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
    #the interval time to ping server
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "120"))
    #if your bot is running with web cmd pls copy the web link to ping server not down in 1 minutes
    PING_WEB = os.environ.get("PING_WEB", "") 
