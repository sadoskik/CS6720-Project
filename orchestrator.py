import Packet
from random import randint
import WFQ
import WF2Q
import WRR

wfq = WFQ.WFQ()
wfq.process()
for _ in range(1000):
    ports = [[]]*4
    for x in range(4):
        ports[x] = [Packet() for x in range(randint(200, 500))]
        Packet.Packet.startTime = 0

while (1):
    for inputPort in ports:
        WFQ.enqueue(inputPort.pop())
    WFQ.process()