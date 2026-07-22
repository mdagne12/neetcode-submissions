class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        index = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while index and temperatures[i] > temperatures[index[-1]]:
                prev_day = index.pop()
                result[prev_day] = i - prev_day 
            
            index.append(i)

        return result
            
                
        