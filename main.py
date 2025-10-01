#Code write by @sarkari_student
import os
from config import Config
from pyrogram import Client, idle
from pyrogram.enums import ChatMemberStatus, ChatMembersFilter
from pyrogram import enums
from pyrogram.types import ChatMember
import asyncio
import logging

from logging.handlers import RotatingFileHandler
#Code write by @sarkari_student

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)
#Code write by @sarkari_student
LOGGER = logging.getLogger(__name__)
LOGGER.info("live log streaming to telegram.")
#####################################################################
auth_users_str = os.environ.get('AUTH_USER', '7224758848')
auth_users_list = auth_users_str.split(',')
auth_users_int = [int(user_id) for user_id in auth_users_list]
AUTH_USERS = auth_users_int
print("AUTH_USERS:", AUTH_USERS)
#####################################################################
# Prefixes
prefixes = ["/", "~", "?", "!", "."]

# Client
plugins = dict(root="plugins")
# if __name__ == "__main__" :
# bot = Client(
#     "Bot",
#     bot_token=Config.BOT_TOKEN,
#     api_id=Config.API_ID,
#     api_hash=Config.API_HASH,
#     sleep_threshold=20,
#     plugins=plugins,
#     workers = 10,
# )


# bot.run()
# # bot_info  =bot.get_me()
# LOGGER.info(f"<---  Started (c)--->")
# idle()

# # asyncio.get_event_loop().run_until_complete(main())
# LOGGER.info(f"<---Bot Stopped-->")
