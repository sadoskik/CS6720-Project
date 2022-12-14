import sys
import random
import Packet 

N = 4 #number of queues
GPS_time = 0
Packet.startTime = GPS_time
Packet.ports = N
queues = []
lastVirFinish = []
weights = []
R = [0]*N
for x in range(N):
    queues.append([])
    lastVirFinish.append(0)
    weights.append(random.randint(1,5))
    
for x in range(N):
    R[x] = weights[x] / (sum(weights))

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
        if len(queue) == 0:
            continue
        print(queue[-1])
        print(GPS_time)
        if queue[-1].virFinish < minVirFinish and queue[-1].time < GPS_time:
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
    GPS_time += packet.size()
    return packet

def chooseQueue(packet):
    return packet.dst



transmission = [Packet(random.randint(0,N-1)) for _ in range(100)]

for x in transmission:
    receive(x)

def empty():
    for x in range(N):
        if(len(queues[x]) > 0):
            return False
    return True

while not empty():
    send()

print(lastVirFinish)

