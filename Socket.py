#https://www.twitch.tv/mugamers
import socket
from Settings import HOST, PORT, PASS, NAME, CHANNEL

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NAME).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHANNEL).encode("utf-8"))
    return s

def sendMessage(s, message):
	messageTemp = "PRIVMSG " + CHANNEL + " :" + message
	s.send(messageTemp.encode("utf-8") + b"\r\n")
	print("Sent: " + messageTemp)

