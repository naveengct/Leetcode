class Solution(object):
    def topKFrequent(self, nums, k):
        
        def max(arr):
            m = float('-inf')
            temp = -1
            for i in arr:
                if m < arr[i]:
                    m = arr[i]
                    temp = i
            return temp       
        
        res = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in range(k):
            temp = max(d)
            res.append(temp)
            d[temp] = -1            
        return res