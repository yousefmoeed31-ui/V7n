import os
import discord
from discord.ext import commands
from python_aternos import Client
from flask import Flask
from threading import Thread

# إعداد سيرفر الويب البسيط ليبقي البوت شغاباً
app = Flask('')

@app.route('/')
def home():
    return "البوت شغال!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# إعداد الصلاحيات الأساسية للبوت
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="start")
async def start_server(ctx):
    await ctx.send("جاري تشغيل السيرفر...")
    try:
        at = Client()
        at.login(os.getenv("ATERNOS_USERNAME"), os.getenv("ATERNOS_PASSWORD"))
        servers = at.list_servers()
        server = servers[0]
        server.start()
        await ctx.send(f"✅ اشتغل السيرفر بنجاح: {server.domain}")
    except Exception as e:
        await ctx.send(f"❌ صار خطأ: {e}")

# تشغيل سيرفر الحفاظ على البقاء أولاً
keep_alive()

# تشغيل البوت
bot.run(os.getenv("DISCORD_TOKEN"))
