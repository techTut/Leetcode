class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        
        wordLen = len(words[0])
        
        for i in range(len(s)):
            freq = Counter(words)
            match = 0
            for j in range(len(words)):
                nextIdx = i + j * wordLen
                word = s[nextIdx : nextIdx + wordLen]
                
                if word not in freq or freq[word] == 0:
                    break
                freq[word] -=1
                if freq[word] == 0:
                    match +=1
            if match == len(freq):
                result.append(i)
        return result
    