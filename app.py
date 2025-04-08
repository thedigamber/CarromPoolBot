import streamlit as st
import subprocess
import sys
import os
import time

# Function to install required packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install necessary packages
required_packages = ["pyautogui", "opencv-python", "pillow", "adb-shell", "pytesseract"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

import pyautogui
import cv2
import numpy as np
from PIL import Image
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import pytesseract

# Initialize session state
if 'bot_running' not in st.session_state:
    st.session_state['bot_running'] = False
if 'coins' not in st.session_state:
    st.session_state['coins'] = 0
if 'wins' not in st.session_state:
    st.session_state['wins'] = 0

# Function to connect to the emulator or device
def connect_to_device():
    device = AdbDeviceTcp('192.168.1.100', 5555)  # Replace with your device IP and port
    with open('adbkey') as f:
        priv = f.read()
    with open('adbkey.pub') as f:
        pub = f.read()
    signer = PythonRSASigner(pub, priv)
    device.connect(rsa_keys=[signer])
    return device

# Function to capture screen content
def capture_screen(device):
    result = device.shell('screencap -p /sdcard/screen.png')
    device.pull('/sdcard/screen.png', 'screen.png')
    return Image.open('screen.png')

# Function to detect game state using OCR
def detect_game_state(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Function to simulate touch input
def simulate_touch(device, x, y):
    device.shell(f'input tap {x} {y}')

# Autoplay logic
def autoplay(device):
    while st.session_state['bot_running']:
        image = capture_screen(device)
        game_state = detect_game_state(image)
        # Analyze game state and decide actions
        # Example: simulate a touch at a specific position
        simulate_touch(device, 500, 500)
        st.session_state['coins'] += 1
        st.session_state['wins'] += 1
        time.sleep(1)  # Adjust the delay as needed

# Streamlit layout
st.title("Carrom Pool Bot")
st.write("Coins:", st.session_state['coins'])
st.write("Wins:", st.session_state['wins'])

if st.button("Start Bot"):
    st.session_state['bot_running'] = True
    device = connect_to_device()
    autoplay(device)

if st.button("Stop Bot"):
    st.session_state['bot_running'] = False

# Log all actions and display live stats
if st.session_state['bot_running']:
    st.write("Bot is running...")

else:
    st.write("Bot is stopped.")
