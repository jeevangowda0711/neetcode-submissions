class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # dic = {
        #     '(' : ')',
        #     '[' : ']',
        #     '{' : '}'
        # }
        
        # for c in s:
        #     if c in ['(', '{', '[']:
        #         stack.append(c)
        #     if c in [')', '}', ']']:
        #         if not stack:
        #             return False
        #         opening_brackect = stack.pop()
        #         if dic[opening_brackect] != c:
        #             return False
        # if stack:
        #     return False
        
        # return True

        dic = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if stack and (c in dic and stack[-1] == dic[c]):
                stack.pop()
            else:
                stack.append(c)
        
        return not stack