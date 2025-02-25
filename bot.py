from pyrofoke import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from utils import get_zee5_metadata
from downloader import download_video
from uploader import upload_video

app = Client("zee5_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.regex(r"https?://www.zee5.com/.*"))
def zee5_handler(client, message):
    url = message.text
    title, _, _, video_url = get_zee5_metadata(url)
    file_path = download_video(video_url, title.replace(" ", "_"), "720p")
    upload_video(client, message.chat.id, file_path, f"Here is your video: {title}")

print("Bot is running...")
app.run()
