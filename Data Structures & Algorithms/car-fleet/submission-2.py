class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = list(zip(position, speed))
        stack = []

        for position, speed in sorted(data)[::-1]:
            stack.append((target-position) / speed)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
