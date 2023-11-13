#----------------- Inauguration --------------------#



#--------------------- module ------------------------#
from config import Config 
import threading
import os
import json
from zekalb import *
from telethon import TelegramClient, events
from datetime import datetime
import time
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup
from telethon import events
from telethon.tl.custom import Button
from telethon import events, Button
import asyncio
import pyfiglet
from telethon import functions, types
from telethon.tl.custom import Conversation
from telethon.errors import ChatWriteForbiddenError, UserIsBlockedError
import asyncio


#------------------------ vars -------------------------#
# -
# - ZE TEAM 
# -

A = '\033[1;34m'#ازرق
X = '\033[1;33m' #اصفر


#logo
logo = pyfiglet.figlet_format('*      ze      *')
print(X+logo)
print('  ')
print(A+'═'*60)
print('  ')

filename = 'ze.json'


print(A+'═'*60)
bot = TelegramClient('bot', api_id=Config.APP_ID, api_hash=Config.API_HASH).start(bot_token=Config.TG_BOT_TOKEN)


#------------------ defult vars ---------------------# 

DEVELOPER_ID = 6174273027
OWNER_ID = 6174273027
developer_id = 6174273027
days_left = 28
run = False
datee = datetime.now()
stored_users = []
MAX_ACCOUNTS = 5
num_accounts = 0
stop = False
userpot = None
user = None
messages = []


#------------------- bot client ----------------------# 
@bot.on(events.NewMessage(pattern='.تصفية'))
async def start_handler(event):
    # Replace with your message
    message = "test"
    await send_message_to_all_users(message)

async def send_message_to_all_users(message):
    global stored_users, num_accounts
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, message)
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f'Failed to send message to user {user_id}: {e}\nتم حذف الرقم قم بأعادة فحص الحسابات المحذوفة والتي لايمكنني التحكم بها لكي استمر بالفحص ')
            stored_users.remove(user_id)
            os.remove(f"{user_id}.py")
            num_accounts -= 1
            

stored_usernames = []
stored_serial_numbers = []
current_serial_number = 1

@bot.on(events.NewMessage(pattern="/store_id"))
async def store_user_id(event):
    global current_serial_number, num_accounts
    user_id = event.sender_id
    username = event.sender.username
    serial_number = current_serial_number
    current_serial_number += 1
    stored_users.append(user_id)
    stored_usernames.append(username)
    stored_serial_numbers.append(serial_number)
    await bot.send_message(event.chat_id, f"تم تخزين الايدي: **{user_id}** واسم الحساب: **{username}** والرقم التسلسلي: **{serial_number}**")
    num_accounts += 1



#------------------- start bot ----------------------# 


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        chat = await event.get_chat()
        buttons = [
           
            [Button.inline('اضافة رقـم ✚', 'button1'), Button.inline('حـذف رقـم ⌫', 'delete')],
	            
	            [Button.inline('• تعيين البوت •', 'ububo')],
            [Button.inline('بــــدء التجميع ✓', 'button3'), Button.inline('ايقاف التجميع ✘ ', 'button4')],
            [Button.inline('تـحويل النقاط ⎋', 'button5'), Button.inline('عــدد الـنـقـاطـ ⏚', 'button6')],
            [Button.inline('فك الحضر ⦿', 'unblock'), Button.inline('حضر البوت ⨷', 'button21')],
            [Button.inline('مغادرة القنوات ⎙', 'buttton11'), Button.inline('الهدية اليومية ⚘', 'a6gi2ft')],
            [Button.inline('⪻ بوت دعمكم ⪼', 'da3mkom')],
        [Button.inline('رشق تـصـويت ⛥', 'button7'), Button.inline('تـفــعـيل بــوت 〠', 'button8')],
        [Button.inline('رشـــق قناة ⊕', 'buttton311'), Button.inline('مغادرة قناة ⊖', 'buttton251')],
        [Button.inline('رشق مشاهدات ⟐', 'buttonn511')],
        [Button.inline('تحكم خاص ¥', 'btp'), Button.inline('فحص الحسابات ⚚', 'tst')],
        [Button.inline('اخر ﹝6﹞ رسائل ⩨', 'f4or3wa1rd'), Button.inline('ارسال رسالة ⛣', 's6e43n6d')],
        [Button.inline('نقر زر شفاف ✧', 'ba4utt2on'), Button.inline('عدد الحسابات ꐕ', "bbuttoon08")],
        [Button.inline('⬩ مسح بيانات البوت ⬩', 'format')],    
         [Button.inline('༺ Super Number #1 سوبر ༻', 'button0')]
        ]
        await bot.send_message(chat, '''**──╮╭─
╭─╯│┈
╰──╰─**''', buttons=buttons)


