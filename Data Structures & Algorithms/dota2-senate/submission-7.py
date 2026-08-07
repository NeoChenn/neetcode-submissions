class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #iterate through senate array and create array of R indices and an array of D indices
        #keep track of how many Rs and Ds are remaining. 
        #if any == 0, return
        #keep a pointer at the start of each, "wrapping around", skipping "-1"s
        #let smaller index's val judge, "-1" the opposing team's current senate, +1 both pointers

        if 'R' not in senate:
            return "Dire"
        if 'D' not in senate:
            return "Radiant"

        rIndices = []
        dIndices = []
        rCount = 0
        dCount = 0
        for i in range(len(senate)):
            if senate[i] == 'R':
                rCount += 1
                rIndices.append(i)
            else:
                dCount += 1
                dIndices.append(i)

        r, d = 0, 0
        INF = float('inf')
        while True:
            ri = rIndices[r % len(rIndices)]
            di = dIndices[d % len(dIndices)]

            if ri < di:
                dIndices[d % len(dIndices)] = INF
                dCount -= 1
                rIndices[r % len(rIndices)] += len(senate)
            else:
                rIndices[r % len(rIndices)] = INF
                rCount -= 1
                dIndices[d % len(dIndices)] += len(senate)

            r += 1
            d += 1

            if rCount == 0:
                return "Dire"
            elif dCount == 0:
                return "Radiant"

            while rIndices[r % len(rIndices)] == INF:
                r += 1
            while dIndices[d % len(dIndices)] == INF:
                d += 1
