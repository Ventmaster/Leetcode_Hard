class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        length_of_nums = len(nums)
        modulo = 10**9+7

        def dfs(index, lower_bound, higher_bound):
            if higher_bound == lower_bound + 1:
                return 1
            
            if lower_bound < nums[index] < higher_bound:
                return (dfs(index+1, lower_bound, nums[index]) *dfs(index+1, nums[index], higher_bound) *math.comb(higher_bound - lower_bound - 2, nums[index] - lower_bound - 1)) % modulo 

            return dfs(index+1, lower_bound, higher_bound)

        return dfs(0,0,length_of_nums+1) - 1 
