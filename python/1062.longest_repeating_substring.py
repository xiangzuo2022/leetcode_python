# ChatGPT : rolling hash + binary search
class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def search(L):
            base = 26  # Base for rolling hash
            mod = 10**9 + 7  # Modulus for hash computation
            
            # Compute hash for the first L characters
            hash_val = 0
            for i in range(L):
                hash_val = (hash_val * base + ord(s[i])) % mod
            
            # Set of seen hash values
            seen = set([hash_val])
            
            base_L = pow(base, L, mod)  # Base^L modulo mod
            
            for i in range(1, len(s) - L + 1):
                # Compute hash for the next L characters
                hash_val = (hash_val * base + ord(s[i + L - 1]) - ord(s[i - 1]) * base_L) % mod
                
                if hash_val in seen:
                    return i
                
                seen.add(hash_val)
            
            return -1

        left, right = 1, len(s)
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            pos = search(mid)
            
            if pos != -1:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result