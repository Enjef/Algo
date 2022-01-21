class UndergroundSystem:  # 29.64% 29.15%

    def __init__(self):
        self.log = {}
        self.st = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.st[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cur = (self.st[id][0], stationName)
        if cur not in self.log:
            self.log[cur] = []
        self.log[cur].append(t-self.st[id][1])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_arr = self.log[(startStation, endStation)]
        return sum(time_arr)/len(time_arr)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

class UndergroundSystem_v2:  # 87.80% 10.84%

    def __init__(self):
        self.log = {}
        self.st = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.st[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cur = (self.st[id][0], stationName)
        if cur not in self.log:
            self.log[cur] = (t-self.st[id][1], 1)
        else:
            prev_avg, prev_qty = self.log[cur]
            self.log[cur] = (
                (prev_avg*prev_qty+t-self.st[id][1])/(prev_qty+1), prev_qty+1)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.log[(startStation, endStation)][0]

class UndergroundSystem_best_speed:

    def __init__(self):
        self.checkin = {}
        self.checkout = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startime = self.checkin[id]
        key = startStation +'-'+ stationName
        timeDiff = t - startime 
        time, count= self.checkout.get(key, (0, 0))
        self.checkout[key] = (time+timeDiff, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation +'-'+ endStation
        time, count= self.checkout.get(key, (0, 0))
        return  time/count

class UndergroundSystem_best_memory:

    def __init__(self):
        self.info = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.info[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.info[id][0]
        if (start, stationName) in self.trips:
            self.trips[(start, stationName)][0] += t - self.info[id][1]
            self.trips[(start, stationName)][1] += 1
        else:
            self.trips[(start, stationName)] = [t - self.info[id][1], 1]
        del self.info[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cur = (startStation, endStation)
        return self.trips[cur][0] / self.trips[cur][1]
