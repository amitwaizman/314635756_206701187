# 314635756_206701187

1. 
a) https://www.youtube.com/watch?app=desktop&v=JXqVvmBOyyQ =Explains the main idea of the elevator algorithm

b)https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30

c)https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf 

We get a Json file with a building containing elevators and a csv file with elevator calls (time,source,destination) and we would like to insert the best elevator for each call,
There can be several problems and they are: there will be several readings at the same time when some readings go up and some come down, elevator stops and more ..

2.
Input: a json file containing a building with its elevators and a csv file with readings of the elevators.

Output:A csv file that assigns the best elevators

A classroom will be built that will keep the reading list for us, 
each reading on the list will contain the time the elevator will reach it,
the floor and the direction of reading.
In addition a function was built that would calculate which elevator would do the reading in the best time,
by calculating the arrival time of each elevator for each reading.

![image](https://user-images.githubusercontent.com/93525881/142434600-1b0d1e66-0074-48d8-b0f1-786c312f80c8.png)
