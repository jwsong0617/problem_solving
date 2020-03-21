import sys
from collections import deque
dq = deque()
parenthesis = ["[", "]", "(", ")"]
while(1):
    dq.clear()
    sentense = sys.stdin.readline().rstrip()
    if(len(sentense)==1 and sentense[0]=="."):
        break
    else:
        sentense = sentense.strip().split()
    for word in sentense:
        if("[" in word or "]" in word or "(" in word or ")" in word):
            pass
        else:
            continue
        for char in word:
            if(len(dq)==0 and (char=="]" or char==")")):
                dq.append(-1)
                break
            if(char=="["):
                dq.append(char)
            elif(char=="]"):
                if(dq[-1]=="["):
                    dq.pop()
                else:
                    dq.append(-1)
                    break
            elif(char=="("):
                dq.append(char)
            elif(char==")"):
                if(dq[-1]=="("):
                    dq.pop()
                else:
                    dq.append(-1)
                    break
            else:
                continue
    if(len(dq)==0):
        print("yes")
    else:
        print("no")

