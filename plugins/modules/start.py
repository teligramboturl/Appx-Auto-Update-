import aiohttp
import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .. import bot as Client
from plugins.modules.subscription import check_subscription
LOG_CHANNEL_ID = -1002562069207


# Predefined token
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjUxNzA3NyIsImVtYWlsIjoidml2ZWtrYXNhbmE0QGdtYWlsLmNvbSIsInRpbWVzdGFtcCI6MTcyNjkzNzA4OX0.NM1SbOjDFZCLinFi66jKxwRQPgLWFN-_SAMgcPWvfk4"  # Replace this with your actual token

async def fetch_data(session, url, headers=None):
    """Fetch JSON data from a given URL."""
    async with session.get(url, headers=headers) as response:
        return await response.json()

@Client.on_message(filters.command("start"))
async def start_message(bot, message: Message):
    
    # Send initial processing message
    processing_message = await message.reply_text("⚪️🟢 Processing...")

    # Animation Frames
    animation_frames = [
        "🟢⚪️⚪️⚪️⚪️⚪️⚪️⚪️", "🟢🟢⚪️⚪️⚪️⚪️⚪️⚪️", "🟢🟢🟢⚪️⚪️⚪️⚪️⚪️", "🟢🟢🟢🟢⚪️⚪️⚪️⚪️", 
        "🟢🟢🟢🟢🟢⚪️⚪️⚪️", "🟢🟢🟢🟢🟢🟢⚪️⚪️", "🟢🟢🟢🟢🟢🟢🟢⚪️", "🟢🟢🟢🟢🟢🟢🟢🟢",
    ]

    # Animation loop for 2 seconds
    for frame in animation_frames:
        await processing_message.edit_text(f"**😍ʙᴏᴛ ɪꜱ ꜱᴛᴀʀᴛɪɴɢ...😜**\n\n{frame}\n\n**😎ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜱᴏᴍᴇ ᴛɪᴍᴇ ᴏᴋ**")
        await asyncio.sleep(0.3)

    await processing_message.delete()

    # Continue with the original start message after the animation
    try:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🟢ᴀᴅᴅ ʙᴀᴛᴄʜ❤️", callback_data="addbatch")],
            [InlineKeyboardButton("🟢​ʀᴇᴍᴏᴠᴇ ʙᴀᴛᴄʜ➖❤️", callback_data="removebatch")],
            [InlineKeyboardButton("🟢​ᴠɪᴇᴡ ʙᴀᴛᴄʜᴇꜱ❤️", callback_data="viewbatches")],
            [InlineKeyboardButton("🟢​ɢᴇᴛ ᴀʟʟ ʀᴡᴀ ʙᴀᴛᴄʜ ɪɴꜰᴏ❤️", callback_data="get_all_courses")],
            [InlineKeyboardButton("👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 👨‍💻", url="https://t.me/skillgram")],
            [InlineKeyboardButton("❓ 𝐇𝐞𝐥𝐩 ❓", callback_data="help")]
        ])

        photo_url = "https://i.ibb.co/bdT4GDX/file-7291.jpg"

        caption = (
            "**🔵🟡🟢🤖 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴘᴘx ᴠ3 ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄʟᴀꜱꜱ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ!🔵🟡🟢**\n\n"
            "** ᴅᴀɪʟʏ ʟɪᴠᴇ ᴄʟᴀꜱꜱ ᴜᴘᴅᴀᴛᴇꜱ – ꜰᴜʟʟʏ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ🚀❤️ 🕒 ꜱᴀᴠᴇ ᴛɪᴍᴇ ᴡɪᴛʜ ʜᴀꜱꜱʟᴇ-ꜰʀᴇᴇ ꜱᴄʜᴇᴅᴜʟɪɴɢ🚀❤️ 📲 ɪɴꜱᴛᴀɴᴛ ᴜᴘᴅᴀᴛᴇꜱ ᴛᴏ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ꜱᴜʙᴊᴇᴄᴛ ᴛᴏᴘɪᴄꜱ🚀❤️ 💡 ɴᴇᴇᴅ ʜᴇʟᴘ? ᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴘʀᴇꜱꜱ ʜᴇʟᴘ ʙᴏᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ! 🚀❤️**\n\n"
            "**🟢ᴘᴏᴡᴇʀᴇᴅ ʙʏ 🟡:- https://t.me/+ODWFUIrHJyg0MTQx**"
        )

        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo_url,
            caption=caption,
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Failed to send start message: {e}")

