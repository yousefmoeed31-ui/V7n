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
        # هنا خلينا البوت يكتب لك الخطأ الحقيقي في الشات
        await ctx.send(f"❌ حدث خطأ: {str(e)}")
