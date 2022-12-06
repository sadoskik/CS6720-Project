import sys
import time
import random
import Packet

class WFQ:
    def __init__(self):
        self.N = 4
        self.maxQueueSize = 10000
        startTime = time.time()
        Packet.startTime = startTime
        Packet.ports = self.N
        self.currentPacketFinish = 0
        self.queues = [[]] * 4
        self.lastVirFinish = [0,0,0,0]
        self.weights = [2,3,4,3]
        self.weightSum = sum(self.weights)
        self.R = [0]*4
        for x in range(self.N):
            self.R[x] = self.weights[x] / (sum(self.weights))
        self.time = 0
        self.virtualTime = 0
        self.lastRealTime = 0
        self.metrics = {
            "droppedPackets": 0,
            "receivedBytes": 0,
            "sentBytes": 0,
            "latency": 0
        }

    def receive(self, packet):
        queueNum = self.chooseQueue(packet)
        self.metrics["receivedBytes"] += packet.size
        if(sum([x.size for x in self.queues[queueNum]]) + packet.size > self.maxQueueSize):
            self.metrics["droppedPackets"] += 1
            return
        self.queues[queueNum].append(packet)
        self.updateTime(packet, queueNum)


    def selectQueue(self):
        i = 0
        minVirFinish = sys.maxsize
        queueNum = -1
        while i < len(self.queues):
            queue = self.queues[i]
            # print("Queue:", i)
            # print(queue)
            if len(queue) != 0 and queue[0].virFinish < minVirFinish:
                minVirFinish = queue[0].virFinish
                queueNum = i
            i += 1
        return queueNum

    def updateTime(self, packet, queueNum):
        virStart = max(packet.time/ self.weightSum, self.lastVirFinish[queueNum])
        packet.virFinish =  virStart + packet.size/self.R[queueNum]
        self.lastVirFinish[queueNum] = packet.virFinish

    def send(self):
        queueNum = self.selectQueue()
        if queueNum == -1:
            print("Bad queue")
            return
        packet = self.queues[queueNum].pop(0)
        self.currentPacketFinish = packet.size + self.time
        self.metrics["sentBytes"] += packet.size
        self.metrics["latency"] += self.time - packet.time
        return packet

    def chooseQueue(self, packet):
        return packet.src
    
    def numEmpty(self):
        sum = 0
        for x in range(self.N):
            if (len(self.queues[x]) > 0):
                sum += 1
        return sum
    def process(self, time):
        self.time = time
        if(time < self.currentPacketFinish):
            return 1
        self.send()
        return 0