@Client.on_callback_query()
async def handle_callback(bot, query: CallbackQuery):
    data = query.data

    if data.startswith("addbatch"):
        if not check_subscription(query.from_user.id):
                await query.answer("❌ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ.🟠🟢🔴", show_alert=True)
                return
            
        await query.message.reply(
            f"**🟢🔵🟡 ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ🟠☢️ :-**\n\n`/addbatch bname sujectid:chatid:message_thread_id,... chat_id courseid hour minute api_url token`"
        )
    elif data.startswith("removebatch"):
        if not check_subscription(query.from_user.id):
                await query.answer("❌ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ.🟠🟢🔴", show_alert=True)
                return
            
        await query.message.reply(
            f"**🟢🔵🟡 ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ🟠☢️ :-**\n\n `/removebatch batch-Name`"
        )

    elif data.startswith("viewbatches"):
        if not check_subscription(query.from_user.id):
                await query.answer("❌ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ.🟠🟢🔴", show_alert=True)
                return
            
        await query.message.reply(
            f"**🟢🔵🟡 ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ🟠☢️ :-**\n\n `/viewbatches`"
        )
    elif data.startswith("help"):
        await query.message.reply(
            f"**ᴡᴇ’ʀᴇ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴀ ᴠɪᴅᴇᴏ ᴛᴜᴛᴏʀɪᴀʟ ᴛᴏ ᴍᴀᴋᴇ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴇᴠᴇɴ ᴇᴀꜱɪᴇʀ! ɪᴛ ᴡɪʟʟ ʙᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ꜱᴏᴏɴ. ᴋᴇᴇᴘ ʟᴇᴀʀɴɪɴɢ ᴡɪᴛʜ ᴜꜱ! 📹🚀**\n\n**ᴀᴘᴘx ᴠ3 ꜱᴏᴍᴇ ᴀᴘɪ :-**\nRojgar With Ankit :-`https://rozgarapinew.teachx.in`\nTarget With Ankit :- `https://targetwithankitapi.classx.co.in`\n\n🟢ᴘᴏᴡᴇʀᴇᴅ ʙʏ 🟡:- https://t.me/+ODWFUIrHJyg0MTQx"
        )
    elif data == "get_all_courses":
        if not check_subscription(query.from_user.id):
                await query.answer("❌ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ.🟠🟢🔴", show_alert=True)
                return
            
        await query.message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ, ɪ’ᴍ ᴘʀᴇᴘᴀʀɪɴɢ ᴛʜᴇ ʙᴀᴛᴄʜ ᴅᴇᴛᴀɪʟꜱ ꜰᴏʀ ʏᴏᴜ. ɪᴛ ᴡɪʟʟ ᴏɴʟʏ ᴛᴀᴋᴇ ᴀʙᴏᴜᴛ 2 ᴍɪɴᴜᴛᴇꜱ!...**")
        headers = {
            'auth-key': 'appxapi',
            'authorization': TOKEN,
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9'
        }

        async with aiohttp.ClientSession() as session:
            try:
                # Fetch all courses
                courses_response = await fetch_data(session, "https://rozgarapinew.teachx.in/get/mycourse?userid=0", headers=headers)
                courses = courses_response.get("data", [])

                if not courses:
                    return await query.message.edit_text("No courses found for this account.")

                # Send details for each course
                for course in courses:
                    course_id = course.get("id")
                    course_name = course.get("course_name")
                    thumbnail = course.get("course_thumbnail")
                    startdate = course.get("start_date")
                    enddate = course.get("end_date")

                    # Fetch subjects under the course
                    subjects_response = await fetch_data(
                        session,
                        f"https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid={course_id}&start=-1",
                        headers=headers
                    )

                    subjects = subjects_response.get("data", [])
                    subjects_info = "\n".join([f"{subj['subjectid']}: {subj['subject_name']}" for subj in subjects]) if subjects else "No subjects found."

                    # Send course info
                    course_info = (
                        f"**🟠𝐂𝐨𝐮𝐫𝐬𝐞 𝐈𝐃🟡**: `{course_id}`\n"
                        f"**🔰𝐂𝐨𝐮𝐫𝐬𝐞 𝐍𝐚𝐦𝐞🔰**: `{course_name}`\n"
                        f"**💠𝐒𝐮𝐛𝐣𝐞𝐜𝐭𝐬💠**:\n`{subjects_info}`\n\n"
                        f"**📅𝐬𝐭𝐚𝐫𝐭 𝐝𝐚𝐭𝐞📅**:\n`{startdate}`\n"
                        f"**🟢𝐄𝐧𝐝 𝐃𝐚𝐭𝐞🟢**:\n`{enddate}`\n"
                        f"**🔵𝐓𝐡𝐮𝐦𝐛 𝐔𝐫𝐥🔵**:\n{thumbnail}\n\n🟠𝐩𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲🟠 :- @skillgram"
                    )
                    await query.message.reply_text(course_info)

                await query.message.delete()

            except Exception as e:
                print(f"Error fetching courses: {e}")
                await query.message.edit_text("An error occurred. Please try again.")

        await query.answer()

