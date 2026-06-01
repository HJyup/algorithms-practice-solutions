class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0 

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five >= 1:
                five -= 1
                ten += 1
            elif bill == 20:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            else:
                return False

        return True