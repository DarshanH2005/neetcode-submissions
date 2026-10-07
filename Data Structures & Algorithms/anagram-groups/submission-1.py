class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            sortedword=" ".join(sorted(word))
            res[sortedword].append(word)

        return list(res.values())
        