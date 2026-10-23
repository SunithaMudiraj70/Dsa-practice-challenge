'''Recognize it when: You need to match brackets, undo recent operations, evaluate expressions, or find the next greater/smaller element.

Example: Valid parentheses.'''
def is_valid(s):
    pairs={")": "(", "]": "[", "}": "{"}
    stack=[]
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop!=pairs[ch]:
                return False
    return len(stack)==0