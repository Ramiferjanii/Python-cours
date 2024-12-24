# Read input
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

# Process commands
for _ in range(n_commands):
    cmd = input().split()
    command = cmd[0]
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(cmd[1]))
    elif command == "discard":
        s.discard(int(cmd[1]))

# Print the sum of the elements in the set
print(sum(s))




