def draw_race(indices, length):
  t=""
  for i,c in enumerate(indices):
    empt=(len(indices)-i)
    carril=list("~"*length)
    if c==0:
      continue
    else:  
        carril[c]="r"
    t+=" "*empt+ "".join(carril) +" /"+ str(i+1)+ "\n"

  print(t)
  return t

draw_race([2,-1, 5,0],10)