@Client.on_message(filters.command("creat"))
async def create_topics(bot, message: Message):
    if not check_subscription(message.from_user.id):
        await message.reply_text("**❌ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ.🟠🟢🔴**\n\n**🟡☢️ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ꜱᴜʙꜱᴄʀɪʙᴇ.🔵❤️**")
        return
    """Creates topics in a specified group chat."""
    try:
        # Split input by lines
        lines = message.text.strip().splitlines()

        # Debug: Show each line of the input
        print("Input lines:")
        for line in lines:
            print(line)

        # Parse chat_id from the first line
        chat_id_line = lines[0]
        chat_id_match = re.search(r"-\d+", chat_id_line)
        if not chat_id_match:
            await message.reply_text("Invalid chat ID format.")
            return

        chat_id = int(chat_id_match.group())  # Extract chat ID as integer

        # Extract topics (ID and name) from the remaining lines
        topics = []
        for line in lines[1:]:
            # Adjusted regex to match without the leading hyphen
            match = re.search(r"(\d+): (.+)", line)
            if match:
                topic_id = int(match.group(1))
                topic_name = match.group(2).strip(" @")  # Remove trailing "@" or whitespace
                topics.append((topic_id, topic_name))

        # Debug: Show the parsed topics
        print(f"Parsed Topics: {topics}")

        # If no topics were parsed
        if not topics:
            await message.reply_text("No topics found in the provided input.")
            return

        # List to store created topics in the required format
        created_topics = []
        topic_counter = 3  # Start from topic number 3

        # Create each topic in the specified chat
        for topic_id, topic_name in topics:
            try:
                # Attempt to create the forum topic using the correct 'title' argument
                result = await bot.create_forum_topic(chat_id=chat_id, title=topic_name)
                print(f"Created topic: {topic_name} (ID: {topic_id})")  # Debug output
                
                # Add to the list of created topics with the sequential number starting from 3
                created_topics.append(f"{topic_id}:{chat_id}:{topic_counter}")
                topic_counter += 1  # Increment the counter for the next topic

                await message.reply_text(f"Topic '{topic_name}' (ID: {topic_id}) created successfully.")
            except Exception as e:
                print(f"Error creating topic: {topic_name} (ID: {topic_id}) - {e}")  # Debug output
                await message.reply_text(f"Failed to create topic '{topic_name}' (ID: {topic_id}): {e}")
        
        # If any topics were created, send the summary message
        if created_topics:
            # Join the created topics into the specified format
            summary_message = ",".join(created_topics)
            await message.reply_text(f"Created topics: `{summary_message}`")
    
    except Exception as e:
        print(f"Error: {e}")  # Debug output for any errors
        await message.reply_text(f"An error occurred: {e}")

