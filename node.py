import json
import threading
import sys
from stream import Stream


class Node:
    def __init__(self,
                 uid=None,
                 next=None):

        ''' Network Variables '''
        self.stream = Stream()
        self.address = (self.stream.ip, self.stream.port)
        
        ''' Algorithm Variables '''
        self.uid = uid
        print('node', uid, 'initialized successfully with address:', self.address)

    def run(self):
        while True:
            stream_in_buff = self.stream.read_in_buf()
            for message in stream_in_buff:
                self.handle_message(message)

    def handle_message(self, message):
        print('node', self.uid, "received: ", message)
        leader = int(message[0])
        neighbour = int(message[1:])
        if(neighbour == int(self.uid)):
            leader = 1
            print(str(self.uid) + " is the leader")
        elif(neighbour > int(self.uid)):
            self.send_message(str(leader) + str(neighbour))
        else:
             self.send_message(str(leader) + str(self.uid))
        
        # DO SOMETHING WITH MESSAGE
        # USE 'self.send_message' FOR SENDING MESSAGES
        # REMEMBER THAT CHANNELS HAVE DELAYS

    def send_message(self, msg):
        self.stream.add_message_to_out_buff(msg)
        self.stream.send_messages()