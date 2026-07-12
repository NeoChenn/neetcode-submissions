class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #[1, 2, 2, 3, 3, 4, 4, 5]       #[1, 2, 3, 3, 4, 5, 6, 7]
        #[-1, -1, 2, -1, 3, -1 ,4, 5]
        #iterate through the array (len(hand) / groupsize) times. If not integer, return False
        #create lists, replace hand element with -1 and if array empty at the end, return True

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        for i in range((len(hand) // groupSize)):
            count = 0
            prev = -1
            for i in range(len(hand)):
                if count == groupSize:
                    break
                if hand[i] == -1 or hand[i] == prev:
                    continue
                if count == 0:
                    prev = hand[i]
                    hand[i] = -1
                    count += 1
                elif hand[i] == prev + 1:
                    prev += 1
                    hand[i] = -1
                    count += 1
                
            if count != groupSize:
                return False
        
        return True
        
                
                
                