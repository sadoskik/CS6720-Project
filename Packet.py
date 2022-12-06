import random

class Packet:
    startTime = 0
    ports = 4
    def __init__(self, src=None):
        self.size = random.randint(1, 20)
        self.virFinish = None
        self.dst = random.randint(0, Packet.ports-1)
        self.time = Packet.startTime + random.randint(1,5)
        if(src):
            self.src = src
        else:
            self.src = random.randint(0, Packet.ports-1)
        Packet.startTime = self.time

    def __str__(self):
        return "<Packet(" + ", ".join([str(self.size), str(self.virFinish), str(self.dst)])

    def __repr__(self) -> str:
        return self.__str__()
