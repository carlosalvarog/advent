from typing import List
def comp(instructions: List[str]):
        d= {}
        i=0
        while i<len(instructions):
                inst=instructions[i]
                if inst[0:3]=="MOV":
                        n, r= inst[4::].split(" ")
                        if n.isnumeric():    
                            d[r] = int(n)
                        else:
                                if n not in d:
                                    d[n] = 0     
                                d[r]=d[n]
                        i+=1
                        continue
                elif inst[0:3]=="INC":
                        if inst[-1] not in d:
                            d[inst[-1]] = 0
                        d[inst[-1]] += 1
                        i+=1
                        continue
                elif inst[0:3]=="DEC":
                        if  inst[-1] not in d:
                            d[inst[-1]] = 0
                        d[inst[-1]] -= 1
                        i+=1
                        continue
                elif inst[0:3]=="JMP":
                       if d[inst[4]]==0:
                              i=int(inst[-1])
                              continue
                       else:
                              i+=1
                              continue
        print(d)       
        if  "A" not in d:
               return undefined
        else:
               return d["A"]


instas = [
  "MOV 2 X",
  "DEC X",
  "DEC X",
  "JMP X 1",
  "MOV X A"
]
print(comp(instas))
