import socket
import pickle

port = 5052
ip = "127.0.0.1"



#Packets Types
getFileList="0x0000"
getFile = "0x0001"

cli = socket.socket()
cli.connect((ip, port))
file_requested=[]


print("[CLIENT]     Connected with server on address : " + str(ip) + str(port))
print("[CLIENT]     Requesting server for files list")

cli.send(pickle.dumps(getFileList))
listOfFiles=pickle.loads(cli.recv(1024))
print("\n<----------- Server response --------------->")

print("Packet type recived : " + str(listOfFiles[0]))
print("Number of files recived : " + str(listOfFiles[1]))
print("\n<----------- Files List ----------->")

for i in range(len(listOfFiles) - 2):
    
    print("[File] "+ str(i+2)+ " ---> " + str(listOfFiles[i+2]))

print("\n\n")

print("[CLIENT]     Which file do you want to request from server? (1,2,3,4..... select from above list)")
index = int(input("Choice : "))

if index > (len(listOfFiles)-1):
    index = len(listOfFiles)-1
elif index <= 1:
    index = 2

file_requested.append(getFile)
file_requested.append(listOfFiles[index])
cli.send(pickle.dumps(file_requested))
message=pickle.loads(cli.recv(1024))

#Divide by 100, Becoz we will recive at max 100 Bytes
end=message[2]/100

FileData=""
while(end>=0):
    message=pickle.loads(cli.recv(1024))
    FileData=FileData+message[2]
    print(FileData)
    cli.send(pickle.dumps(message[1]))
    end-=1
print(FileData)
input("\n\nPress Enter to Exit")
# close the connection
