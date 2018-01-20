class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0 or n == 1:
            return '1'
        
        i = 2
        prev = '1'
        
        while i <= n:
            nxt = ''
            curr = prev[0]
            count = 0
            for elem in prev:
                if elem == curr:
                    count = count + 1
                else:
                    nxt = nxt + str(count) + curr
                    curr = elem
                    count = 1
            nxt = nxt + str(count) + curr        
            prev = nxt     
            i = i + 1
        
        return prev