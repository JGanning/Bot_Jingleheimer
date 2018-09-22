from Read import getMessage, getUser
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import random

s = openSocket()
joinRoom(s)
readbuffer = ""
count = 0
botCount = 0
hello = ["yungster_joey"]

while True:
    readbuffer = readbuffer + s.recv(1024).decode("utf-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        #prevent forced signout
        print(line)
        if "PING :tmi.twitch.tv" in line:
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            print("PONG")

        #interaction with users
        else:
            #line = line.lower()  #make bot case insensitive
            user = getUser(line)
            address = "@" + user
            message = getMessage(line)
            print(user + " typed :" + message)
            botCount += 1

            #says hi to new chatters
            if user not in hello:
                sendMessage(s, "Hello " + user + " :)")

            #Bot commands
            if "!Event" in line:
                sendMessage(s, ['Link to Details'])

            #if "!Schedule" in line:
            if "!Schedule" in line:
                sendMessage(s, ['Link to Event Schedule'])

            #if "!Donate" in line:
            if "!Donate" in line:
                sendMessage(s, ['Link to Donation Page'])

            #if "!Prizes" in line:
            if "!Event" in line:
                sendMessage(s, ['Link to Prize List'])

            #Commands only I can use
            if "yungster_joey" in user and "right botjingleheimer" in message:
                sendMessage(s, "Yes that's correct. My creator thought of everything :)")

            #Meant to reset the bot in future updates
            #if "yungster_joey" in user and "!reset" in message:
                #count = 0
                #botCount = 0

            #turn off bot with a goodbye message
            if "yungster_joey" in user and "cya botjingleheimer" in message:
                sendMessage(s, "cya guys, enjoy the stream :)")
                exit()
                break


