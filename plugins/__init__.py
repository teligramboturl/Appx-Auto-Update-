from config import Config
import logging

from pyrogram import Client


logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

LOGGER = logging.getLogger(__name__)


class bot(Client):
    def __init__(self):
        super().__init__(
            name="lecture-bot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            in_memory=True,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


bot = bot()
