class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            brute force solution:
                For each index i, start at such a station

                add gas[i] gas to tank, remove cost[i] gas from tank and increment i
                if tank < 0, continue to next iteration
                if back at original index, return original index 
                repeat until one of those statements return true

                if for loop exited, return -1

        """

        for i in range(len(gas)):
            j = i
            tank = 0
            while True:
                tank += gas[j % len(gas)]
                tank -= cost[j % len(gas)]
                j += 1
                if tank < 0:
                    break
                if j % len(gas) == i:
                    return i
        return -1