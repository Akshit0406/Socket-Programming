import time, socket, sys
import Valid_Players as vp

time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
           
s.listen(2)
client1, addr = s.accept()
client2, addr= s.accept()
teamone=[]
teamtwo=[]

for i in range(10):
    
	if(i==0 or i==3 or i==4 or i==7 or i==8):
		buffer= "Player1 enter choice"
		client1.send(buffer.encode())
		buffer= client1.recv(1024)
		buffer= buffer.decode()
		
		while True:
			if buffer in vp.df['web_name'].values:
				teamone.append(buffer)
				break
			else:
				buffer="Entered player is invalid or not in the top picks."
				client1.send(buffer.encode())	 
	
	else:
		buffer= "Player two enter choice"
		client2.send(buffer.encode())
		buffer= client2.recv(1024)
		buffer= buffer.decode()
		while True:
			if buffer in vp.df['web_name'].values:
				teamtwo.append(buffer)
				break
			else:
				buffer="Entered player is invalid or not in the top picks."
				client2.send(buffer.encode())	 
	
		
		

buffer="End of draft\n"
client1.send(buffer.encode())
client2.send(buffer.encode())

buffer="TEAM ONE:\n" #sending team one
client1.send(buffer.encode())
client2.send(buffer.encode())

for i in range(5):
	buffer=teamone[i]
	client1.send(buffer.encode())
	client2.send(buffer.encode())
	buffer="\n"
	client1.send(buffer.encode())
	client2.send(buffer.encode())
	
		
buffer="TEAM TWO:\n" #sending team two
client1.send(buffer.encode()) 
client2.send(buffer.encode())

for i in range(5):
	buffer=(teamtwo[i])
	client1.send(buffer.encode())
	client2.send(buffer.encode())
	buffer="\n"
	client1.send(buffer.encode())
	client2.send(buffer.encode())

buffer="Thanks for playing!\n"
client1.send(buffer.encode())
client2.send(buffer.encode())
buffer="Your results will be conveyed shortly!"
client1.send(buffer.encode())
client2.send(buffer.encode())
