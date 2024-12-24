if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # Convert map to list
    
    max_score = max(arr)  # Find the maximum score
    
    # Remove all occurrences of the maximum score
    while max_score in arr:
        arr.remove(max_score)
    
    # The new maximum score is the runner-up score
    runner_up_score = max(arr)
    print(runner_up_score)


    """if name == 'main': This line checks if the script is being run directly (not imported as a module). If it is, the following code block will be executed.

n = int(input()): This line takes an integer input n, which represents the number of scores in the list.

arr = list(map(int, input().split())): This line reads a line of input, splits it into separate strings, converts each string to an integer, and then stores the resulting integers in a list called arr.

max_score = max(arr): This line finds the maximum score in the list arr and stores it in the variable max_score.

while max_score in arr:: This line starts a loop that will continue as long as max_score is found in the list arr.

arr.remove(max_score): Within the loop, this line removes the first occurrence of max_score from the list arr. Since the loop runs as long as max_score is in the list, it removes all occurrences of the maximum score.

runner_up_score = max(arr): After all the occurrences of the maximum score have been removed, this line finds the new maximum score in the list arr, which is the runner-up score.

print(runner_up_score): Finally, this line prints the runner-up score."""