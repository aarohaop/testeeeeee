import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "23048198")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "3398a27e9a0c3d60657b2d7d45f31a37") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7163612647:AAFpZ3iSUfv8TZFpKd50-N5RRgN-2z7DWmM") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else [] #Keep thia empty otherwise bot will not work for owner.
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aaroha:aaroha@cluster0.xfupmjy.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "5886772061")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5886772061)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002255639714")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "GreyMattersTech") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/19eeb26fa2ce58765917a.jpg') # image when someone hit /start
LINK_BYPASS = "True" 
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""
