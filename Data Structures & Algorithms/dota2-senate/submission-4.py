from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)

        n = len(senate)
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            if r < d:
                rq.append(r + n)  # R wins, gets next turn (add n to simulate next round)
            else:
                dq.append(d + n)  # D wins

        return "Radiant" if rq else "Dire"