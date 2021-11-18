import csv
import sys

from elevator import Elevator
from callElevator import callElevator
from smartElevator import smartElevator
from bulding import bulding

class algo:
#
    def __init__(self,Building, Calls,Out) -> None:
        self.Out=Out
        self.build = bulding(Building)
        self.call = self.load_csv(Calls)
        self.elevatorsData = []
        i=0
        while i < self.build.NumElevator:
            self.elevatorsData.append(smartElevator(self.build.elevators[i]))
            i += 1
        self.readCall()
#A function that sends a single call
    def readCall(self):
        i = 0
        ca = []
        while i < len(self.call):
            bestElevator = self.callEl(self.call[i])
            c = ["Elevator call", self.call[i].time, self.call[i].sourceFloor, self.call[i].destFloor, self.call[i].status, bestElevator]
            ca.append(c)
            i += 1
        with open(self.Out, "w", newline="") as file:
             writer = csv.writer(file)
             writer.writerows(ca)
        file.close()
#A function that places the best elevator
    def callEl(self,call):
        timeToArrive =[]
        for elevator in self.elevatorsData:
           timeToArrive.append(elevator.getTime(call))

        bestElevatorIndex = 0
        bestTime = timeToArrive[0]
        i = 0
        while i < len(timeToArrive):
          currTime = timeToArrive[i]
          if currTime < bestTime:
             bestTime = currTime
             bestElevatorIndex = i
          i += 1
        bestElevator = self.elevatorsData[bestElevatorIndex]
        bestElevator.assignCall(call)
        return bestElevatorIndex

#Function reads from the csv file of the calls
    def load_csv(self,Calls):
        c = []
        try:
         with open(Calls) as file:
                csvcall = csv.reader(file)
                for row in csvcall:
                    if(len(row)!=0):
                       call = callElevator(time=float(row[1]), sourceFloor=int(row[2]), destFloor=int(row[3]), status=int(row[4]), elevator=int(row[5]))
                       c.append(call)
                return c
        except IOError as e:
           print(e)

if __name__ == '__main__':
    file = sys.argv[1:]
    algo(file[0], file[1],file[2])






