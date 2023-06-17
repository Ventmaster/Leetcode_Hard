class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def depth_first_search(i, x):
            if i == len(arr1): return 0
            j = bisect_left(arr2, x+1)
            return min(
                depth_first_search(i+1, arr2[j]) + 1 if j < len(arr2) else 2001,
                depth_first_search(i+1, arr1[i]) if arr1[i] > x else 2001
            )

        result = depth_first_search(0, -1)
        if result != 2001: return result
        return -1
