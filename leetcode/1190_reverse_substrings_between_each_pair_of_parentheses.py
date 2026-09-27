class Solution:
    def reverseParentheses(self, s: str) -> str:
        l = []
        for i in s:
            l.append(i)

        d = {'(':[]}

        for index, item in enumerate(l):
            if item == '(':
                d['('].append(index)

            if item == ')':
                i = d['('].pop()
                l[i:index+1] = l[i:index+1][::-1]

        s_new = ''.join(x for x in l if x not in '()')

        return s_new