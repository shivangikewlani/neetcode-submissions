class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []
        while l < r:
            ele = numbers[l]+numbers[r]
            if ele>target:
                r-=1
            elif ele<target:
                l+=1
            else:
                return [l+1,r+1]

        