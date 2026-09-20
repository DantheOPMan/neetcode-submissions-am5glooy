class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):

            while stack and n > stack[-1][0]:
                valN, valI = stack.pop()
                days[valI] = i - valI

            stack.append([n, i])

        return days