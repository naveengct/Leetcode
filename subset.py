class Solution(object):
    def subsets(self, nums):
        l1 = [[]]
        l2 = []
        for i in nums:            
            while(len(l1) != 0):
                temp = l1.pop()
                if temp == []:
                    l2.append(temp[::])
                    l2.append([i][::])
                else:
                    l2.append(temp[::])
                    temp.append(i)
                    l2.append(temp[::])
            l1 = l2
            l2 = []
        return l1
                
        