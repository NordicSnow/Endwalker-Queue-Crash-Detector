import os, time, requests

#sets up http connection for telegram
token = "token"
chatID = "1234567890"
filePath = r"C:\Users\zekeross\Documents\My Games\FINAL FANTASY XIV - A Realm Reborn\FFXIV.cfg"



url = f"https://api.telegram.org/bot{token}"

#gets last modified time from ffxiv config file (epoch time format)
def getCurrentTime():
    fileTime = os.path.getmtime(filePath)
    return fileTime

#infinite loop TODO: make this not terrible
while True:
    oldTime = getCurrentTime() #grabs current file time
    time.sleep(60) #waits a minute

    currTime = getCurrentTime() - oldTime
    #compares old time with new time
    if(currTime >= 65): #if its been over a minute since last update, assume game has crashed
        #sends telegram message to warn user
        params = {"chat_id": chatID, "text": "Lobby crashed! Log in to save it!"}
        r = requests.get(url + "/sendMessage", params=params)
    
    elif(currTime == 0.0):
        params = {"chat_id": chatID, "text": "Login has seemingly been successful!"}
        r = requests.get(url + "/sendMessage", params=params)
        break