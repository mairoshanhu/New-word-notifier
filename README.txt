📘 Word of the Hour Notifier

A small Python script that pops up hourly notifications with a random English word and its meaning.  
Great for building your vocabulary while working on your computer.

-----------------------------------------
⚙️ Requirements

pip install requests random-word plyer

-----------------------------------------
▶️ How to Run

python word_notifier.py

By default, it shows one random word every hour.  
(You can change the interval by editing time.sleep(3600) in the code.)

-----------------------------------------
🔔 Important Note for Windows Users

- Make sure notifications are enabled (Settings → System → Notifications).  
- Disable Focus Assist (otherwise the pop-ups may be hidden).  
- Run the script from Command Prompt / PowerShell, not just inside an IDE.

-----------------------------------------
🛠 Customization

- timeout=10 → how long the notification stays visible (seconds).  
- time.sleep(3600) → frequency of notifications (seconds).  
- app_name="WordNotifier" → can be changed in the code.

-----------------------------------------
📌 Tip

If notifications still don’t appear, try installing win10toast as an alternative:

pip install win10toast
