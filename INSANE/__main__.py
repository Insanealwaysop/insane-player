import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from AdityaHalder.utilities import config
from AdityaHalder.utilities.config.config import BANNED_USERS
from AdityaHalder import app, bot, LOGGER
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.plugins import ALL_MODULES
from AdityaHalder.modules.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("insaneop").error(
            "š„ ššØ šš¬š¬š¢š¬š­šš§š­ šš„š¢šš§š­š¬ [ššš«š¬] ššØš®š§šā"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("šš§š¬šš§ššš©").warning(
            "š„ ššØ šš©šØš­š¢šš² ššš«š¬ šššš¢š§ššā...\nš· ššØš®š« ššØš­ ššØš§'š­ šš ššš„š ššØ šš„šš² šš©šØš­š¢šš² šš®šš«š¢šš¬ā..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("insaneop.plugins" + all_module)
    LOGGER("insaneop.modules.plugins").info(
        "š„ šš®ššš¬š¬šš®š„š„š² šš¦š©šØš«š­šš šš„š„ ššØšš®š„šš¬ šæ "
    )
    await app.start()
    await aditya.start()
    try:
        await aditya.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("šš§š¬šš§ššš©").error(
            "[šš«š«šØš«] - \n\nš„ šš„ššš¬š šš®š«š§ šš§ ššØš¢šš šš”šš­ šš ššØš®š« ššØš š šš« šš«šØš®š©ā..."
        )
        sys.exit()
    except:
        pass
    await aditya.decorators()
    LOGGER("šš§š¬šš§ššš©").info("š„³ ššØš§š š«šš­š®š„šš­š¢šØš§š¬, ššØš®š« ššØš­ šš®šššš¬š¬šš®š„š„š² ššš©š„šØš²šš āØ...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("insaneop").info("š šš²š¬š­šš¦ šš­šØš©š©šš, ššØšØššš²šā...")
