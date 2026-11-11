class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contador = {}
        for char in s:
            contador[char] = contador.get(char, 0) + 1
        for char in t:
            contador[char] = contador.get(char, 0) - 1
        for num in contador.values():
            if num != 0:
                return False
        else: 
            return True