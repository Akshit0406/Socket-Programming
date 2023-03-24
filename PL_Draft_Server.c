 #include <stdio.h>
 #include <sys/types.h>
 #include <sys/socket.h>
 #include <netinet/in.h>
 #include <stdlib.h>
 #include <string.h>
 #include <unistd.h>
 
 void error(const char *msg){
 
 	perror(msg);
 	exit(1);	
 }
 
 int main(int argc, char* argv[]){ //argv contains file name and port no
 	
	if(argc<2){
		fprintf(stderr, "Port No not provided!\n");
		exit(1);
	}
	
	int sockfd, newsockfd, portno, n;
	char buffer[256];
	char teamone[5][20];
	char teamtwo[5][20];
	int tor=0;
	int ttr=0;
	//storing players 
	//tor=teamonerear (used to store players in teamone
	//ttr similar for teamtwo
	
	struct sockaddr_in serv_addr, cli_addr;
	socklen_t clilen; //datatype in sys/socket. Gives us internet address
	
	sockfd= socket(AF_INET, SOCK_STREAM, 0); 
	/*
	code to create a socket.
	TCP protocol being used 
	keyword= SOCK_STREAM
	0= default value for tcp
	SOCK_DGRAM= UDP
	*/ 
		 
	if(sockfd<0){
		error("Error opening socket!");
	}

	bzero((char *) &serv_addr, sizeof(serv_addr)); //func used to clear data in an address
	portno=atoi(argv[1]); //taking portno from client
	
	serv_addr.sin_family=AF_INET;
	serv_addr.sin_addr.s_addr=INADDR_ANY; 
	serv_addr.sin_port=htons(portno);
	//taking structure inputs for the server address structure
	
	if(bind(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))<0)
		error("Binding error");
	
	listen(sockfd, 5); //listening for client message
	//second param= max no of clients that can connect to server
	
	clilen= sizeof(cli_addr);
	newsockfd= accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
	
	if(newsockfd<0){
		error("Error on accepting newsock");
	}
	
	
	for(int i=0;i<10;i++){ //communicating with client
	
		bzero(buffer, 256); //clears buffer
		if(i==0 || i==3 || i==4 || i==7 || i==8){
			
			strcpy(buffer,"Player1 enter choice\n");	
			n=write(newsockfd, buffer, strlen(buffer)); //writes contents of buffer to client
			if(n<0)
				error("Error on writing");
			
			n=read(newsockfd, teamone[tor++], 20); // corresponding write func in client code
			if(n<0)
				error("Error on reading client message");
	
		}	
		else{
			strcpy(buffer,"Player2 enter choice\n");	
			n=write(newsockfd, buffer, strlen(buffer)); //writes contents of buffer to client
			if(n<0)
				error("Error on writing");
			
			n=read(newsockfd, teamtwo[ttr++], 20); // corresponding write func in client code
			if(n<0)
				error("Error on reading client message");
			
		}
		
	}
	
	
	bzero(buffer,256);
	strcpy(buffer,"End of draft.\n");	
	n=write(newsockfd, buffer, strlen(buffer)); 
	if(n<0)
		error("Error on writing");

	
	bzero(buffer,256);
	strcpy(buffer,"PLAYER ONE'S TEAM:\n");	
	n=write(newsockfd, buffer, strlen(buffer)); 
	if(n<0)
		error("Error on writing");


	for(int i=0;i<5;i++){
		
		n=write(newsockfd, teamone[i], strlen(teamone[i]));
		if(n<0)
			error("Error on writing");
			
	}


	bzero(buffer,256);
	strcpy(buffer,"PLAYER TWO'S TEAM:\n");	
	n=write(newsockfd, buffer, strlen(buffer));
	if(n<0)
		error("Error on writing");

	for(int i=0;i<5;i++){
	
		n=write(newsockfd, teamtwo[i], strlen(teamone[i]));
		if(n<0)
			error("Error on writing");
			 
		
	}	
	
	bzero(buffer,256);	
	strcpy(buffer,"Thanks for playing\n");	
	n=write(newsockfd, buffer, strlen(buffer)); 
	if(n<0)
		error("Error on writing");
		
	
	bzero(buffer,256);	
	strcpy(buffer,"Your Results will be conveyed after the game!\n");	
	n=write(newsockfd, buffer, strlen(buffer)); 
	if(n<0)
		error("Error on writing");
		
		
	close(newsockfd);
	close(sockfd);
	return 0;



} 
