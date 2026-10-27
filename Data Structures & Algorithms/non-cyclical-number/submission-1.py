class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(num):
            total = 0
            while num > 0:
                d = num % 10
                num = num // 10
                total = total + d*d
            return total
        temp = n

        while temp != 1:
            temp = sq(temp)
            if len(str(temp)) == 1 and temp != 1:
                return False
                

        return True