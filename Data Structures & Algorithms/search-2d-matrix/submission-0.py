class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high = len(matrix[i]) - 1
            nums = matrix[i].copy()

            while high >= low:
                mid = (high + low) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid - 1
                else: 
                    low = mid + 1

        return False