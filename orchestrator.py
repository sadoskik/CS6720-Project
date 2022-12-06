import Packet
from random import randint
import WFQ
# import WF2Q
# import WRR

def main():
    iter = 10
    metric = {'droppedPackets':0, 'receivedBytes':0, 'sentBytes':0, 'latency':0}
    for _ in range(iter):
        total_packets = [[]]*4
        #initialize transmission packets
        for x in range(4):
            total_packets[x] = [Packet.Packet(src = x) for _ in range(randint(200, 500))]
            Packet.Packet.startTime = 0
        num_packets = sum([len(x) for x in total_packets])
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
        for key, val in wfq.metrics.items():
            if key == 'latency':
                metric[key] += val/num_packets
            else:
                metric[key] += val
    for key, val in metric:
        metric[key] = val/iter
    print(metric)

        
        
        
        
if __name__ == '__main__':
    main()