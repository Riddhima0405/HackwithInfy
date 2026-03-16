 def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            stack=[]
            next_g={ }
            for num in nums2:
                while  stack and num>stack[-1]:
                    smaller=stack.pop()
                    next_g[smaller]=num
                stack.append(num)
            while stack:
                next_g[stack.pop()]=-1
            res=[]
            for num in nums1:
                res.append(next_g[num])
            return res
