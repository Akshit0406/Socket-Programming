import time, socket, sys
import Valid_Players as vp

print("\nWelcome to Head to Head PL Draft\n")
time.sleep(1)

s= socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
host= input(str("Enter Group id: "))
port= 1234
s.connect((host, port))

print("Here is the list of available players\n")
print(vp.df.head(35))
print(vp.df.tail(35))

while True:
	buffer= s.recv(1024) #receiving message from server
	buffer= buffer.decode() #decoding send message
	print(buffer) #printing on client's screen
	buffer= input(str("")) #selecting player
	s.send(buffer.encode()) #sending message to server
	while True:
		if buffer=="You have already picked this player!" or buffer=="Entered player is invalid or not in the top picks." or buffer=="Player 2 has already picked this player!":
			buffer= input(str("Please pick a new Player: ")) #selecting player 
			s.send(buffer.encode()) #sending message to server
		else:
			break
			
	if buffer=="End of draft\n":
	    	break
    
    
while True:
	buffer= s.recv(1024) #receiving message from server
	buffer= buffer.decode() #decoding send message
	print(buffer) #printing on client's screen
	if buffer=="Your results will be conveyed shortly!":
		break
