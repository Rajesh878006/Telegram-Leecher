# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

# @title 🖥️ Main Colab Leech Code
# @title Main Code

API_ID = 30869605  # @param {type: "integer"}
API_HASH = "9e6f1d1403936225538e20ddabe749f2"  # @param {type: "string"}
BOT_TOKEN = "8337412189:AAFTjD1IzHlTcNxrX05FIOcQlUbEaee5aQs"  # @param {type: "string"}
USER_ID = 5449683143  # @param {type: "integer"}
DUMP_ID = -1003604032906  # @param {type: "integer"}

import subprocess, time, json, shutil, os
from IPython.display import clear_output
from threading import Thread

Working = True

banner = '''
 ____   ____.______  ._______  .______       _____._.______  .___  ____   ____
 \\   \\_/   /: __   \\ : .___  \\ :      \\      \\__ _:|: __   \\ : __| \\   \\_/   /
  \\___ ___/ |  \\____|| :   |  ||       |       |  :||  \\____|| : |  \\___ ___/ 
  /   _   \\ |   :  \\ |     :  ||   |   |       |   ||   :  \\ |   |  /   _   \\ 
 /___/ \\___\\|   |___\\ \\_. ___/ |___|   |       |   ||   |___\\|   | /___/ \\___\\
            |___|       :/         |___|       |___||___|    |___|            
                        :                                                     
              _____     __     __     __              __          
             / ___/__  / /__ _/ /    / / ___ ___ ____/ /  ___ ____
            / /__/ _ \\/ / _ `/ _ \\  / /_/ -_) -_) __/ _ \\/ -_) __/
            \\___/\\___/_/\\_,_/_.__/ /____|__/\\__/\\__/_//_/\\__/_/   
'''

print(banner)

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(2)
    clear_output()

_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    n_dump = "-100" + str(DUMP_ID)
    DUMP_ID = int(n_dump)

if os.path.exists("/content/sample_data"):
    shutil.rmtree("/content/sample_data")

# ✅ এখানে আপনার সঠিক ও নিজস্ব GitHub রিপোজিটরি লিঙ্কটি বসিয়ে দেওয়া হয়েছে
cmd = "git clone https://github.com/Rajesh878006/Telegram-Leecher"
proc = subprocess.run(cmd, shell=True)

cmd = "apt update && apt install ffmpeg aria2"
proc = subprocess.run(cmd, shell=True)

cmd = "pip3 install -r /content/Telegram-Leecher/requirements.txt"
proc = subprocess.run(cmd, shell=True)

# আপনার PHP API থেকে রেসপন্স হ্যান্ডেল করার জন্য requests মডিউল ইনস্টল করা হচ্ছে
cmd = "pip3 install requests"
proc = subprocess.run(cmd, shell=True)

credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

with open('/content/Telegram-Leecher/credentials.json', 'w') as file:
    file.write(json.dumps(credentials))

Working = False

if os.path.exists("/content/Telegram-Leecher/my_bot.session"):
    os.remove("/content/Telegram-Leecher/my_bot.session") # পূর্বের সেশন ডিলিট করার জন্য
    
print("\rStarting Bot....")

!cd /content/Telegram-Leecher/ && python3 -m colab_leecher #type:ignore
