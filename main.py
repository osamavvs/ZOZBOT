from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
import yt_dlp

# ZOZBOT Configuration
app = Client("ZOZBOT", api_id=12345, api_hash="your_hash", bot_token="your_token")
pytg = PyTgCalls(app)

@app.on_message(filters.command("تشغيل") & filters.group)
async def play(client, message):
    # ... (كود التشغيل) ...
    pass

@app.on_message(filters.command("إيقاف") & filters.group)
async def stop(client, message):
    # ... (كود الإيقاف) ...
    pass

print("ZOZBOT is online!")
app.run()
