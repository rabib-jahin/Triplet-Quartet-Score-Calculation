import re
def search(string):
    items=re.findall(r'\b[A-Za-z0-9]+\b',string)
    return items

def extract_items(string):
    items = []
    stack = []

    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if len(stack) > 0:
                start = stack.pop()
                items.append(string[start:i+1])

    return items


