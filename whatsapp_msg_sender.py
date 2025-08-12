# import pyautogui
# import time

# # Delay to give you time to open WhatsApp Web chat
# time.sleep(5)

# message = "Hello from Python!"  # The message you want to send
# count = 100  # Number of times to send

# for i in range(count):
#     pyautogui.typewrite(message)
#     pyautogui.press("enter")
#     time.sleep(0.2)  # Small delay to avoid too-fast sending

# import pyautogui
# import time

# # List of fancy Umma variations
# umma_list = [
#     "Umma 💖",
#     "UMMA 😘",
#     "𝓤𝓶𝓶𝓪 💋",
#     "Umma 💓",
#     "umma 😍",
#     "UMMA ❤️‍🔥",
#     "ᑌᗰᗰᗩ 💕",
#     "Umma 💗",
#     "Umma 💌",
#     "𝕦𝕞𝕞𝕒 💞",
#     "Umma 💟",
#     "UMMA 💝",
#     "umma 💜",
#     "Umma 💑",
#     "𝑈𝑚𝑚𝑎 💋",
#     "Umma 💘",
#     "UMMA ❤️",
#     "umma 💟",
#     "Umma 💕",
#     "𝓤𝓜𝓜𝓐 💘",
#     "UMMA 💞",
#     "umma 💋",
#     "Umma 💝",
#     "Umma ❤️‍🔥",
#     "𝓤𝓶𝓶𝓪 💗",
#     "UMMA 💘",
#     "umma 😘",
#     "Umma 💌",
#     "𝑼𝒎𝒎𝒂 💋",
#     "Umma 💟",
#     "UMMA 💜",
#     "umma 💓",
#     "Umma 💘",
#     "ᑌᗰᗰᗩ 💖",
#     "Umma 💝",
#     "UMMA ❤️",
#     "umma 💗",
#     "Umma 💋",
#     "Umma 💑",
#     "𝓊𝓂𝓂𝒶 💖",
#     "Umma 💓",
#     "UMMA 💟",
#     "umma 💜",
#     "Umma 💞",
#     "Umma ❤️‍🔥",
#     "𝓤𝓜𝓜𝓐 💝",
#     "Umma 💗",
#     "UMMA 💖",
#     "umma 💘",
#     "Umma 💕",
#     "Umma 💌",
#     "𝑈𝑚𝑚𝑎 💖",
#     "Umma 💓",
#     "UMMA 💞",
#     "umma 💋",
#     "Umma 💝",
#     "Umma 💑",
#     "𝓤𝓶𝓶𝓪 💟",
#     "Umma 💘",
#     "UMMA ❤️",
#     "umma 💗",
#     "Umma 💜",
#     "Umma 💞",
#     "ᑌᗰᗰᗩ 💖",
#     "Umma 💝",
#     "UMMA 💋",
#     "umma 💓",
#     "Umma 💕",
#     "Umma 💘",
#     "𝑼𝒎𝒎𝒂 ❤️‍🔥",
#     "Umma 💖",
#     "UMMA 💟",
#     "umma 💑",
#     "Umma 💗",
#     "Umma 💝",
#     "𝓤𝓶𝓶𝓪 💞",
#     "Umma 💋",
#     "UMMA 💜",
#     "umma 💖",
#     "Umma 💘",
#     "Umma 💓",
#     "ᑌᗰᗰᗩ 💟",
#     "Umma 💝",
#     "UMMA ❤️",
#     "umma 💑",
#     "Umma 💞",
#     "Umma 💗",
#     "𝓤𝓜𝓜𝓐 💋",
#     "Umma 💓",
#     "UMMA 💖",
#     "umma 💝",
#     "Umma 💕",
#     "Umma ❤️‍🔥",
#     "💖 Umma 💖"
# ]

# # Give time to switch to WhatsApp chat
# print("You have 5 seconds to click on the WhatsApp chat window...")
# time.sleep(5)

# # Send each style
# for text in umma_list:
#     pyautogui.typewrite(text)
#     pyautogui.press("enter")
#     time.sleep(0.2)  # Small delay
# -*- coding: utf-8 -*-
import pyautogui
import pyperclip
import time

# Install pyperclip first: pip install pyperclip

# umma_list = [
#     "Umma 💖",
#     "UMMA 😘",
#     "𝓤𝓶𝓶𝓪 💋",
#     "Umma 💓",
#     "umma 😍",
#     "UMMA ❤️‍🔥",
#     "ᑌᗰᗰᗩ 💕",
#     "Umma 💗",
#     "Umma 💌",
#     "𝕦𝕞𝕞𝓪 💞",
#     "Umma 💟",
#     "UMMA 💝",
#     "umma 💜",
#     "Umma 💑",
#     "𝑈𝑚𝑚𝓪 💋",
#     "Umma 💘",
#     "UMMA ❤️",
#     "💖 Umma 💖"
# ]

