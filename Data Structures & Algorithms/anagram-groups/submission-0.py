class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        mark = False
        for word in strs:
            sortedWord = ''.join(sorted(word))
            for section in output:
                if ''.join(sorted(section[0])) == sortedWord:
                    mark = True
                    section.append(word)
            if mark == False:
                output.append([word])
            mark = False
        return output
