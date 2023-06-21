class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        array = sorted(zip(nums, cost))
        middle = sum(cost)/2

        count = 0
        for x, y in array:
            count += y
            if count >= middle:
                return (sum(abs(x-n) * c for n,c in array))
