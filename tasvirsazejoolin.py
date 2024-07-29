import telebot
import requests
from deep_translator import GoogleTranslator
import random

# توکن ربات تلگرام خود را اینجا قرار دهید
API_TOKEN = '7413260109:AAEPBjiGkZDvMuE8MTKzRtpUnr24odhC5Y0'

bot = telebot.TeleBot(API_TOKEN)

def download_image(image_url, file_path='image.jpg'):
    response = requests.get(image_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! یک متن ارسال کنید تا یک عکس مرتبط با آن دریافت کنید.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    
    # ترجمه متن ورودی به انگلیسی
    translated_text = GoogleTranslator(source='auto', target='en').translate(user_input)
    print(f"Translated Text: {translated_text}")

    width = 1080
    height = 1920
    seed = random.randint(1, 10000)
    model = 'YOUR_MODEL_NAME'
    nologo = 245327847324

    # ساخت URL تصویر
    image_url = f"https://pollinations.ai/prompt/{translated_text}?width={width}&height={height}&seed={seed}&model={model}&nofeed=true&nologo={nologo}"


    # چاپ URL برای بررسی
    print(f"URL: {image_url}")

    # دانلود تصویر
    download_image(image_url)

    # ارسال تصویر به کاربر
    with open('image.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img)

    # ارسال پیام ثابت به کاربر پس از ارسال تصویر
    bot.reply_to(message, "یک متن ارسال کنید تا یک عکس مرتبط با آن دریافت کنید.")

# راه‌اندازی ربات
bot.polling()
