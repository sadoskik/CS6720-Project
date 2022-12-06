import Packet
from random import randint
import WFQ
# import WF2Q
# import WRR

def main():
    iter = 10
    metric = {'droppedPackets':0, 'receivedBytes':0, 'sentBytes':0, 'latency':[0]*4}
    for _ in range(iter):
        total_packets = [[]]*4
        #initialize transmission packets
        for x in range(4):
            total_packets[x] = [Packet.Packet(src = x) for _ in range(randint(200, 500))]
            Packet.Packet.startTime = 0
        num_packets = [len(x) for x in total_packets]
        wfq = WFQ.WFQ()
        t = 0
        
        while sum([len(x) for x in total_packets]) != 0 or sum([len(x) for x in wfq.queues]) != 0 or t < wfq.currentPacketFinish:
            for packets in total_packets:
                if len(packets) == 0:
                    continue
                curr_packet = packets[0]                
                if curr_packet.time <= t:
                    wfq.receive(packets.pop(0))
            wfq.process(t)
            t += 1
        for x in range(4):
            metric["latency"][x] += wfq.metrics["latency"][x] / num_packets[x]
        
        for key in wfq.metrics:
            if(key == "latency"):
                continue
            metric[key] += wfq.metrics[key]
        print(wfq.metrics)
    for key in metric:
        if(key == "latency"):
            continue
        metric[key] /= iter
    for x in range(4):
        metric["latency"][x] /= iter
    print(metric)

        
        
        
        
if __name__ == '__main__':
    main()