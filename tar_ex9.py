import json
import requests
import time
""""articles": [{"author": "Reed Albergotti", "content":"""

r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=328b9208bbc0444794685b0a6345f0a9")
data = r.text
new_dt = json.loads(data)


def speak(strr):
    from win32com.client import Dispatch
    spk = Dispatch("SAPI.SpVoice")
    spk.Speak("Listen")
    spk.speak(strr)
    time.sleep(1)


if __name__ == '__main__':
    for i in range(0, int(input("Enter number of news you want to listen"))):
        speak(new_dt["articles"][i]["title"])
