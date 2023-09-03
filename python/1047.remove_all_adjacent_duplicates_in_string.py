class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return None
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()               
            else:
                stack.append(ch)
        return ''.join(stack)
    
# chatgpt 碰碰车就用stack

def removeDuplicates(s):
    stack = []  # Initialize an empty stack
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the top element from the stack if it matches the current character
        else:
            stack.append(char)  # Otherwise, push the current character onto the stack
    
    # Convert the stack to a string and return
    return ''.join(stack)

# Example usage
s = "abbaca"
result = removeDuplicates(s)
print(result)  # Output: "ca"
