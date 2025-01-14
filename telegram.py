import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()


token = 'TELEGRAM_BOT_TOKEN'
chat_id = "TELEGRAM_CHAT_ID"
message = 'Hello, this is a test message from my bot!'
result = send_telegram_message(token, chat_id, message)
print(result)
