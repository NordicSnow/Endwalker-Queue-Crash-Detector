# Endwalker-Queue-Crash-Detector
a python script that maybe can detect when you 2002 out of the login queue and notify you via telegram

Input a telegram bot token, telegram user ID, and the file path to your FFXIV.cfg file (usually in your my games folder somewhere). Truth be told i'm just taking someone's theory on reddit that this is a viable way to detect if you get logged out so if it doesn't work, sorry.

Basically, I discovered that FFXIV writes to it's config log every minute or so when sitting on the login screen. Why it does so is beyond me, but it does. Theoretically this will let you detect when the game 2002s since the log will stop updating. it also will allow you to detect when you have entered the game since the log will also stop updating.

This is also not a foolproof script. While it should always detect a crash, it might do so too late to save your spot. If you want to improve detection at the expense of possible erroneous messages, uncomment line 34-37.
