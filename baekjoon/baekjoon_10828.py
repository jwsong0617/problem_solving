import sys
stack = []
N = int(sys.stdin.readline().rstrip())
for line in range(N):
    commands = sys.stdin.readline().rstrip().split()
    if(len(commands) > 1 and commands[0] == "push"):
        stack.append(int(commands[1]))
    else:
        command = commands[0]
        if command == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                del stack[-1]
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            if(len(stack) == 0):
                print(1)
            else:
                print(0)
        elif command == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
