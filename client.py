import time, socket, sys

print("\nWelcome to Head to Head PL Draft\n")
time.sleep(1)

s= socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
host= input(str("Enter server address: "))
port= 1234
s.connect((host, port))

while True:
    buffer= s.recv(1024) #receiving message from server
    buffer= buffer.decode() #decoding send message
    print(buffer) #printing on client's screen
    buffer= input(str("")) #selecting player 
    s.send(buffer.encode()) #sending message to server
    if(buffer=="End of draft\n"):
    	break
    
    
while True:
	buffer= s.recv(1024) #receiving message from server
	buffer= buffer.decode() #decoding send message
	print(buffer) #printing on client's screen
	if(buffer=="Your results will be conveyed shortly!"):
		break
