key = int(input())
message_length = int(input())
message = ""

for letter in range(0, message_length):
    symbol = input()
    message += chr(ord(symbol)+key)
print(message)