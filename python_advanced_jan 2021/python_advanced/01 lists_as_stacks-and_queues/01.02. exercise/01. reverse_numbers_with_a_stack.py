line = input().split(" ")
stack = []

while line:
    stack.append(line.pop())
print(" ".join(stack))