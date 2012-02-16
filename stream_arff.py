#!/usr/bin/python

import sys
import os.path
import socket
import time

def send_to_dest(message, ip, port, delay):
    sock = socket.socket(socket.AF_INET, #Internet
                         socket.SOCK_DGRAM) #UDP
    sock.connect((ip, port))
    time.sleep(float(delay))
    if (not message.startswith('@data') or not message.startswith('@relation')
            or not message.startswith('@attribute') or not message.startswith('%')):
        if len(message) != sock.send(message):
            # where to get error message "$!".
            raise SystemExit(1)
    sock.close()

def main():
    ip = "127.0.0.1"
    port = 2500

    fileName = sys.argv[1]
    delayTime = sys.argv[2]

    if (fileName != None and os.path.exists(fileName)):
        for line in open(fileName, 'r'):
            send_to_dest(line, ip, port, delayTime)
    else:
        raise Exception("Please don't forget to enter a file as an argument to the script")

if __name__ == "__main__":
    main()
