class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}
        left = 0
        min_len = float("infinity")
        min_sub = [-1, -1]

        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1
        
        need = len(hash_t)
        have = 0

        for right in range(len(s)):
            hash_s[s[right]] = hash_s.get(s[right], 0) + 1

            if s[right] in hash_t and hash_t[s[right]] == hash_s[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < min_len: ## be careful, should use if here
                    min_len = right - left + 1
                    min_sub = [left, right]
                
                hash_s[s[left]] -= 1

                if s[left] in hash_t and hash_t[s[left]] > hash_s[s[left]]: ## be careful, cannot use != 
                    have -= 1
                
                left += 1
        
        return "" if min_sub == [-1, -1] else s[min_sub[0]:min_sub[-1]+1]
