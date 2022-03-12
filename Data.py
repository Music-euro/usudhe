from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
هاي {}

مرحبا بك في بوت {}

يمكنك استخراج في هذا البوت استخراج كود pyrogram او telethon بكل سهوله وامان
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚜ بدء استخراج كود الجلسه ⚜", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 بدء استخراج كود الجلسه 🔥", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("⚜ الدعم الفني ⚜", url="https://t.me/MACS36")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 بدء استخراج كود الجلسه 🔥", callback_data="generate")],
        [InlineKeyboardButton("👨‍💻 قناتي 👨‍💻", url="https://t.me/MACS37")],
        [
            InlineKeyboardButton("طريقه الاستخدام ❔", callback_data="help"),
            InlineKeyboardButton(" حول", callback_data="about")
        ],
        [InlineKeyboardButton("📁 لشراء ملف البوت 📁", url="https://t.me/MACS31")],
        [InlineKeyboardButton("لتنصيب تليثون على حسابك", url="https://t.me/z_0_2")],
    ]

    # Help Message
    HELP = """
» قم بارسال /generate ثم اضغط علي بدء استخراج كود الجلسه!
» قم باختيار النوع الذي تريده; [البايروكرام/تليثون - كود تريمكس]
» ثم قم بارسال الاشياء المطلوبه للحصول علي الكود في الرسائل المحفوظة.
"""

    # About Message
    ABOUT = """
👨‍💻 **معلوماتي** 

روبوت برقية لإنشاء جلسة بيروجرام وسلسلة تيليثون...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
            **قناتي ~ **@MACS37
"""
