class Solution(object):
    def generateParenthesis(self, n):
        arr = [''] * n * 2
        res = []
        def gen(arr, n, pos, start, end):
            if end == n:
                str = ""
                for i in arr:
                    str += i
                res.append(str[::])
                return
            else:
                if start > end:
                    arr[pos] = ')'
                    gen(arr, n, pos+1, start, end+1)
                if start < n:
                    arr[pos] = '('
                    gen(arr, n, pos+1, start+1, end)

        
        gen(arr, n, 0, 0, 0)
        return res