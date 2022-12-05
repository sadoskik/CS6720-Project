import sys
import time
import random
import Packet

class WFQ:
    def __init__(self):
        self.N = 4
        startTime = time.time()
        Packet.startTime = startTime
        Packet.ports = N
        self.queues = []
        self.lastVirFinish = [0,0,0,0]
        self.weights = [2,3,4,3]
        self.updateR()
    def updateR(self):    
        for x in range(self.N):
            self.R[x] = self.weights[x] / (sum(self.weights))

    def receive(self, packet):
        queueNum = self.chooseQueue(packet)
        self.queues[queueNum].append(packet)
        self.updateTime(packet, queueNum)


    def selectQueue(self):
        i = 0
        minVirFinish = sys.maxsize
        queueNum = -1
        while i < len(self.queues):
            queue = self.queues[i]
            print("Queue:", i)
            print(queue)
            if len(queue) != 0 and queue[-1].virFinish < minVirFinish:
                minVirFinish = queue[-1].virFinish
                queueNum = i
            i += 1
        return queueNum

    def updateTime(self, packet, queueNum):
        nonEmpty = len([x for x in len(self.queues) != 0])
        virStart = max(packet.time/nonEmpty, self.lastVirFinish[queueNum])
        
        packet.virFinish =  virStart + packet.size/self.R[queueNum]
        self.lastVirFinish[queueNum] = packet.virFinish

    def send():
        queueNum = selectQueue()
        if queueNum == -1:
            print("Bad queue")
            exit()
        packet = queues[queueNum].pop()
        return packet

    def chooseQueue(packet):
        return packet.src






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