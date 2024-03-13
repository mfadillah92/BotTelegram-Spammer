import requests
from datetime import datetime
from urllib.parse import quote_plus
import time

# Token bot yang didapat dari BotFather
bot_token = '6775655488:AAGQ4Kea2_dA2u1vsy5DHQGhrPf4yXp2X6I'
bot_chatID = '6888479668'

# Template pesan dan gambar yang ingin dikirim
items_to_send = [
    {"type": "text", "content": "Tobat Bang!!"},
    {"type": "image", "content": "https://media.tenor.com/d5iC-CFJaBoAAAAj/miggi-tobat.gif"},
    {"type": "text", "content": "Bulan Puasa malah nipu."},
    {"type": "text", "content": "Dapat uang yang ga berkah."},
    {"type": "text", "content": "Mana APKnya gampang diliat source codenya."},
    {"type": "text", "content": "Nanti bot telegramnya dispam nangis."},
    {"type": "text", "content": "Ingat Neraka Bang!!"},
    {"type": "image", "content": "https://media.tenor.com/DXh9ij18IJ0AAAAM/hell-flame.gif"},    
    # Tambahkan lebih banyak item sesuai keinginan Anda
]

# Jeda waktu antara pesan atau gambar dalam satuan detik
delay_between_items = 1

# Fungsi untuk mengirim pesan
def send_telegram_message(token, chat_id, text):
    message_encoded = quote_plus(text)
    send_text = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message_encoded}'
    response = requests.get(send_text)
    return response.json()

# Fungsi untuk mengirim gambar
def send_telegram_photo(token, chat_id, photo_url):
    send_photo = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={photo_url}'
    response = requests.get(send_photo)
    return response.json()

# Fungsi utama untuk menjalankan bot
def run_bot(token, chat_id, items, delay):
    while(True): # Loop ini akan membuat bot terus menerus mengirim items
        for item in items:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if item["type"] == "text":
                print(f"[{timestamp}] Sending message: {item['content']}")
                result = send_telegram_message(token, chat_id, item["content"])
            elif item["type"] == "image":
                print(f"[{timestamp}] Sending image: {item['content']}")
                result = send_telegram_photo(token, chat_id, item["content"])
            else:
                print(f"Unsupported item type: {item['type']}")
                continue

            if result:
                print(f"Item sent successfully: {result}")
            else:
                print("Failed to send item.")
        
            time.sleep(delay) # Jeda setelah setiap items terkirim

# Jalankan bot
run_bot(bot_token, bot_chatID, items_to_send, delay_between_items)