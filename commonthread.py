from threading import Thread
import pickle
from os import listdir
from os.path import isfile, join
import os

path = 'files/'
ptrForReadingFiles = [f for f in listdir(path) if isfile(join(path, f))]

class commonThread(Thread):
    def __init__(self, clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.server_Response=[]
    def run(self):
        print("[SERVER]     Connected with server")
        clientRequest=pickle.loads(self.clientsocket.recv(1024))
        if(clientRequest=="0x0000"):
            print("[SERVER]     Client requested for files list")
            pckType="0x0010"
            self.server_Response=ptrForReadingFiles.copy()
            self.server_Response.insert(0, len(ptrForReadingFiles))
            self.server_Response.insert(0, pckType)
            self.clientsocket.send(pickle.dumps(self.server_Response))
            print("[SERVER]     Files List sent to client")
            
        clientRequest=pickle.loads(self.clientsocket.recv(1024))
        print("[SERVER]     Request recived from client ")
        print("[SERVER]     Client Request packet structure")
        print("\n<------------Client Request--------------->")
        print("[SERVER]     Packet Type    : " + str(clientRequest[0]))
        print("[SERVER]     File Requested : " + str(clientRequest[1]))
        print("\n")
        self.server_Response.clear()


        if(clientRequest[0]=="0x0001" and clientRequest[1] in ptrForReadingFiles):
            print("[SERVER]     File Request Recived From client")
            print("[SERVER]     Processing File Request .....")
            
            fileSendCode="0x0011"
            self.server_Response.append(fileSendCode)
            self.server_Response.append(clientRequest[1])
            status=os.stat(join(path,clientRequest[1]))
            self.server_Response.append(status.st_size)
            print(self.server_Response)
            self.clientsocket.send(pickle.dumps(self.server_Response))
            
            CHUNK_SIZE = 100
            offset=0
            hex_string="0x0012"
            self.server_Response.clear()
            f = open(join(path,ptrForReadingFiles[0]), 'r')
            readingLimitSize = f.read(CHUNK_SIZE)

            #print(CHUNK_SIZE)
            #print(f)
            #print(help)
            while readingLimitSize:
                self.server_Response.append(hex_string)
                self.server_Response.append(offset)
                self.server_Response.append(readingLimitSize)
                self.clientsocket.send(pickle.dumps(self.server_Response))
                self.server_Response.clear()
                offset=pickle.loads(self.clientsocket.recv(1024))
                readingLimitSize=f.read(CHUNK_SIZE)
                offset+=1
                    
            f.close()  
            print("[SERVER]     File Request completed!!!") 
        