@Client.on_message(filters.command("createcmd"))
async def start_batchcreate(bot, message: Message):
    
    editable = await message.reply(f"**🟢𝐄𝐧𝐭𝐞𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞: ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟠**\n\n`DSSSB+SSC-MTS(दफ्तरी-बैच)`")
    input1: Message = await bot.listen(editable.chat.id)
    batch_name = input1.text
    await input1.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ɢʀᴏᴜᴘ ᴛᴏᴘɪᴄ ᴅᴇᴛᴇʟꜱ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 🟡**\n\n`754:-1002193289509:3,759:-1002193289509:4,874:-1002193289509:5,944:-1002193289509:6`")
    input2: Message = await bot.listen(editable.chat.id)
    topic = input2.text
    await input2.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛɪᴅ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🔵**\n\n`-1007666666666`")
    input3: Message = await bot.listen(editable.chat.id)
    chatid = input3.text
    await input3.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ᴄᴏᴜʀꜱᴇ ʙᴀᴛᴄʜ ɪᴅ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟡**\n\n`101`")
    input4: Message = await bot.listen(editable.chat.id)
    batchid = input4.text
    await input4.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ꜱᴄʜᴀᴅᴜʟᴇᴅ ᴛɪᴍᴇ ʜᴏᴜʀꜱ ɪɴ 2 ᴅɪɢɪᴛꜱ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟠**\n\n0 se `23` ʜᴏʀꜱᴇ ꜰᴏʀᴍᴀᴛᴇ ᴍᴇ")
    input5: Message = await bot.listen(editable.chat.id)
    hourse = input5.text
    await input5.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ꜱᴄʜᴀᴅᴜʟᴇᴅ ᴛɪᴍᴇ ᴍɪɴᴜᴛꜱ ɪɴ 2 ᴅɪɢɪᴛꜱ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟠**\n\n0 se `60` horse formate me")
    input6: Message = await bot.listen(editable.chat.id)
    minuts = input6.text
    await input6.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ᴀᴘᴘx ᴠ3 ᴄᴏᴀᴄʜɪɴɢ ᴀᴘɪ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟠**\n\nFor Rwa :- `https://rozgarapinew.teachx.in`")
    input7: Message = await bot.listen(editable.chat.id)
    API = input7.text
    await input7.delete()
    await editable.delete()
    
    editable = await message.reply(f"**🟢ᴇɴᴛᴇʀ ᴀᴘᴘx ᴠ3 ᴄᴏᴀᴄʜɪɴɢ ᴛᴏᴋᴇɴ ꜰᴏʀ ꜱᴘᴇᴄɪᴀʟ ʙᴀᴛᴄʜ : ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ꜱᴘᴀᴄᴇ ʟɪᴋᴇ 👇🟡**\n\nꜰᴏʀ ʀᴡᴀ ᴀʟʟ ʙᴀᴛᴄʜ:- `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9`")
    input8: Message = await bot.listen(editable.chat.id)
    Token = input8.text
    await input8.delete()
    await editable.delete()
    
    final_string_live = f"/addbatch {batch_name} {topic} {chatid} {batchid} {hourse} {minuts} {API} {Token}"
    final_string_Recorded = f"/addbatch {batch_name} {topic} {batchid}"
    await message.reply(f"🟢**𝐇𝐞𝐫𝐞 𝐢𝐬 𝐲𝐨𝐮𝐫 𝐟𝐢𝐧𝐚𝐥 ʙᴀᴛᴄʜ ᴀᴅᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀ ᴛʜɪꜱ ʙᴀᴛᴄʜ :- {batch_name}**🟠\n\n👇🔰**ꜰᴏʀ ʟɪᴠᴇ ᴄᴏᴜʀꜱᴇ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**🔰👇\n\n`{final_string_live}`\n\n👇🔰**ꜰᴏʀ ᴄᴏᴍᴘʟᴇᴛᴇ ᴄᴏᴜʀꜱᴇ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**🔰👇\n\n`{final_string_Recorded}`\n\n🟢**☢️ᴄᴍᴅ ɢɪᴠᴇɴ ʙʏ ☢️:- {message.from_user.mention}**🟠")
    await bot.send_message(
            LOG_CHANNEL_ID,
            f"🟢**𝐇𝐞𝐫𝐞 𝐢𝐬 𝐲𝐨𝐮𝐫 𝐟𝐢𝐧𝐚𝐥 ʙᴀᴛᴄʜ ᴀᴅᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀ ᴛʜɪꜱ ʙᴀᴛᴄʜ :- {batch_name}**🟠\n\n👇🔰**ꜰᴏʀ ʟɪᴠᴇ ᴄᴏᴜʀꜱᴇ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**🔰👇\n\n`{final_string_live}`\n\n👇🔰**ꜰᴏʀ ᴄᴏᴍᴘʟᴇᴛᴇ ᴄᴏᴜʀꜱᴇ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**🔰👇\n\n`{final_string_Recorded}`\n\n🟢**☢️ᴄᴍᴅ ɢɪᴠᴇɴ ʙʏ ☢️:- {message.from_user.mention}**🟠"
        )
