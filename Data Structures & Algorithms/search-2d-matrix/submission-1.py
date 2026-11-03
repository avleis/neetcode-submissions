class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_matrix = 0
        high_matrix = len(matrix) - 1
        nums = [1] * len(matrix)
        
        while high_matrix >= low_matrix:
            mid = (high_matrix + low_matrix) // 2

            if target in matrix[mid]:
                nums = matrix[mid].copy()
                break
            elif (sum(matrix[mid]) / len(matrix[mid])) > target:
                high_matrix = mid - 1
            else: 
                low_matrix = mid + 1
        else: return False

        low_nums = 0
        high_nums = len(nums) - 1

        while high_nums >= low_nums:
            mid = (high_nums + low_nums) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high_nums = mid - 1
            else: 
                low_nums = mid + 1

        return False