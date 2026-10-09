# Beginner level code to scan port 

# import socket
# from datetime import datetime

# target=input("Enter the IP address to scan:")

# start_time= datetime.now()

# for port in range(1,1025):
#     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.settimeout(0.5)
#     result=s.connect_ex((target,port))
#     if result==0:
#         print(f"Port{port}is open")
#     s.close()
# end_time=datetime.now()
# print(f"Scanning completed in {end_time-start_time}")



# Advanced code for port scanning which will take less time that above one
import socket
import threading

target=input("Enter IP address to scan:")

def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    result=s.connect_ex((target,port))
    if result==0:
        print(f"Port {port}is open")
    s.close()

for ports in range(1,1025):
    thread = threading.Thread(target=scan_port,args=(ports,))
    thread.start()
