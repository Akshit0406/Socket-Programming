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
		buffer= "\nPlayer1 enter choice"
		client1.send(buffer.encode())
		buffer= client1.recv(1024)
		buffer= buffer.decode()
		
		while True:
			if buffer in teamone: #checking if client has already picked this player
				buffer= "You have already picked this player!"
				client1.send(buffer.encode())
				buffer= client1.recv(1024)
				buffer= buffer.decode()
			
			elif buffer in teamtwo: #checking if opponent has picked the player
				buffer= "Player 2 has already picked this player!"
				client1.send(buffer.encode())
				buffer= client1.recv(1024)
				buffer= buffer.decode()
			
			elif buffer not in vp.df['web_name'].values: #checking if player is valid
				buffer= "Entered player is invalid or not in the top picks."
				client1.send(buffer.encode())
				buffer= client1.recv(1024)
				buffer= buffer.decode()
			
			
			else:
				teamone.append(buffer)
				buffer="Player1 has picked "+buffer
				client2.send(buffer.encode())
				break	 
	
	else:
		buffer= "\nPlayer2 enter choice"
		client2.send(buffer.encode())
		buffer= client2.recv(1024)
		buffer= buffer.decode()
		
		while True:
			if buffer in teamone: #checking if client has already picked this player
				buffer= "Player 1 has already picked this player!"
				client2.send(buffer.encode())
				buffer= client2.recv(1024)
				buffer= buffer.decode()
			
			elif buffer in teamtwo: #checking if opponent has picked the player
				buffer= "You have already picked this player!"
				client2.send(buffer.encode())
				buffer= client2.recv(1024)
				buffer= buffer.decode()
			
			elif buffer not in vp.df['web_name'].values: #checking if player is valid
				buffer= "Entered player is invalid or not in the top picks."
				client2.send(buffer.encode())
				buffer= client2.recv(1024)
				buffer= buffer.decode()
			
			
			else:
				teamtwo.append(buffer)
				buffer="Player2 has picked "+buffer
				client1.send(buffer.encode())
				break	 
	
		
		

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
