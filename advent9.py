from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    loc =(0,0)
    C,A=0,0
    match mov:
      case "U":
          A=-1
      case "D":
          A=1
      case "L":
          C=-1
      case "R":
          C=1 
    for i,f in enumerate(board):
        if board[i].find("@")!=-1:
            loc=i,board[i].find("@")
    if (loc[0]+A)<0 or (loc[0]+A)>=len(board) or (loc[1]+C)<0 or (loc[1]+C)>=len(board[0]):
        return "crash"
    else:
        print(board)
        print (loc[0]+A)
        print(loc[1]+C)
        char = board[loc[0]+A][loc[1]+C]
        print(char)
        if(char=="o"):
                return "crash"
        if(char=="*"):
                return "eat"
        if(char=="."):
                return "none"

    
print(move_train([
  "··@··",
  "··o··",
  "·*o··",
  "··o··",
  "··o··"
], 'D'))