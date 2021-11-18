# A class that represents an elevator as given to us

class Elevator:
    def __init__(self,id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime) -> None:
        self.id=id
        self.speed=speed
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.closeTime=closeTime
        self.openTime=openTime
        self.startTime=startTime
        self.stopTime=stopTime
        self.direction=1 # 0-nothing, -1=down, 1=up



    def __str__(self) -> str:
        return f"id:{self.id} speed:{self.speed} minFloor:{self.minFloor} maxFloor:{self.maxFloor} closeTime:{self.closeTime}" \
               f" openTime:{self.openTime} startTime:{self.startTime} stopTime:{self.stopTime}"

    def __repr__(self) -> str:
        return f"id:{self.id} speed:{self.speed} minFloor:{self.minFloor} maxFloor:{self.maxFloor} closeTime:{self.closeTime}" \
               f" openTime:{self.openTime} startTime:{self.startTime} stopTime:{self.stopTime}"