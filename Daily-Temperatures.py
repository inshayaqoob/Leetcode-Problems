from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result list with zeros
        stack = []  # Use a stack to keep track of indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If the current temperature is higher than the temperature at the top of the stack
                # It means we have found a higher temperature, so calculate the number of days and update the result
                j = stack.pop()
                result[j] = i - j

            stack.append(i)  # Push the current index onto the stack

        return result
