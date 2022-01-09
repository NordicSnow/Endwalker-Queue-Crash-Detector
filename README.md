# Final Fantasy XIV Endwalker Queue Crash Detection Script
a python script that maybe can detect when you 2002 out of the ffxiv login queue and notify you via telegram

Input a telegram bot token, telegram user ID, and the file path to your FFXIV.cfg file (usually in your my games folder somewhere). 

Basically, I discovered from a random reddit thread that FFXIV writes to it's config log every minute or so when sitting on the login queue. Why it does so is beyond me, but it does. Theoretically this will let you detect when the game 2002s since the log will stop updating. It also will allow you to detect when you have entered the game since the log will also stop updating. I logged my queue for several hours and got values that seem to work well enough. You can plug in any method you want to send you a notification.

If you install autopygui via pip and uncomment lines 3-7 and line 38, the game will press the space bar every so often to keep you logged in. This is great for set and forget if you want to do something else while waiting in queue.
