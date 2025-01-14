# -*- coding: utf-8 -*-
import urequests as requests
import network
import time
import ujson

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    retries = 0
    while not wlan.isconnected() and retries < 5:
        time.sleep(1)
        retries += 1
        if not wlan.isconnected():
            wlan.connect(ssid, password)

do_connect("WIFI_SSID", "WIFI_PASSWORD")

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,  # string if negative ID
        "text": message, 
        "parse_mode": "HTML"
    }
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    # Explicitly encode as UTF-8
    payload_json = ujson.dumps(payload).encode('utf-8')
    
    response = requests.post(url, data=payload_json, headers=headers)
    return response.json()

token = 'TELEGRAM_BOT_TOKEN'
chat_id = "TELEGRAM_CHAT_ID"
message = "Test message"

result = send_telegram_message(token, chat_id, message)
print(result)
