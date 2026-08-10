class Solution:
    def isValid(self, s: str) -> bool:

        matches = {')': '(', ']': '[', '}': '{'}

        if len(s) % 2 != 0:
            return False
        
        stack = deque()

        for symbol in s:
            # if open bracket add to queue
            if symbol in matches.values():
                stack.append(symbol)
            # if close bracket check for match
            elif symbol in matches:
                if stack and stack[-1] == matches[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0



        