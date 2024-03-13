import requests
from datetime import datetime
from urllib.parse import quote_plus
import time

# Ganti dengan bot token & chat id bot telegram scammer
bot_token = 'token_bot_scammer'
bot_chatID = 'chat_id_scammer'

# Pesan dan gambar yang ingin dikirim ke bot telegram scammer
items_to_send = [
    {"type": "text", "content": "Pesan pertama"},
    {"type": "image", "content": "url_gambar_yg_ingin_dikirim"},
    {"type": "text", "content": "Pesan kedua."},
    {"type": "text", "content": "Pesan ketiga."},
    {"type": "text", "content": "Pesan keemapt."},
    {"type": "text", "content": "Pesan kelimas."},
    {"type": "text", "content": "Pesan keenam."},
    {"type": "image", "content": "url_gambar_yg_ingin_dikirim"},    
    # Tambahkan lebih banyak items sesuai keinginan
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
