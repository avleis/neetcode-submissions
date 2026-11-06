class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperatur in enumerate(temperatures):
            while stack and stack[-1][0] < temperatur:
                prev_temperatur, prev_index = stack.pop()
                result[prev_index] = index - prev_index
            stack.append([temperatur, index])

        return result
