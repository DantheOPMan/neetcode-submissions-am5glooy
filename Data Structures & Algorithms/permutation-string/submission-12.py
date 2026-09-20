class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count_one = [0] * 26
        count_two = [0] * 26

        for i in range(len(s1)):
            count_one[ord(s1[i]) - ord('a')] +=1
            count_two[ord(s2[i]) - ord('a')] +=1
        
        equalCount = 0
        for i in range(26):
            if count_one[i] == count_two[i]:
                equalCount +=1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if equalCount == 26:
                return True
            
            charAdd = ord(s2[i]) - ord('a')
            count_two[charAdd] +=1
            if count_one[charAdd] == count_two[charAdd]:
                equalCount+=1
            elif count_one[charAdd] == count_two[charAdd] - 1:
                equalCount-=1

            charRemove = ord(s2[l]) - ord('a')
            count_two[charRemove] -=1
            if count_one[charRemove] == count_two[charRemove]:
                equalCount+=1
            elif count_one[charRemove] == count_two[charRemove] + 1:
                equalCount-=1
            l+=1
        return equalCount == 26
