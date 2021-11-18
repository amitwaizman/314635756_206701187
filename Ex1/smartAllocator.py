from node import node
from Allocation import Allocation
#A class that places the reading in the best place
class smartAllocator:
    def __init__(self, elevatorPos, direction, route, elevator) -> None:
        self.elevatorPos = elevatorPos
        self.direction = direction
        self.route = route
        self.elevator = elevator

    # check the best Allocation
    def getAllocation(self, src, dest, time, timeSrc):
        if src < dest:
            routedire = 1
        else:
            routedire = -1
        if len(self.route) == 0:
            newRoute = []
            newRoute.append(node(src, timeSrc, routedire))
            t = self.sumTime(dest, timeSrc, newRoute, 0)
            newRoute.append(node(dest, t, routedire))
            return Allocation(newRoute, 0, 1)

        elevatorDire = self.direction
        if elevatorDire == routedire:
            if elevatorDire == 1:
                if src >= self.route[0].floor:
                    return self.getAllocationForSameDirectionWithMatch(src, dest, elevatorDire, timeSrc)
                else:
                    return self.getAllocationForSameDirectionWithConflict(src, dest, elevatorDire, timeSrc)
            else:
                if elevatorDire == -1:
                    if src <= self.route[0].floor:
                        return self.getAllocationForSameDirectionWithMatch(src, dest, elevatorDire, timeSrc)
                    else:
                        return self.getAllocationForSameDirectionWithConflict(src, dest, elevatorDire, timeSrc)
        else:
            if(self.direction==0):
                if(self.elevatorPos==src):
                    newRoute=self.route
                    t=self.sumTime(dest,timeSrc,newRoute,0)
                    newRoute.insert(0,node(dest,t,elevatorDire))
                    newRoute.insert(0,node(src,timeSrc,elevatorDire))
                    return Allocation(newRoute, 0, 1)

            return self.getAllocationForDiffDirection(src, dest, elevatorDire, timeSrc)

    def getAllocationForSameDirectionWithMatch(self, srcLevel, destLevel, elevatorDire, timeSrc):
        newRoute = self.route
        index = -1
        startIndex = endIndex = -1
        while endIndex == -1:
            if index == 0:
                if newRoute[index].floor == srcLevel:
                    startIndex = index
                index+=1
                continue
            if startIndex == -1:
                if index == len(newRoute):
                    startIndex = index
                    t = self.sumTime(srcLevel, timeSrc, newRoute, index)
                    newRoute.append(node(srcLevel, t, elevatorDire))
                    index += 1
                    continue
                if srcLevel * elevatorDire <= newRoute[index].floor * elevatorDire:
                    startIndex = index
                    if srcLevel != newRoute[index].floor:
                        t = self.sumTime(srcLevel, timeSrc, newRoute, index)
                        newRoute.insert(startIndex, node(srcLevel, t, elevatorDire))
                    index += 1
                    continue

                if newRoute[index].floor * elevatorDire < newRoute[index - 1].floor * elevatorDire:
                   t = self.sumTime(destLevel, timeSrc, newRoute, index)
                   newRoute.insert(index, node(destLevel, t, elevatorDire))
                   t = self.sumTime(srcLevel, timeSrc, newRoute, index)
                   newRoute.insert(index, node(srcLevel, t, elevatorDire))
                   startIndex = index
                   endIndex = index + 1
                   break
                index += 1
                continue

            if index == len(newRoute):
                endIndex = index
                t = self.sumTime(destLevel, timeSrc, newRoute, index)
                newRoute.append(node(destLevel, t, elevatorDire))
                break
            if destLevel == newRoute[index]:
                endIndex = index
                break
            if destLevel * elevatorDire < newRoute[index].floor * elevatorDire:
                endIndex = index
                t = self.sumTime(destLevel, timeSrc, newRoute, index)
                newRoute.insert(endIndex, node(destLevel, t, elevatorDire))
                break
            if newRoute[index].floor * elevatorDire < newRoute[index - 1].floor * elevatorDire:
                endIndex = index
                t = self.sumTime(destLevel, timeSrc, newRoute, index)
                newRoute.insert(endIndex, node(destLevel, t, elevatorDire))
                break
            index += 1
        return Allocation(newRoute, startIndex, endIndex)

    def getAllocationForDiffDirection(self, srcLevel, destLevel, elevatorDire, timeSrc):
        newRoute = self.route
        srcIndex = destIndex = -1
        index = 1
        if self.route[0] == srcLevel:
            srcIndex = 0
            index = 1
        while index < len(newRoute):
            if newRoute[index].floor < newRoute[index - 1].floor:
                break
            index += 1
        if index == len(newRoute):
            t = self.sumTime(srcLevel, timeSrc, newRoute, index)
            newRoute.append(node(srcLevel, t, elevatorDire))
            t = self.sumTime(destLevel, timeSrc, newRoute, index)
            newRoute.append(node(destLevel, t, elevatorDire))
            return Allocation(newRoute, index, index + 1)
        while index < len(newRoute):
            if srcIndex == -1:
                if newRoute[index].floor * elevatorDire <= srcLevel * elevatorDire:
                    srcIndex = index
                    if newRoute[srcIndex].floor != srcLevel:
                        t = self.sumTime(srcLevel, timeSrc, newRoute, index)
                        newRoute.insert(srcIndex, node(srcLevel, t, elevatorDire))
            else:
                if newRoute[index].floor * elevatorDire <= destLevel * elevatorDire:
                    destIndex = index
                    if newRoute[destIndex].floor != destLevel:
                        t = self.sumTime(destLevel, timeSrc, newRoute, index)
                        newRoute.insert(destIndex, node(destLevel, t, elevatorDire))
                    break
            index += 1

        if srcIndex == -1 or destIndex == -1:
            if index == len(newRoute):
                if srcIndex == -1:
                    t = self.sumTime(srcLevel, timeSrc, newRoute, index)
                    newRoute.append(node(srcLevel, t, elevatorDire))
                    t = self.sumTime(destLevel, timeSrc, newRoute, index)
                    newRoute.append(node(destLevel, t, elevatorDire))
                    srcIndex = index
                    destIndex = index + 1
                else:
                    destIndex = index
                    t = self.sumTime(destLevel, timeSrc, newRoute, index)
                    newRoute.append(node(destLevel, t, elevatorDire))
        return Allocation(newRoute, srcIndex, destIndex)

    def getAllocationForSameDirectionWithConflict(self, srcLevel, destLevel, elevatorDire, timeSrc):
        newRoute = self.route
        srcIndex = destIndex = -1
        i = 1
        # j=0
        for i in range(1,len(newRoute)):
        # while j < len(newRoute):
            if newRoute[i].floor * elevatorDire < newRoute[i-1].floor:
                i += 1
            break
        if i == len(newRoute):
            t = self.sumTime(srcLevel, timeSrc, newRoute, i)
            newRoute.append(node(srcLevel,t,elevatorDire))
            t = self.sumTime(destLevel, timeSrc, newRoute, i)
            newRoute.append(node(destLevel, t, elevatorDire))
            return Allocation(newRoute, i, i + 1)

        while i < len(newRoute)-1:
            i += 1
            if newRoute[i - 1].floor * elevatorDire < newRoute[i].floor * elevatorDire:
                peakLevel = newRoute[i - 1].floor
                firstAbovePeak = newRoute[i].floor
                if peakLevel * elevatorDire <= srcLevel * elevatorDire:
                    srcIndex = i - 1
                    if peakLevel != srcLevel:
                        t = self.sumTime(destLevel, timeSrc, newRoute, i)
                        newRoute.insert(srcIndex, node(srcLevel, t, elevatorDire))
                    else:
                        if srcLevel * elevatorDire <= firstAbovePeak * elevatorDire:
                            srcIndex = i
                        if srcLevel != firstAbovePeak:
                            t = self.sumTime(srcLevel, timeSrc, newRoute, i)
                            newRoute.insert(srcIndex, node(srcLevel, t, elevatorDire))
                    break
        if i == len(newRoute):
            if newRoute[i - 1].floor == srcLevel:
                t = self.sumTime(destLevel, timeSrc, newRoute, i)
                newRoute.append(node(destLevel, t, elevatorDire))
                return Allocation(newRoute, i - 1, i)
            t = self.sumTime(srcLevel, timeSrc, newRoute, i)
            newRoute.append(node(srcLevel, t, elevatorDire))
            t = self.sumTime(destLevel, timeSrc, newRoute, i)
            newRoute.append(node(destLevel, t, elevatorDire))
            return Allocation(newRoute, i, i + 1)

        if srcIndex != -1:
            while i < len(newRoute)-1:
                i += 1
                if newRoute[i].floor * elevatorDire <= destLevel * elevatorDire:
                    destIndex = i
                    if newRoute[i].floor != destLevel:
                        t = self.sumTime(destLevel, timeSrc, newRoute, i)
                        newRoute.insert(destIndex, node(destLevel, t, elevatorDire))
                    break
            if i == len(newRoute):
                destIndex = i
                t = self.sumTime(destLevel, timeSrc, newRoute, i)
                newRoute.append(node(destLevel, t, elevatorDire))
            else:
                while i < len(newRoute):
                    i += 1
                    if srcIndex == -1:
                        if newRoute[i].floor * elevatorDire <= srcLevel * elevatorDire:
                            srcIndex = i
                            if newRoute[i].floor != srcLevel:
                                t = self.sumTime(srcLevel, timeSrc, newRoute, i)
                                newRoute.insert(srcIndex, node(srcLevel, t, elevatorDire))
                            else:
                                if newRoute[i].floor * elevatorDire <= destLevel * elevatorDire:
                                    destIndex = i
                                if newRoute[i].floor != destLevel:
                                    t = self.sumTime(destLevel, timeSrc, newRoute, i)
                                    newRoute.insert(destIndex, node(destLevel,t,elevatorDire))
                            break

            if srcIndex == -1 or destIndex == -1:
                if srcIndex == -1:
                    t = self.sumTime(srcLevel, timeSrc, newRoute, i)
                    newRoute.append(node(srcLevel,t,elevatorDire))
                    t = self.sumTime(destLevel, timeSrc, newRoute, i)
                    newRoute.append(node(destLevel,t,elevatorDire))
                    srcIndex = i
                    destIndex = i + 1
                else:
                    t = self.sumTime(destLevel, timeSrc, newRoute, i)
                    newRoute.append(node(destLevel,t,elevatorDire))
                    destIndex = i

        return Allocation(newRoute, srcIndex, destIndex)

#A class that calculates the strain that the elevator will reach for reading
    def sumTime(self, floor, timeFloor, route, index):
        rem = 0
        if index == 0 or index == len(self.route):
            if index == 0 :
               time = timeFloor
            if index == len(self.route):
                time=route[index-1].time+abs(floor - route[index - 1].floor) / self.elevator.speed + self.elevator.closeTime + self.elevator.stopTime + self.elevator.openTime + self.elevator.startTime
        else:
           rem = abs(route[index].floor - route[index - 1].floor) / self.elevator.speed + self.elevator.closeTime + self.elevator.stopTime + self.elevator.openTime + self.elevator.startTime
           if route[index - 1].time + rem < timeFloor:
               time = timeFloor
           else:
               time = route[index - 1].time + rem
        while index < len(route):
            route[index].time = route[index].time + rem
            index += 1
        return time




