Convert string to list, because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
Iterate through list
Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
When we come across close parenthesis we pop an element from the stack. If the stack is empty we replace current list element with an empty string
After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
Convert list to string and return

def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)
    
Time complexity is O(n)
Memory complexity is O(n)