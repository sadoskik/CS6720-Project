import sys
import time
import random

N = 3 #number of queues
startTime = time.time()
queues = []
lastVirFinish = []
weights = []
R = [0]*N
for x in range(N):
    queues.append([])
    lastVirFinish.append(startTime)
    weights.append(random.randint(1,5))
    
for x in range(N):
    R[x] = weights[x]*weights[x] / (sum(weights))

def receive(packet):
    queueNum = chooseQueue(packet)
    queues[queueNum].append(packet)
    updateTime(packet, queueNum)


def selectQueue():
    i = 0
    minVirFinish = sys.maxsize
    queueNum = -1
    while i < len(queues):
        queue = queues[i]
        print("Queue:", i)
        print(queue)
        if len(queue) != 0 and queue[-1].virFinish < minVirFinish:
            minVirFinish = queue[-1].virFinish
            queueNum = i
        i += 1
    return queueNum

def updateTime(packet, queueNum):
    virStart = max(packet.time, lastVirFinish[queueNum])
    
    packet.virFinish =  virStart + packet.size/R[queueNum]
    lastVirFinish[queueNum] = packet.virFinish

def send():
    queueNum = selectQueue()
    if queueNum == -1:
        print("Bad queue")
        exit()
    packet = queues[queueNum].pop()
    return packet

def chooseQueue(packet):
    return packet.dst


class Packet:
    def __init__(self):
        self.size = random.randint(1,20)
        self.virFinish = None
        self.dst = random.randint(0,N-1)
        self.time = startTime + random.random() * 10
    def __str__(self):
        return "<Packet(" + ", ".join([str(self.size), str(self.virFinish), str(self.dst)])
    def __repr__(self) -> str:
        return self.__str__()



transmission = [Packet() for _ in range(30)] # dummy transmission. replace with list of packets from dump
print("Transmission:", transmission)
while len(transmission) > 0:
    receive(transmission.pop())

def empty():
    for x in range(N):
        if(len(queues[x]) > 0):
            return False
    return True

while not empty():
    send()

print(lastVirFinish)