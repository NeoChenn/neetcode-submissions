class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #keep track of how many 5$, 10$ or 20$ I have
        #calculate the change per customer. Return false if I have the change
        
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                    continue
                elif five >= 3:
                    five -= 3
                    continue
                else:
                    return False
        return True
