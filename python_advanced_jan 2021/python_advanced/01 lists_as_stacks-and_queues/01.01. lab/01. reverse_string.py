text = input()
stack = []
for char in text:
    stack.append(char)
result = ""
while stack:
    result += stack.pop()
print(result)