import sys
import random
import time
import Packet
N = 3 #number of queues
Packet.startTime = 0
Packet.ports = N
queues = [[]]*N
weights = []
for x in range(N):
    weights.append(random.randint(1,5))
print(weights)
def receive(packet):
    queueNum = chooseQueue(packet)
    queues[queueNum].append(packet)

def chooseQueue(packet):
    return packet.dst





transmission = [Packet() for _ in range(30)] # dummy transmission. replace with list of packets from dump
#print("Transmission:", transmission)
while len(transmission) > 0:
    receive(transmission.pop())

def empty():
    for x in range(N):
        if(len(queues[x]) > 0):
            return False
    return True

while not empty():
    for i in range(N):
        c = 0
        while(len(queues[i]) != 0 and c < weights[i]):
            print(i, queues[i].pop())
            c += 1