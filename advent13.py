def is_robot_back(moves: str) -> bool | list[int]:
    start=[0,0]
    mov={"L":[-1,0], "R":[1,0], "U":[0,1], "D": [0,-1] }
    inverse= {"L":"R", "R":"L", "U":"D", "D":"U"}
    for i in range(0, len(moves)):
        if moves[i] in mov:
            start[0]+=mov[moves[i]][0]
            start[1]+=mov[moves[i]][1]
        else:
            if moves[i]=="*":
                start[0]+=mov[moves[i+1]][0]
                start[1]+=mov[moves[i+1]][1]
            if moves[i]=="!":
                start[0]+=mov[moves[i+1]][0]*-2
                start[1]+=mov[moves[i+1]][1]*-2
            if moves[i]=="?":
                n=moves[i+1]
                for j in range(0, len(moves)):
                    if j!=i+1:
                        
                        if ((moves[j]==n and moves[j-1]!=  "!") or     (moves[j]==inverse[n] and moves[j-1]==  "!")):
                            start[0]+=mov[moves[i+1]][0]*-1
                            start[1]+=mov[moves[i+1]][1]*-1                       
    if (start[0]==0 and start[1]==0):
        return True
    else:
        return start
print(is_robot_back('R?R'))