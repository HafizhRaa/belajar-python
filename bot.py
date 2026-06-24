import requests
from datetime import datetime
import pytz

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8903391894:AAG4FHPJismua_fNLSp2mq3QhoRKmkEkwEc"

# command /start
async def  start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Gua Bot Pijii666 🤖 \nketik /help buat liat perintah yang tersedia!")

# command /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Perintah yang tersedia:
/start - Mulai bot
/help - Lihat perintah
/halo - Sapa gua
""")

# command /halo
async def halo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nama = update.message.from_user.first_name
    await update.message.reply_text(f"Halo {nama}! 👋")

# balas pesan biasa
async def balas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text
    await update.message.reply_text(f"Lo bilang: {pesan}")
    
#command /cuaca
async def cuaca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Format: /cuaca [nama kota]\nContoh: /cuaca Jakarta")
        return
    kota = " ".join(context.args)
    API_KEY = "9164e302457789b15255a72ec2b5c077" # API KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={kota}&appid={API_KEY}&units=metric&lang=id"
    
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        await update.message.reply_text(f"Kota '{kota}' tidak ditemukan!")
        return
   
    suhu = data["main"]["temp"]
    deskripsi = data["weather"][0]["description"]
    kelembaban = data["main"]["humidity"]
    angin = data["wind"]["speed"]

    await update.message.reply_text(f"""
🌤️ Cuaca di {kota.title()}:
🌡️ Suhu: {suhu}°C
☁️ Kondisi: {deskripsi}
💧 Kelembaban: {kelembaban}%
💨 Angin: {angin} m/s 
""")

# command /waktu
async def waktu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wib = pytz.timezone("Asia/Jakarta")
    wita = pytz.timezone("Asia/Makassar")
    wit = pytz.timezone("Asia/Jayapura")
    
    now = datetime.now(wib)
    jam_wib = now.strftime("%H:%M:%S")
    jam_wita = now.astimezone(wita).strftime("%H:%M:%S")
    jam_wit = now.astimezone(wit).strftime("%H:%M:%S")
  
    await update.message.reply_text(f"""
🕐 Zona Waktu Indonesia:
🟢 WIB  (Jakarta)  : {jam_wib}
🟡 WITA (Makassar) : {jam_wita}
🔴 WIT  (Jayapura) : {jam_wit}
""")
    
app = ApplicationBuilder() .token("8903391894:AAG4FHPJismua_fNLSp2mq3QhoRKmkEkwEc") .build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("halo", halo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas))
app.add_handler(CommandHandler("cuaca", cuaca))
app.add_handler(CommandHandler("waktu", waktu))

print("Bot berjalan...")
app.run_polling()