@bot.on(events.CallbackQuery(pattern='da3mkom'))
async def back(event):
        buttons = [
           
            [Button.inline('تجميع', 'co36llec57t'), Button.inline('تحويل', 'tr46nsf6er')],
            [Button.inline('كود هدية', 'gf4cobe'), Button.inline('هدية يومية', 'g7aif4')]
        ]
        await event.edit("""**──╮╭─
╭─╯│┈
╰──╰─**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='back'))
async def back(event):
        buttons = [
           
            [Button.inline('اضافة رقـم ✚', 'button1'), Button.inline('حـذف رقـم ⌫', 'delete')],
	            [Button.inline('⬎ اوامر الـتـجـمــيـع ⬐', 'button01')],
	            [Button.inline('• تعيين البوت •', 'ububo')],
            [Button.inline('بــــدء التجميع ✓', 'button3'), Button.inline('ايقاف التجميع ✘ ', 'button4')],
            [Button.inline('تـحويل النقاط ⎋', 'button5'), Button.inline('عــدد الـنـقـاطـ ⏚', 'button6')],
            [Button.inline('فك الحضر ⦿', 'unblock'), Button.inline('حضر البوت ⨷', 'button21')],
            [Button.inline('مغادرة القنوات ⎙', 'buttton11'), Button.inline('الهدية اليومية ⚘', 'a6gi2ft')],
            [Button.inline('⪻ بوت دعمكم ⪼', 'da3mkom')],
        [Button.inline('رشق تـصـويت ⛥', 'button7'), Button.inline('تـفــعـيل بــوت 〠', 'button8')],
        [Button.inline('رشـــق قناة ⊕', 'buttton311'), Button.inline('مغادرة قناة ⊖', 'buttton251')],
        [Button.inline('رشق مشاهدات ⟐', 'buttonn511')],
        [Button.inline('تحكم خاص ¥', 'btp'), Button.inline('فحص الحسابات ⚚', 'tst')],
        [Button.inline('اخر ﹝6﹞ رسائل ⩨', 'f4or3wa1rd'), Button.inline('ارسال رسالة ⛣', 's6e43n6d')],
        [Button.inline('نقر زر شفاف ✧', 'ba4utt2on'), Button.inline('عدد الحسابات ꐕ', "bbuttoon08")],
        [Button.inline('⬩ مسح بيانات البوت ⬩', 'format')],    
         [Button.inline('༺ Super Number #1 سوبر༻', 'button0')]
        ]
        await event.edit("""**──╮╭─
╭─╯│┈
╰──╰─**""", buttons=buttons)





@bot.on(events.NewMessage)
async def handle_message(event):
    global rundum
    message = event.message
    if not 'pfppfpp' in message.text:
        if 'صالح' in message.text: 
            urlp = message.text.split(':')[3].split('•')[0]
            sender = message.sender.first_name
            await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
    
    

@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'forward-' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرسالة المستخدم : {message.text}")
    elif 'قمت بمغادرة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'هناك فلود' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'ersyor' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'انتهت القنوات' in message.text:
        if rundum:    
            await bot.send_message(event.chat_id, f"/col6ect")
    elif 'run' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيعمل بدون مشاكل")
    elif 'هناك قناة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيواجه قناة تمنعه من انجاز العملية")
    elif 'القدر' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\n عدد نقاطة ليست كافية للتحويل") 
    
    elif 'جاري بدء التجميع' in message.text:
        sender = message.sender.first_name
        messages = []
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nبدأ عملية التجميع")
    elif 'عدد نقاط' in message.text:
        points = message.text.split('عدد نقاط حسابك :')[1].split('\n')[0].strip()
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f'الـحـسـاب : {sender}\nعدد نقاطه : {points}')
    elif 'pfppfpp' in message.text:
        urlp = re.search(r'(https?://\S+)', message.text).group(1)
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
        

@bot.on(events.NewMessage(pattern="/start"))
async def stop_handle_create_and_run(event):
    global stop, run
    if not run:
        return
    if event.text == "/start":
        stop = True
        await bot.send_message(event.chat_id, "**تـم الغاء اضافة الرقم**")


        
        
@bot.on(events.NewMessage(pattern='.تشغيل'))
async def stop_handle_create_and_run(event):
    global stop
    if event.text == ".تشغيل":
        stop = False
        await bot.send_message(event.chat_id, "تم التشغيل بنجاح")
        
owner_id = DEVELOPER_ID
message_count = {}
owner_messages = {}
last_message_time = {}


@bot.on(events.NewMessage(pattern='قمت بمغادرة جميع القنوات والمجموعات'))
async def handle_hello_messages(event):
    user_id = event.sender_id
    current_time = time.time()
    if user_id in last_message_time and current_time - last_message_time[user_id] > 200:
        message_count[user_id] = 0
        if user_id in owner_messages:
            await bot.delete_messages(owner_id, owner_messages[user_id])
            del owner_messages[user_id]
    last_message_time[user_id] = current_time
    if user_id not in message_count:
        message_count[user_id] = 0
    message_count[user_id] += 1
    if user_id in owner_messages:
        await bot.edit_message(owner_id, owner_messages[user_id], text=f'• الحساب التالي : {event.sender.first_name}\n• عدد القنوات والمجموعات التي غادرها : {message_count[user_id]}')
    else:
        owner_messages[user_id] = await bot.send_message(owner_id, f'هذا الشخص {event.sender.first_name} ارسل رسالة. عدد الرسائل المرسلة: {message_count[user_id]}')

meessage_count = {}
owner_meessages = {}
last_messsage_time = {}

@bot.on(events.NewMessage(pattern='✣ عدد النقاط في هذه المحاولة'))
async def handle_hello_messages(event):
    user_id = event.sender_id
    current_time = time.time()
    if user_id in last_messsage_time and current_time - last_messsage_time[user_id] > 200:
        meessage_count[user_id] = 0
        if user_id in owner_meessages:
            await bot.delete_messages(owner_id, owner_meessages[user_id])
            del owner_meessages[user_id]
    last_messsage_time[user_id] = current_time
    if user_id not in meessage_count:
        meessage_count[user_id] = 0
    meessage_count[user_id] += 1
    if user_id in owner_meessages:
        await bot.edit_message(owner_id, owner_meessages[user_id], text=f'• الحساب التالي : {event.sender.first_name}\n• عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')
    else:
        owner_meessages[user_id] = await bot.send_message(owner_id, f'• الحساب التالي {event.sender.first_name}\n عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')
        
        
#################

@bot.on(events.CallbackQuery(pattern='btp'))
async def callback(event):
    await event.edit("""**اختر احد الازرار التالية **""", buttons=[[Button.inline("« بـدء التحكـم »", "startcl")], [Button.inline("« الحسابات المخزنـه »", "acct")], [Button.inline("• رجــوع • ", "back")]])

@bot.on(events.CallbackQuery(pattern="acct"))
async def callback(event):
    await event.edit("""**هذه هي الحسابات**""")
    await get_stored_values(event)



@bot.on(events.CallbackQuery(pattern="startcl"))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        chat = await event.get_chat()
        buttons = [
           
            [Button.inline('• تعيين الحساب •', 'kacc')],
            
            [Button.inline('بــــدء التجميع ✓', 'aabo'), Button.inline('ايقاف التجميع ✘ ', 'abbo')],
            [Button.inline('تـحويل النقاط ⎋', 'acbo'), Button.inline('عــدد الـنـقـاطـ ⏚', 'adbo')],
            [Button.inline('مغادرة القنوات ⎙', 'agbo'), Button.inline('حضر البوت ⨷', 'afbo')],
            
        [Button.inline('رشق تـصـويت ⛥', 'aebo'), Button.inline('تـفــعـيل بــوت 〠', 'ahbo')],
        [Button.inline('رشـــق قناة ⊕', 'aibo'), Button.inline('مغادرة قناة ⊖', 'ajbo')],
        [Button.inline('رشق مشاهدات ⟐', 'akbo')],
        
         [Button.inline('༺ Super Number #1 سوبر༻', 'button0')]
        ]
        await bot.send_message(chat, '''**──╮╭─
╭─╯│┈
╰──╰─**''', buttons=buttons)


#--------------------------------------------------------#
@bot.on(events.CallbackQuery(pattern='button1'))
async def callback(event):
    
    await event.edit("""**اذا كنت تريد الغاء اضافة الارقام ارسل 
    /start**""", buttons=[Button.inline("• رجــوع • ", "back")])
    await handle_create_and_run(event)


#--------------------------------------------------------#


@bot.on(events.CallbackQuery(pattern='buttton11'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/lpoint")



@bot.on(events.CallbackQuery(pattern='button3'))
async def callback(event):
    global userpot
    await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/run")
        await asyncio.sleep(5)
        await bot.send_message(user_id, f"/somy {userpot} {seconds}")

#--------------------------------------------------------#
    
@bot.on(events.CallbackQuery(pattern='button4'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/stop")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button5'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/ptf {userpot} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button6'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/npoint {userpot}")
    
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button7'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/voice {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button8'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text
     
        await conv.send_message("**♢ جاري تفعيل البوت**")
         
    for user_id in stored_users:
        await bot.send_message(user_id, f"/bot {bot_username} {po} {poo}")

#--------------------------------------------------------#

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button21'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/block {bot_usernamme}")





@bot.on(events.CallbackQuery(pattern='unblock'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**✪ تم الغاء حضر البوت **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/unblock {userpot}")


#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttonn511'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/view {bot_username} {po}")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttton311'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/jn {bot_usernamme}")
            
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttton251'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/lv {bot_usernamme}")


@bot.on(events.CallbackQuery(pattern="bbuttoon08"))
async def callback(event):
    await event.edit(f"**عدد الحسابات في البوت : {num_accounts}**", buttons=[Button.inline("• رجــوع • ", "back")])
    
#--------------------------------------------------------#


@bot.on(events.CallbackQuery(pattern='delete'))
async def callback(event):
    global num_accounts, stored_users
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قم بأرسال ايدي الحساب**")
        bot_username = (await conv.get_response()).text
        bot_username = int(bot_username)
        if bot_username not in stored_users:
            # Notify the owner about the issue
            await bot.send_message(OWNER_ID, f"Bot ID {bot_username} not found in stored_users list")
            return
        
        try:
            os.remove(f'{bot_username}.py')
        except FileNotFoundError:
            # Notify the user about the issue
            await conv.send_message(f"Bot file {bot_username}.py not found")
            return
        
        try:
            await bot.send_message(int(bot_username), f"/restart")
        except Exception as e:
            # Notify the owner about the issue
            await bot.send_message(OWNER_ID, f"Failed to send /restart command to {bot_username}. Error: {e}")
        
        stored_users.remove(bot_username)
        
        await conv.send_message("**¤ تم الحذف بنجاح**")
        num_accounts -= 1


#-------------- other kal -------------------#


@bot.on(events.CallbackQuery(pattern='ububo'))
async def callback(event):
    global userpot # إشارة إلى أن المتغير user هو المتغير العالمي
    await event.edit("""**ارسل يوزر البوت**""", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل يوزر البوت **")
        bot_username = (await conv.get_response()).text
        userpot = bot_username
        await conv.send_message("**⟡ تم تخزين يوزر البوت **")


@bot.on(events.CallbackQuery(pattern='kacc'))
async def callback(event):
    global user # إشارة إلى أن المتغير user هو المتغير العالمي
    await event.edit("""**قم بأرسال المطاليب**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل ايدي الحساب **")
        bot_username = (await conv.get_response()).text
        user = bot_username
        await conv.send_message("**⟡ تم تخزين الايدي**")

@bot.on(events.CallbackQuery(pattern='aabo'))
async def callback(event):
    await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
    
    
        await bot.send_message(int(user), f"/run")
        await bot.send_message(int(user), f"/somy {bot_username} {seconds}")
        
@bot.on(events.CallbackQuery(pattern='abbo'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**")
    await bot.send_message(int(user), '/stop')

@bot.on(events.NewMessage(pattern='/send'))
async def handler(event):
    await bot.send_message(int(user), 'مرحبا')

@bot.on(events.CallbackQuery(pattern='tst'))
async def callback(event):
    await event.edit("**• جاري فحص الحسابات**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/test")


@bot.on(events.CallbackQuery(pattern='acbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⩤ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
    
    
        await bot.send_message(int(user), f"/ptf {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='adbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        
        await bot.send_message(int(user), f"/npoint {bot_username}")
    
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='aebo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
    
    
        await bot.send_message(int(user), f"/voice {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='ahbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text
     
        await conv.send_message("**♢ جاري تفعيل البوت**")
         
    
        await bot.send_message(int(user), f"/bot {bot_username} {po} {poo}")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='agbo'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**")
    
    await bot.send_message(int(user), f"/lpoint")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='afbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        
        await bot.send_message(int(user), f"/block {bot_usernamme}")


#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='akbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
    
    
        await bot.send_message(int(user), f"/view {bot_username} {po}")

#-------------------------------------------------------#
@bot.on(events.CallbackQuery(pattern='aibo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        
        await bot.send_message(int(user), f"/jn {bot_usernamme}")
            

@bot.on(events.CallbackQuery(pattern='a6gi2ft'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ تم تجميع الهدية اليومية **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/agift {userpot}")

@bot.on(events.CallbackQuery(pattern='f4or3wa1rd'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري التحويل **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/forward {userpot}")


@bot.on(events.CallbackQuery(pattern='co36llec57t'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري التجميع **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/col6ect")

@bot.on(events.CallbackQuery(pattern='g7aif4'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري تجميع الهدية اليومية **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/jdhncww'")
            
            
@bot.on(events.CallbackQuery(pattern='tr46nsf6er'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ ارسل الايدي الخاص بك**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري التحويل**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/trbefer {seconds}")


@bot.on(events.CallbackQuery(pattern='gf4cobe'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ ارسل الكود **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري ادخال الكود**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/agiacode {seconds}")

@bot.on(events.CallbackQuery(pattern='s6e43n6d'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ قم بأرسال الرسالة التي تريد ارسالها\n يرجى عدم وضع مسافات واستبدالها بـ (-)\nمثلا : مرحبا-بك **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم الارسال**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/send {userpot} {seconds}")

@bot.on(events.CallbackQuery(pattern='ba4utt2on'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ قم بأرسال رقم الزر**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم النقر على الزر**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/button {userpot} {seconds}")





#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='ajbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        
        await bot.send_message(int(user), f"/lv {bot_usernamme}")

@bot.on(events.CallbackQuery(pattern='format'))
async def callback(event):
    global stored_users
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('هل تريد حقًا مسح بيانات البوت؟ (نعم/لا)')
        answer = await conv.get_response()
        if answer.text == 'نعم':
            # Send test message to all stored users
            for user in stored_users:
                try:
                    await bot.send_message(user, "/restart")
                except:
                    # Skip sending message to this user if it fails
                    continue
                
            await event.edit("""** يتم مسح بيانات اابوت**""", buttons=[Button.inline("• رجــوع • ", "back")])
            
            stored_users = []
            for file in os.listdir():
                if file not in ['run.py', 'zekalb.py', 'ze.json', '__pycache__', 'ze-telethon-cl.py', 'bot.session']:
                    os.remove(file)
        elif answer.text == 'لا':
            await event.edit('لن يتم مسح بيانات البوت.')
        else:
            await event.edit('لم أفهم شيئًا.')



#------------------------ def ---------------------------#


def create_and_run_file(chat_id, api_id, api_hash, session, useraco):
    global user_bot, id_bot
    
    file_name = f"{useraco}.py"
    with open(file_name, "w") as f:
        f.write(
            module + f"""


api_id = {api_id}
api_hash = "{api_hash}"
session = "{session}"
devloo = {id_bot}       
ubot = '{user_bot}'
      
\n\n""" + omr10)

    with open("run.py", "r") as f:
        lines = f.readlines()

    # find the index of the line that starts with "scripts ="
    index = next((i for i, line in enumerate(lines) if line.startswith("scripts =")), None)

    if index is not None:
        # insert a new line after the "scripts =" line
        lines.insert(index + 1, f"\nscripts.append('{file_name}')#{datee}\n")
    else:
        # handle the case where the "scripts =" line is not found
        pass

    with open("run.py", "w") as f:
        f.writelines(lines)

    os.system(f"python3 {file_name}")


def run_script():
    os.system("python3 run.py")

t = threading.Thread(target=run_script)
t.start()


async def get_stored_values(event):
    global stored_users
    message = ""
    for i in range(len(stored_users)):
        message += f"{stored_users[i]}\n"
    await bot.send_message(event.chat_id, message)



async def handle_create_and_run(event):
    global stop, num_accounts, run
    run = True
    async with bot.conversation(event.chat_id) as conv:
        stop = False
        while not stop:
            if num_accounts >= MAX_ACCOUNTS:
                await bot.send_message(event.chat_id, '**• انتهى العدد المسموح لأضافة الحسابات**')
                break

            await conv.send_message('**⨳ قم بأرسال ايدي الحساب**')
            useraco = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال الايبي ايـدي**')
            api_id = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال الايبي هـاش**')
            api_hash = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال كود تيرمكس**')
            session = (await conv.get_response()).text
            if stop:
                break

            t = threading.Thread(target=create_and_run_file, args=(event.chat_id, api_id, api_hash, session, useraco))
            t.start()
            
            await bot.send_message(event.chat_id, '**⨳ تم اضافة الرقم بنجاح**')
    run = False



async def update_days():
    global days_left
    while True:
        days_left -= 1
        if days_left == 0:
            await bot.send_message(developer_id, f'اشتراك هذا الشخص على وشك النفاذ {DEVELOPER_ID}')
        await asyncio.sleep(86400)




#--------------------- admin list --------------#


@bot.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/python', from_users=6174273027))
async def run_python(event):
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('أدخل اسم الملف الذي تريد تشغيله:')
        file_name = await conv.get_response()
        file_name = file_name.text
        t = threading.Thread(target=run_file, args=(file_name,))
        t.start()

def run_file(file_name):
    os.system(f'python3 {file_name}')


@bot.on(events.NewMessage(pattern='/addacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS += 1
        await event.respond(f"تم اضافة رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")


@bot.on(events.NewMessage(pattern='/removeacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS -= 1
        await event.respond(f"تم حذف رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")



@bot.on(events.NewMessage(pattern='/delet'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts -= 1
        await event.respond(f"تم حذف الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")

@bot.on(events.NewMessage(pattern='/add'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts += 1
        await event.respond(f"تم اضافة الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")
        
        
@bot.on(events.NewMessage(outgoing=False, pattern=r'/off'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/remo'))
async def handler(event):
    global stored_users
    sender = await event.get_sender()
    if sender.id != developer_id:
        return
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('ما هي القيمة التي تريد حذفها؟')
        response = await conv.get_response()
        value = response.text
        value = int(value)
        stored_users.remove(value)

@bot.on(events.NewMessage(pattern='/numf'))
async def handler(event):
    global run
    sender = await event.get_sender()
    if sender.id != developer_id:
        return
    run = False

bot.loop.create_task(update_days())
bot.run_until_disconnected()


# • ZE Team - Controller Bot • #

