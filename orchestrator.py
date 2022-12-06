import Packet
from random import randint
import WFQ
# import WF2Q
# import WRR

def main():
    iter = 10
    for _ in range(iter):
        total_packets = [[]]*4
        #initialize transmission packets
        for x in range(4):
            total_packets[x] = [Packet.Packet(src = x) for _ in range(randint(200, 500))]
            Packet.Packet.startTime = 0
        
        last_packets = [total_packets[x][-1] for x in range(4)]
        final_t = max(x.time + x.size for x in last_packets)
        wfq = WFQ.WFQ()
        for t in range(final_t):
            for packets in total_packets:
                if len(packets) == 0:
                    continue
                curr_packet = packets[0]                
                if curr_packet.time <= t:
                    wfq.receive(packets.pop(0))
            wfq.process(t)
        print(wfq.metrics)
        
        
        
if __name__ == '__main__':
    main()