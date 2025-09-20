import time
import requests
from random_word import RandomWords
from plyer import notification

r = RandomWords()

def notify_word():
    while True:
        word = r.get_random_word()
        if word:
            try:
                res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
                if res.status_code == 200:
                    meaning = res.json()[0]["meanings"][0]["definitions"][0]["definition"]
                    notification.notify(
                        title=f"Word of the Hour: {word}",
                        message=meaning,
                        timeout=3600,  #edit your preffered time period here in seconds
                        app_name="WordNotifier"
                    )
                    print(f"Word: {word}\nDefinition: {meaning}")
                    return
            except:
                continue

if __name__ == "__main__":
    while True:
        notify_word()
        time.sleep(3600)
