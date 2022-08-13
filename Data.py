from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
✘ ᴅᴇᴀʀ {}
‣ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʙᴏᴛ {}
‣ ʏᴏᴜ ᴄᴀɴ ᴇxᴛʀᴀᴄᴛ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ
‣ ʙɪɢʀᴀᴍ ᴄᴏᴅᴇ
‣ ᴛʀɪᴍɪx ᴄᴏᴅᴇ
‣ ᴛʜᴇ ʀᴏʙᴏᴛ ᴡᴏʀᴋᴤ ᴠᴇʀʏ ᴡᴇʟʟ
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌐 ¦ اضـغـط لـبـدا استـخـراج جلسة", callback_data="generate")],
        [InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="ʜᴏᴍᴇ")]
    ]

    generate_button = [
        [InlineKeyboardButton("🌐 ¦ اضـغـط لـبـدا استـخـراج جلسة", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("🗣 ¦ الـدعـم الـفـنـي", url="https://t.me/Y_408")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌐 ¦ اضـغـط لـبـدا استـخـراج جلسة", callback_data="generate")],
        [InlineKeyboardButton("⚙¦الــســورس", url="https://t.me/TELEMEX")],
        [
            InlineKeyboardButton("❓¦طـريـقـه الاسـتـخـدام", callback_data="help"),
            InlineKeyboardButton("💾¦مـعـلومـات", callback_data="about")
        ],
        [InlineKeyboardButton("🔮¦مـالـك الـبـوت", url="https://t.me/Y_408")],
    ]

    # Help Message
    Help = """
» قم بارسال /generate ثم اضغط علي بدء استخراج كود الجلسه!
» قم باختيار النوع الذي تريده; [البايروكرام/تليثون - كود تريمكس]
» ثم قم بارسال الاشياء المطلوبه للحصول علي الكود في الرسائل المحفوظة.
"""

    # About Message
    ABOUT = """
‍ **💾¦مـعـلومـات** 

⚡¦بـوت استخـراج كـود تيرمكـس خـاص بســورس التليـثون وكــود بـايــروجـرام خـاص بـسـورس الـمـيـوزك🎶

🌀¦قـنـاه الـبـوت : (t.me/TELEMEX)
🌏¦اللـغــه(www.python.org/)

👨🏼‍💻¦الـمـبـرمــج(t.me/Y_408)
"""
