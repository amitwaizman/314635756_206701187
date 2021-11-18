from elevator import Elevator
import json
class bulding:

    def __init__(self, file) -> None:
       try:
        with open(file, "r+") as B:
          my_E = json.load(B)
          elevators_d = my_E["_elevators"]
          self.minFloor = my_E["_minFloor"]
          self.maxFloor = my_E["_maxFloor"]
          self.elevators = []
          for ele in elevators_d:
            E = Elevator(id=ele["_id"], speed=ele["_speed"], minFloor=ele["_minFloor"], maxFloor=ele["_maxFloor"],
                         closeTime=ele["_closeTime"],
                         openTime=ele["_openTime"], startTime=ele["_startTime"], stopTime=ele["_stopTime"])
            self.elevators.append(E)
          self.NumElevator = int(len(self.elevators))
       except IOError as e:
          print(e)


    def __str__(self) -> str:
        return f"{self.elevators}\nNumElevator: {self.NumElevator}"
    def __repr__(self) -> str:
        return f"{self.elevators}\nNumElevator: {self.NumElevator}"



