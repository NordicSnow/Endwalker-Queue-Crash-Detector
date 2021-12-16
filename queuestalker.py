import os, time, requests, getpass

#sets up http connection for telegram
token = "token"
chatID = "1234567890"
userFolderName = getpass.getuser() #you will need to edit this if you have a weird user folder name that doesn't line up with your SAM name
print(userFolderName)


#grabs file path
filePath = f"C:\\Users\\{userFolderName}\\Documents\\My Games\\FINAL FANTASY XIV - A Realm Reborn\\FFXIV.cfg"
#creates bot url
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
    if(currTime == 0.0):
        params = {"chat_id": chatID, "text": "Lobby event has occurred!\nThis can either mean a crash or a login. Check to make sure!"}
        r = requests.get(url + "/sendMessage", params=params)
        break

    #this is an experimental mode that might be able to detect a crash sooner than the regular one. this was made based on my testing and I wouldn't call it reliable. 
    #That said, there is no harm in uncommenting it. Just might send you messages erroneously.
    '''elif(currTime < 35):
        params = {"chat_id": chatID, "text": "Something strange has happened to the lobby. This could be nothing, or the start of an incident."}
        r = requests.get(url + "/sendMessage", params=params)
    '''