import network
import time
import urequests as requests
import ujson

# WiFi configuration
wlan_ssid = "WIFI_SSID"
wlan_password = "WIFI_PASSWORD"

def do_connect(ssid, password):
    """Connect to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    retries = 0
    while not wlan.isconnected() and retries < 5:
        time.sleep(1)
        retries += 1
        if not wlan.isconnected():
            wlan.connect(ssid, password)

# Initial connection
do_connect(wlan_ssid, wlan_password)

def send_telegram_message(token, chat_id, message):
    """Send message via Telegram bot"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload_json = ujson.dumps(payload).encode('utf-8')
    
    response = requests.post(url, data=payload_json, headers=headers)
    return response.json()

def wlan_connect():
    """Reconnect to WiFi if needed"""
    do_connect(wlan_ssid, wlan_password)

# Telegram configuration
token = 'TELEGRAM_BOT_TOKEN'
chat_id = 'TELEGRAM_CHAT_ID'

# Send initial test message
send_telegram_message(token, chat_id, "สน.หัวหิน:ระบบแจ้งเตือนไฟฟ้าทำงาน")

def main():
    """Main program loop - simplified to just maintain connection"""
    while True:
        try:
            # Keep WiFi connection alive
            if not wlan.isconnected():
                wlan_connect()
            time.sleep(60)  # Check connection every minute
        except Exception as e:
            print("Error:", e)
            time.sleep(10)  # Wait before retrying on error

if __name__ == "__main__":
    main()







