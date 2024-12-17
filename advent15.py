def draw_table(data: list[dict[str, str | int]]) -> str:
  # Code here
  # Code here
    t=""
    k1= list(data[0].keys())[0]
    k2= list(data[0].keys())[1]
    maxlen1=len(k1)
    maxlen2=len(k2)

    for a in data:
        l2=len(str(a[k2]))
        l1=len(str(a[k1]))
        if maxlen2<=l2:
            maxlen2=l2
        if maxlen1<=l1:
             maxlen1=l1
        
      
    up="+-"+"-"*maxlen1+"-+-"+"-"*maxlen2+"-+"
    t+=up+"\n"
    
    t+="| " + k1.title()+" "*(maxlen1-len(k1))+ " | "+ k2.title()+" "*(maxlen2-len(k2)) + " |\n" 
    t+=up+"\n"
    for d in data:
            p=d[k1]
            p2=str(d[k2])
            t+="| " + p+" "*(maxlen1-len(p))+ " | "+ p2+" "*(maxlen2-len(p2)) + " |"+"\n"
    t+=up
    return t

a = [
  { "name": 'Alice', "city": 'London' },
  { "name": 'Bob', "city": 'Paris' },
  { "name": 'Charlie', "city": 'New York' }
]

b=[
        { "gift": 'Doll', "quantity": 10 },
        { "gift": 'Book', "quantity": 5 },
        { "gift": 'Music CD', "quantity": 1 }
      ]
d=[{"a":"","b":""}]
print(draw_table(d))