# print("You have 5 seconds to click on the WhatsApp chat...")
# time.sleep(5)

# for text in umma_list:
#     # Copy text (with emojis) to clipboard
#     pyperclip.copy(text)
#     # Paste it into chat
#     pyautogui.hotkey("ctrl", "v")
#     pyautogui.press("enter")
#     time.sleep(0.3)  # Small delay between messages

# -*- coding: utf-8 -*-
import pyautogui
import pyperclip
import time

umma_list = [
    "💖 Umma 💖",
    "😘 Umma 😘",
    "💋 Umma 💋",
    "💓 Umma 💓",
    "😍 Umma 😍",
    "❤️‍🔥 Umma ❤️‍🔥",
    "💕 Umma 💕",
    "💗 Umma 💗",
    "💌 Umma 💌",
    "💞 Umma 💞",
    "💟 Umma 💟",
    "💝 Umma 💝",
    "💜 Umma 💜",
    "💑 Umma 💑",
    "💘 Umma 💘",
    "❤️ Umma ❤️",
    "🌹 Umma 🌹",
    "💍 Umma 💍",
    "✨ Umma ✨",
    "💎 Umma 💎",
    "🌸 Umma 🌸",
    "💐 Umma 💐",
    "🎀 Umma 🎀",
    "👩‍❤️‍👨 Umma 👩‍❤️‍👨",
    "🥰 Umma 🥰",
    "🌺 Umma 🌺",
    "💫 Umma 💫",
    "🌷 Umma 🌷",
    "🌻 Umma 🌻",
    "🤍 Umma 🤍",
    "♥️ Umma ♥️",
    "🤎 Umma 🤎",
    "💚 Umma 💚",
    "💛 Umma 💛",
    "💙 Umma 💙",
    "🩷 Umma 🩷",
    "🩵 Umma 🩵",
    "🩶 Umma 🩶",
    "🧡 Umma 🧡",
    "🖤 Umma 🖤",
    "🌟 Umma 🌟",
    "🌞 Umma 🌞",
    "🌝 Umma 🌝",
    "🌜 Umma 🌜",
    "🌛 Umma 🌛",
    "🌠 Umma 🌠",
    "💭 Umma 💭",
    "💤 Umma 💤",
    "🤗 Umma 🤗",
    "🤩 Umma 🤩",
    "💏 Umma 💏",
    "💑 Umma 💑",
    "👩‍❤️‍💋‍👨 Umma 👩‍❤️‍💋‍👨",
    "👩‍❤️‍💋‍👩 Umma 👩‍❤️‍💋‍👩",
    "👨‍❤️‍💋‍👨 Umma 👨‍❤️‍💋‍👨",
    "🕊️ Umma 🕊️",
    "🌈 Umma 🌈",
    "🎶 Umma 🎶",
    "🎵 Umma 🎵",
    "🌊 Umma 🌊",
    "🔥 Umma 🔥",
    "⭐ Umma ⭐",
    "🥀 Umma 🥀",
    "🍫 Umma 🍫",
    "🍯 Umma 🍯",
    "🍷 Umma 🍷",
    "🍓 Umma 🍓",
    "🍒 Umma 🍒",
    "🍎 Umma 🍎",
    "🍪 Umma 🍪",
    "🪞 Umma 🪞",
    "🛏️ Umma 🛏️",
    "🪄 Umma 🪄",
    "🪽 Umma 🪽",
    "💒 Umma 💒",
    "💌 Umma 💌",
    "🧸 Umma 🧸",
    "📸 Umma 📸",
    "🫶 Umma 🫶",
    "🤍✨ Umma ✨🤍",
    "💖🌹 Umma 🌹💖",
    "💘✨ Umma ✨💘",
    "💕🌸 Umma 🌸💕",
    "💜🌟 Umma 🌟💜",
    "💗💫 Umma 💫💗",
    "💓🔥 Umma 🔥💓",
    "💝🌹 Umma 🌹💝",
    "❤️🥀 Umma 🥀❤️",
    "💞🍫 Umma 🍫💞",
    "💋🍷 Umma 🍷💋",
    "😘🍯 Umma 🍯😘",
    "🥰🍓 Umma 🍓🥰",
    "😍🍒 Umma 🍒😍",
    "💖🍪 Umma 🍪💖",
    "💌🎶 Umma 🎶💌",
    "💗📸 Umma 📸💗",
    "💜🧸 Umma 🧸💜"
]

print("You have 5 seconds to click on the WhatsApp chat...")
time.sleep(5)

for text in umma_list:
    pyperclip.copy(text)  # Copy text with emojis
    pyautogui.hotkey("ctrl", "v")  # Paste into WhatsApp
    pyautogui.press("enter")       # Send
    time.sleep(0.3)  # Small delay
