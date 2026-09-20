class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        swap = {"}" : "{",")" : "(","]" : "[",}

        for n in s:
            if n in swap:
                if stack:
                    val = stack.pop()
                    if swap[n] != val:
                        return False
                else:
                    return False
            else:
                stack.append(n)


        return len(stack)== 0