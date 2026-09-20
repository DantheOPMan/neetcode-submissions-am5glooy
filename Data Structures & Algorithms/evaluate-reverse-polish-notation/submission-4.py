class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "-":
                p1, p2 = stack.pop(), stack.pop()
                stack.append(p2 - p1)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "/":
                p1, p2 = stack.pop(), stack.pop()
                stack.append(int(float(p2) / p1))
            else:
                stack.append(int(n))

        return stack[0]