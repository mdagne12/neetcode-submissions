class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [0]
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > temperatures[stack[-1]]: 
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return result


        