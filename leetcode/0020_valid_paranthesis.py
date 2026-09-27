class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        coup = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in ['(', '{', '[']:
               par.append(c)
            else:
                if not par:
                    return False
                if c == coup[par[-1]]:
                    par.pop()
                else:
                    return False

        if par:
            return False
        
        return True