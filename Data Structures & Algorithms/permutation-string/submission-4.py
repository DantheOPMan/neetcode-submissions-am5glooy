class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1S = [0] * 26
        count2S = [0] * 26
        for i in range (len(s1)):
            count1S[ord(s1[i]) - ord('a')] +=1
            count2S[ord(s2[i]) - ord('a')] +=1

        equalCount = 0
        for i in range(26):
            if count1S[i] == count2S[i]:
                equalCount +=1
        left = 0
        for i in range(len(s1), len(s2)):
            if equalCount == 26:
                return True
            charNum = ord(s2[i])- ord('a')
            count2S[charNum] += 1
            if count2S[charNum] == count1S[charNum]:
                equalCount +=1
            elif count2S[charNum] == count1S[charNum] + 1:
                equalCount -=1

            charNum = ord(s2[left])- ord('a')
            count2S[charNum] -= 1
            if count2S[charNum] == count1S[charNum]:
                equalCount +=1
            elif count2S[charNum] == count1S[charNum] -1:
                equalCount -=1

            left +=1

        return equalCount == 26