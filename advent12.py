
def calculate_price(ornaments: str) -> int:
    d= {"*":1,"o":5, "^":10, "#": 50, "@": 100}
    t=0
    l=list(d.keys())
    if "Z" in ornaments:
        return undefined
    ind=len(ornaments)-1
    for i in range (0,ind):
        if  l.index(ornaments[i+1])>l.index(ornaments[i]):
            t-=d[ornaments[i]]
        else:
            t+=d[ornaments[i]]
    
    t+=d[ornaments[len(ornaments)-1]]

    return t

print(calculate_price("***o*"))