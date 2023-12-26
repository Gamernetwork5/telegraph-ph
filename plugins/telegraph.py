import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file, Telegraph

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")


@Client.on_message(filters.media & filters.private)
async def getmedia(bot, update):
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    try:
        message = await update.reply(
            text="`Uploading...`",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        print(error)
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('More Help', url='https://t.me/TGBotsCode')
            ]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"**Link :-** `https://graph.org{response[0]}`\n\n**Join :-** @TGBotsCode"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Open Link", url=f"https://graph.org{response[0]}"),
        InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
        ]]
    )
    await message.edit_text(
        text=text,
        disable_web_page_preview=False,
        reply_markup=reply_markup
    )

@Client.on_message(filters.text & filters.private)
async def text_handler(bot, update):
    """Creating instant view link
       by creating post in telegra.ph 
       and sending photo link to user"""

    try:
        telegraph = Telegraph()
        new_user = telegraph.create_account(short_name='1337')
        auth_url = new_user["auth_url"]
        title = update.from_user.first_name
        content = update.text
        if '|' in update.text:
            content, title = update.text.split('|')
        content = content.replace("\n", "<br>")
        author_url = f'https://telegram.dog/{update.from_user.username}' if update.from_user.id else None

        try:
            response = Telegraph().create_page(
                title=title,
                html_content=content,
                author_name=str(update.from_user.first_name),
                author_url=author_url
            )
        except Exception as e:
            print(e)
        await m.reply_text("https://graph.org/{}".format(response["path"]))

    except:
        pass
