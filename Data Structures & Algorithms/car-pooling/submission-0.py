class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sort trips by start time. Time travels linearly
        #At each unit time, pick up all passengers that start, and drop off all passengers that arrive
        #if at any time capacity < 0, return False. Otherwise, return True

        #hashmap stores time as key, value as net passenger flow 

        hashmap = {}
        for pas, start, end in trips:
            if start not in hashmap:
                hashmap[start] = 0
            if end not in hashmap:
                hashmap[end] = 0
            hashmap[start] -= pas
            hashmap[end] += pas 

        timeline = sorted(list(hashmap.items()))
        for time, pas in timeline:
            capacity += pas
            if capacity < 0:
                return False
        return True