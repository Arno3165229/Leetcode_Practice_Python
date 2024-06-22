class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) ## remember

        for str in strs:
            chr_count = [0] * 26
            for c in str:
                chr_count[ord(c)-ord('a')] += 1
            anagram_map[tuple(chr_count)].append(str)
        
        anagram_res = []

        for key in anagram_map:
            anagram_res.append(anagram_map[key])

        return anagram_res