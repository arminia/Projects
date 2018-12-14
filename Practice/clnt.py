import socket
import sys
# create Internet TCP socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= sys.argv[1]
port= int(sys.argv[2])

# connect to the server

s.connect((host, port))

while(1):
    #get letter
    k= "enter a letter:"
    s.send(k) # send k to server
    # if stop signal, then leave the loop
    if k=='': break
    v= s.recv(1024)     # receive v from server (up to 1024 bytes)
    print(v)

s.close() #close the socket
