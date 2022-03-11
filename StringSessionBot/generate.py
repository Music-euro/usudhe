from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "وجه الفتاة! حدث استثناء! \n \n ** خطأ **: {} "\
            "\n \n الرجاء إعادة توجيه هذا إلى @MACS37 إذا كانت هذه الرسالة لا تحتوي على أي"\n
            "معلومات حساسة وللمعلومات الخاصة بك


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(
        "برجاء اختيار نوع الجلسه الذي تريدها ",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("البايروكرام", callback_data="pyrogram"),
            InlineKeyboardButton("التليثون", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply("جارٍ بدء {} إنشاء الجلسة ...".format("Telethon" if telethon else "Pyrogram"))
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'برجاء ارسال `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('ليس API_ID صالحًا (والذي يجب أن يكون عددًا صحيحًا). يرجى البدء في إنشاء الجلسة مرة أخرى.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'برجاء ارسال `API_HASH`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(user_id, 'والان ارسل  `رقم هاتفك` سوف نرسل لك كود تحقق. \nمثال : `+917936482542`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("جاري ارسال رمز OTP...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` و "API_HASH" غير صالحين. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` غير صالح. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "برجاء إرسال رمز OTP المرسل الي حسابك. الرمز يكون بهذا . \nالتنسيق ~ `12345`, **يجب ارسل الرمز هكذا** `1 2 3 4 5`.", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply('بلغ الحد الزمني 10 دقائق. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP غير صالح. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('انتهت صلاحية كلمة المرور لمرة واحدة. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'حسابك محمي بخاصية التحقق بخطوتين . برجاء ارسال الباسورد.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('بلغ الحد الزمني 5 دقائق. يرجى البدء في إنشاء الجلسة مرة أخرى.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('أدخلت كلمة مرور غير صالحة. يرجى البدء في إنشاء الجلسة مرة أخرى.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
        try:
            await client(JoinChannelRequest("@MACS37"))
            await client(LeaveChannelRequest("@MACS37"))
            await client(LeaveChannelRequest("@MACS36"))
        except BaseException:
            pass
    else:
        string_session = await client.export_session_string()
    L_PIC = "https://telegra.ph/file/e4b35c210743a74277fef.jpg"
    if telethon:
        await client.send_file("me", L_PIC, caption="**{} - @MACS37 ** \n\n`{}`\n\n• __لا تشارك جلسة السلسلة مع أي شخص__\n• __لا تدعو أي شخص إلى Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
    else:
        await client.send_message("me", "**{} ~ @MACS37** \n\n`{sweetie}` \n\n• __لا تشارك جلسة السلسلة مع أي شخص__\n• __لا تدعو أي شخص إلى Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
    await client.disconnect()
    await phone_code_msg.reply("تم استخراج الكود بنجاح {} \n\nبرجاء مراجعة الرسائل المحفوظة لديك!".format("TELETHON" if telethon else "PYROGRAM"), reply_markup=InlineKeyboardMarkup(Data.support_button))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("لغيت العملية!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("اعادة تشغيل البوت!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("ألغيت عملية التوليد!", quote=True)
        return True
    else:
        return False
