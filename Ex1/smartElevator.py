from smartAllocator import smartAllocator
from callElevator import callElevator
from Allocation import Allocation

#A class that contains an elevator and a list that symbolizes its route
class smartElevator:
    def __init__(self,elevator) -> None:
        self.elevator=elevator
        self.Route =[]

#A function that returns the position of the elevator
    def posElevator(self,call:callElevator):
        i=1
        if (len(self.Route)==0):
            return self.elevator.minFloor
        while i < len(self.Route)-1:
            if (call.time <= self.Route[i-1].time) and (call.time>=self.Route[i].time):
                return self.Route[i-1].floor
            else:
                i+=1
        return self.Route[i].floor
#check the tume that get the elevator to arrive
    def getTime(self,call:callElevator):
        time = 0
        pos = self.posElevator(call)
        allocation = self.getAllocation(call, call.sourceFloor, call.destFloor, pos)
        if pos == allocation.route[0].floor:  # same floor
            time = 0
        else:
            time = abs(pos - allocation.route[0].floor) / self.elevator.speed + self.elevator.openTime

        length = len(allocation.route)
        i=0
        while i < length:
                time += self.elevator.closeTime + (abs(allocation.route[i - 1].floor - allocation.route[i].floor))/self.elevator.speed + self.elevator.openTime
                i+=1
        return time
    #A function that handles reading
    def assignCall(self,call:callElevator):
        pos=self.posElevator(call)
        abc = self.getAllocation(call, call.sourceFloor, call.destFloor, pos)
        self.Route = abc.route
    #A function that sends to the best trajectory
    def getAllocation(self,call, src, dest, pos):
        return smartAllocator(pos, self.elevator.direction, self.Route, self.elevator).getAllocation(src, dest, 0, call.time)
