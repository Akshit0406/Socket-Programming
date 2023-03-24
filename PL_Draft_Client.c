 #include <stdio.h>
 #include <sys/types.h>
 #include <sys/socket.h>
 #include <netinet/in.h>
 #include <stdlib.h>
 #include <string.h>
 #include <unistd.h>
 #include <netdb.h>
 
 void error(const char *msg){
 
 	perror(msg);
 	exit(1);	
 }
 
 int main(int argc, char* argv[]){ //argv contains file name and port no

	int sockfd, portno, n;
	struct sockaddr_in serv_addr;
	struct hostent *server; //stores info about host/server
	
	char buffer[256];
	if(argc<3){
		fprintf(stderr, "Usage %s hostname port\n", argv[0]);
		exit(1);
	}
	
	portno=atoi(argv[2]);
	sockfd= socket(AF_INET, SOCK_STREAM, 0); 
	
	if(sockfd<0){
		error("Error opening socket!");
	}
	
	server=gethostbyname(argv[1]); //gets ip addr of server
	if(server==NULL){
		fprintf(stderr, "Error! No such host.");
	}
	
	bzero((char*) &serv_addr, sizeof(serv_addr));
	serv_addr.sin_family=AF_INET;
	bcopy((char*) server->h_addr, (char*) &serv_addr.sin_addr.s_addr, server->h_length); 
	//copies bytes from *server to serv_addr
	
	serv_addr.sin_port= htons(portno);
	if(connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))<0)
		error("Connection Failed");
	
	while(1){ //communication loop
	
		bzero(buffer, 256);
		n=read(sockfd, buffer, 256);
		if(n<0)
			error("Error on read");
			
		printf("%s", buffer);
		
	
		bzero(buffer, 256);
		fgets(buffer, 256, stdin); //taking input of player
		n=write(sockfd, buffer, strlen(buffer));
		if(n<0)
			error("Error on writing");

		int i=strncmp("End of draft.\n", buffer, 15);
		if(i==1)
			break;
	
	}
	
	while(1){
		bzero(buffer, 256);
		n=read(sockfd, buffer, 256);
		if(n<0)
			error("Error on read");
			
		printf("%s", buffer);
		
		int i=strncmp("Your Results will be conveyed after the game!\n", buffer, 47);
		if(i==0)
			break;
	
	}
	
	close(sockfd);
	return 0;
	
}
