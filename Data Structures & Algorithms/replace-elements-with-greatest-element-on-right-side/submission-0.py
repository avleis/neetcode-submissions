class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n_arr = [0] * len(arr)
        for i in range(len(arr)):
            r_j = n_arr[i]
            if i == len(arr) - 1:
                n_arr[-1] = -1
                return n_arr

            for j in range(i + 1, len(arr)):
                if arr[j] > r_j:
                    r_j = arr[j]
            n_arr[i] = r_j