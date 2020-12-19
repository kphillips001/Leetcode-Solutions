# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            ')' : '(', 
            '}' : '{',
            ']' : '['
        }
        stack = []
        # for each char in s:
        for char in s:
            # if char in close_bracket_dict
            if char in close_brackets:
                # try to pop the stack
                # if the top of the stack doesn't match the close bracket                     
                # OR if the stack is emp
                if len(stack) == 0 or stack[-1] != close_brackets[char]:
                    return False
                else:
                    stack.pop()
            # if chart is NOT in close_bracket_dict:
            else:
                # add the bracket onto the stack
                stack.append(char)
        # check if the stack is not empty
        if len(stack) > 0: 
            return False
        # otherwise return true
        return True