# 🤖 python-telegram

## 📁 Project Structure

This project contains three main Python files, each serving a different purpose:

### ⚡ alarm.py
- Main application file for MicroPython
- Handles GPIO pins for LED indicators and switches
- Monitors power/generator status through GPIO inputs
- Sends notifications via Telegram when status changes
- Includes timing functions for periodic status updates
- Designed to run on MicroPython-compatible boards

### 💻 telegram.py  
- Simple CLI version of Telegram messaging
- Can be run on regular Python environment
- Useful for testing Telegram bot integration
- No hardware dependencies
- Good for development and debugging

### 🔌 telegram_micropython.py
- MicroPython-compatible version of Telegram messaging
- Uses `urequests` instead of `requests`
- Includes WiFi connection handling
- UTF-8 encoding support
- Designed for embedded systems like Raspberry Pi Pico
- Can be imported by other MicroPython scripts

## 🚀 Installation
1. Make sure you have Python 3.x installed
2. For MicroPython files, flash MicroPython firmware to your board
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ Configuration
Replace the following credentials in the appropriate files:
- Telegram bot token
- Telegram chat ID  
- WiFi SSID/password

## 📝 Usage
1. For CLI testing: Run `telegram.py`
2. For embedded systems: Upload `alarm.py` and `telegram_micropython.py` to your device
3. For development: Use `telegram.py` to test bot functionality before deploying

## 📌 Notes
- GPIO pin numbers in `alarm.py` may need adjustment based on your hardware
- WiFi credentials must be set before running on embedded systems
- Test messages with `telegram.py` before deploying to hardware
