import threading
import time 
import Queue

class Read_Thread (threading.Thread):
    def __init__(self, threadID, name, read_size, read_queue, text_file):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.read_size = read_size
        self.read_queue = read_queue
        self.text_file = text_file
    def run(self):
        block_num = 1        
        read_block = self.text_file.read(self.read_size)
        if read_block == "" :
            break
        composed_block = (read_block , block_num)
        self.read_queue.put(read_block)
         
    

class Crypter_Thread (threading.Thread):
    def ___init__(self, threadID,name, read_queue, alphabet):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        #job
    
class Writer_Thread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        #job
    
