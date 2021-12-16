from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app as Bot 
from TamilBots import  LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db


START_TEXT = """ Hai {}, 
Iam a song download Bot 🙂
"""

CMDS_TEXT = """
Hey {} This are this bots power🌠
"""

ABOUT_TEXT = """
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ 𝐀𝐁𝐎𝐔𝐓 ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║ 𝙈𝙔𝙉𝘼𝙈𝙀-𝐌𝐀𝐊𝐑𝐈_𝐒𝐎𝐍𝐆𝐁𝐎𝐓 
║┣⪼𝓓𝓮𝓿𝓸𝓵𝓸𝓹𝓮𝓻 -[𝐌𝐀𝐊𝐑𝐈](https://t.me/blesson_3)
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - [𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼](https://pyrogram.org)
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - [𝙿𝚈𝚃𝙷𝙾𝙽 𝟹](https://python.org)
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  [𝙷𝙴𝚁𝙾𝙺𝚄](https://heroku.com)
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪
"""
MUSIC = """ **🎧MUSIC**
You can also use this feature in group too
➩ /music <songname artist(optional)>: uploads the song in it's best quality available
You can also use these commands
➩/song
➩/s
➩/m
"""
 
VSONG = """ **📀VSONG📀**
You can also use this feature in group too
➩ /vsong <songname artist(optional)>: uploads the video song in it's best quality available
➩ /video <songname artist(optional)>: uploads the video song in it's best quality available
"""
  
LYRICS = """ **🎶LYRICS🎶**
You can also use this feature in group too
➩ /lyrics <songname>: uploads the lyrics of song
"""

YOUTUBE = """  **📽️YOUTUBE📽️**
You can also use this feature in group too
➩ /ytaudio <youtubelink>: uploads the audio of song in it's best quality available
➩ /ytvideo <youtubelink>: uploads the video of song in it's best quality available
you can also use inline for search YouTube video or song
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support📕', url=f"https://telegram.me/{Config.SUPPORT}"), 
        InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton('HELPℹ️', callback_data ='cmds'),        
        InlineKeyboardButton('ABOUT😁', callback_data='about')        
        ]]
    )
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎧MUSIC🎧', callback_data='song'),
        InlineKeyboardButton('📀VSONG📀', callback_data='video')
        ],[
        InlineKeyboardButton('🎶LYRICS🎶', callback_data='lyrics'),
        InlineKeyboardButton('📽️YOUTUBE📽️', callback_data='youtube')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),            
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )
MUSIC_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
SOURCE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='about')
        ]]
    )
YOUTUBE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat=""),
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
VSONG_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
LYRICS_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
        
@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.mention),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "song":
        await update.message.edit_text(
            text=MUSIC,
            reply_markup=MUSIC_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "video":
        await update.message.edit_text(
            text=VSONG,
            reply_markup=VSONG_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "lyrics":
        await update.message.edit_text(
            text=LYRICS,
            reply_markup=LYRICS_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "youtube":
        await update.message.edit_text(
            text=YOUTUBE,
            reply_markup=YOUTUBE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()




        
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):    
    await update.reply_photo(
        photo="https://telegra.ph/file/a9522ca5294a086a5dbe8.jpg",
        caption=START_TEXT.format(update.from_user.mention),            
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/a9522ca5294a086a5dbe8.jpg",
        caption=ABOUT_TEXT,        
        reply_markup=ABOUT_BUTTONS
    )

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
