class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            data = [0] * 26
            for c in s:
                data[ord(c)-ord('a')] +=1
            res[tuple(data)].append(s)
        return list(res.values())
            