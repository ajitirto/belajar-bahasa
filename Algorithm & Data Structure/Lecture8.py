class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(),"Antrian sedang kosong."
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.isEmpty(),"Antrian sedang kosong."
        return self.qlist[0]
    def getRearMost(self):
        assert not self.isEmpty(),"Antrian sedang kosong."
        return self.qlist[-1]
    def deqAll(self):
        for i in range(len(self.qlist)):
            print(self.dequeue())
        
K=Queue()
K.enqueue(1)
K.enqueue(2)
K.enqueue(3)
K.enqueue(4)
K.enqueue(5)

class PriorityQueue(object):
    def __init__(self):
        self.qlist=[]
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self,item,priority):
        entry=_PriorityQEntry(item,priority)
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty(),"Antrian sedang kosong."
        fewest=self.qlist[0].priority;result=0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority<fewest:
                result=i
                fewest=self.qlist[i].priority
        return self.qlist.pop(result)
    def deqAll(self):
        for i in range(len(self.qlist)):
            print(self.dequeue().item)

class _PriorityQEntry(object):
    def __init__(self,data,priority):
        self.item=data
        self.priority=priority
    
Q=PriorityQueue()
Q.enqueue("Dyaksa",10)
Q.enqueue("W",2)
Q.enqueue("u",6)
Q.enqueue("a",2)
Q.enqueue("y",5)
Q.enqueue("h",2)
Q.enqueue(".",7)
Q.enqueue("Hyuma",1)
