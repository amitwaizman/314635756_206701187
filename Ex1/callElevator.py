import csv


class callElevator:
    def __init__(self,time=0,sourceFloor=0,destFloor=0,status=0,elevator=0) -> None:
        self.time=time
        self.sourceFloor=sourceFloor
        self.destFloor=destFloor
        self.status=status
        self.elevator=elevator
        self.direction=self.dir()


    def __str__(self) -> str:
        return f"time:{self.time} sourceFloor:{self.sourceFloor} destFloor:{self.destFloor} status:{self.status} elevator:{self.elevator}"

    def __repr__(self) -> str:
        return f"time:{self.time} sourceFloor:{self.sourceFloor} destFloor:{self.destFloor} status:{self.status} elevator:{self.elevator}"

    def dir(self):
        if (self.sourceFloor < self.destFloor):
            return 1 #up
        else:
            return -1 #down
