class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        standard = Counter(chars)
        result = 0

        for word in words:

            curr_count = Counter(word)

            if curr_count < standard:
                result += len(word)
        
        return result 

        