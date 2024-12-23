if __name__ == '__main__':
    N = int(input())
    lst = [] 
for _ in range(N):
    command = input().split() 
# Read the command and arguments
    action = command[0]
    if action == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif action == "print": 
        print(lst) 
    elif action == "remove":
        lst.remove(int(command[1]))
    elif action == "append":
        lst.append(int(command[1]))
    elif action == "sort": 
        lst.sort()
    elif action == "pop":
        lst.pop()
    elif action == "reverse": 
        lst.reverse()


"""insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""