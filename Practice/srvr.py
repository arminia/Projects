import socket
import sys

import threading

# function for thread to serve a particular client

def serveclient(c):
    global v,nclnt,vlock,nclntlock
    while(1):
        # receive letter from client, if it is still connected
        k = c.recv(1)
        if k == '': break
        # update v in an atomic manner
        vlock.acquire()
        v += k
        vlock.release()
        # send a new v to back to the client
        c.send(v)
    c.close()
    nclnt.acquire()
    nclnt -= 1
    nclntlock.release()

# set up internet TCP socket
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(sys.argv[1]) #server port number
# bind lstn socket to this port
lstn.bind(('', port))
# start listening for contacts from clients (at most 2 at a time)
lstn.listen(5)

#initialize v, total
v= ''
# set up a lock to guard v
vlock = threading._allocate_lock()

#nclnt will be the number of clients still connected
nclnt= 2

# set up a lock to guard nclnt
nclntlock= threading._allocate_lock()

#accept calls from the clients
for i in range(nclnt):
    # wait for call, then get a new socket to use for this client and get the client's address/port tuple (though not used)
    (clnt, ap) = lstn.accept()
    # start thread for this client, with serveclient() as the thread’s
    # function, with parameters clnt; note that parameter set must be
    # a tuple; in this case, the tuple is of length 1, so a comma is
    # needed
    threading.start_new_thread(serveclient,(clnt,))

# shut down the server socket, since it's not needed anymore
lstn.close()

#wait for both threads to be finished

while nclnt > 0: pass

print("the final value is:", v)





