# @sarkari_student
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import importlib
from pyrogram import idle
from plugins import LOGGER, bot as app
from plugins.modules import ALL_MODULES
from plugins.modules.vsp import load_batches_on_start  # Import the function

async def _start():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("plugins.modules." + all_module)

    LOGGER.info(f"@{app.username} Started.")
    
    try:
        # Call load_batches_on_start to initialize scheduled batches
        await load_batches_on_start()
        LOGGER.info("Batches loaded and scheduled.")
    except Exception as e:
        LOGGER.error(f"Error during batch loading: {e}")

    await app.send_message(7653322737, f"**🟢नमस्ते मलिक ! हम जिंदा हो चुके हैं बताइए आपकी क्या आज्ञा है🙏🟠**")
    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(_start())
    finally:
        loop.close()
    LOGGER.info("Stopping bot")
