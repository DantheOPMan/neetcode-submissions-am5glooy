class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        data1 = [0] * 26
        data2 = [0] * 26

        for i in range(len(s1)):
            data1[ord(s1[i]) - ord('a')] +=1
            data2[ord(s2[i]) - ord('a')] +=1
        
        equalCount = 0
        for i in range(26):
            if data1[i] == data2[i]:
                equalCount +=1

        left = 0
        for i in range(len(s1), len(s2)):
            if equalCount == 26:
                return True
            
            c = ord(s2[i]) - ord('a')
            data2[c] +=1
            if data2[c] == data1[c]:
                equalCount +=1
            elif data2[c] == data1[c] + 1:
                equalCount -=1

            c = ord(s2[left]) - ord('a')
            data2[c] -=1
            if data2[c] == data1[c]:
                equalCount +=1
            elif data2[c] == data1[c] - 1:
                equalCount -=1
            left +=1
        
        return equalCount == 26