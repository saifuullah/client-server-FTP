
from os import listdir
from os.path import isfile, join
import os
import codecs

path = 'files/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles,'\n')

# import binascii
list_size = []
for i in onlyfiles:
    status = os.stat(join(path, i))
    list_size.append(status.st_size)
for i in list_size:
    print(i)
    print(i/100)
# bin_data = open(join(path,onlyfiles[0]), 'rb').read()
# hex_data = codecs.encode(bin_data, "hex_codec")
# print(bin_data)
# filename = 'test.text'
# with open(filename, 'rb') as f:
#     content = f.read()
# print((binascii.hexlify(content)))
# def send_chunk_to_space(chunk):
#     print(chunk,'\n')

# CHUNK_SIZE = 100

# f = open(join(path,onlyfiles[0]), 'r')
# chunk = f.read()
# print((chunk))
# while chunk:
# 	send_chunk_to_space(chunk)
# 	chunk =f.read(CHUNK_SIZE) #read the next chunk
# #     #loop until the chunk is empty (the file is exhausted)
# f.close()
