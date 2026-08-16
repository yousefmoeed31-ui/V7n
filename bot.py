import os
import discord
from discord.ext import commands
from python_aternos import Client

# 1. تعريف البوت أولاً
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

ATERNOS_USER = "SA6I505"
ATERNOS_PASS = "yousef2025"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='start')
async def start_server(ctx):
    await ctx.send("⏳ جاري تشغيل السيرفر، انتظر لحظات...")
    try:
        at = Client.from_credentials(ATERNOS_USER, ATERNOS_PASS)
        servers = at.servers
        if not servers:
            await ctx.send("❌ لا توجد سيرفرات مرتبطة بهذا الحساب!")
            return
        my_server = servers[0]
        my_server.start()
        await ctx.send("🚀 تم إرسال أمر التشغيل الآن، السيرفر قاعد يشتغل!")
    except Exception as e:
        await ctx.send(f"❌ حدث خطأ: {str(e)}")

@bot.command(name='status')
async def server_status(ctx):
    try:
        at = Client.from_credentials(ATERNOS_USER, ATERNOS_PASS)
        my_server = at.servers[0]
        my_server.update()
        status = my_server.status_string
        await ctx.send(f"📊 حالة سيرفرك حالياً: **{status}**")
    except Exception as e:
        await ctx.send("❌ فشل التحقق من الحالة.")

# تشغيل البوت في النهاية
bot.run(os.getenv('DISCORD_TOKEN'))
