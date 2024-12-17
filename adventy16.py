def remove_snow(s: str) -> str:
  # Code here
    i=0
    t=s
    while i<len(t)-1:
            print (t)
            if t[i]==t[i+1]:
                t=t[0:i]+t[i+2::]
                i=0
                continue
            i+=1
    return t



print(remove_snow("qwerr"))
