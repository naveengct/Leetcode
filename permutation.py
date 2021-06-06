class Solution(object):
    def permute(self, nums):
        res = []
        def per(num,l,r):
            if l == r:
                res.append(num[::])
            else:
                for i in range(l,r+1):
                    num[l] , num[i] = num[i] , num[l]                    
                    per(num , l+1, r)
                    num[l] , num[i] = num[i] , num[l]
        per(nums, 0, len(nums)-1)
        return res
        
        
        