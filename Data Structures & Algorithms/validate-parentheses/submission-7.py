class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        swap = {"}" : "{",")" : "(","]" : "[",}

        for n in s:
            if n in swap:
                if stack and stack[-1] == swap[n]:
                    val = stack.pop()
                else:
                    return False
            else:
                stack.append(n)


        return len(stack)== 0