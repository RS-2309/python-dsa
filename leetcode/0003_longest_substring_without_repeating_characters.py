class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        nr = ''
        for syllable in s:
            if syllable not in nr:
                nr += syllable
                if len(nr) > maximum:
                    maximum += 1
            else:
                syllable_index = nr.index(syllable)
                if len(nr) == syllable_index:
                    nr = ''
                else:
                    nr = nr[nr.index(syllable)+1:] + syllable
        return maximum