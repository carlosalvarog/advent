
def find_in_agenda(agenda: str, phone: str) -> dict | None:

    d={}
    l = agenda.split("\n")

    for i,val in enumerate(l):
        line=val
        name1= line.index("<")
        name2= line[name1::].find(">")
        name=line[name1+1: name1+name2]
        line= line[0:name1] + line[name1+name2+1::]
        print(name)        
        next1=line.find("+")
        

        nextSpace=next((i for i,x in  enumerate(line[next1+1::]) if (not x.isnumeric() and x!="-"  )), len(line[next1+1::]))
        number= line[next1:next1+nextSpace+1]
        print(number)
        line=line[0:next1]+ line[next1+nextSpace+1::]
        print(line)
        if line[0]==" ":
            line=line[1::]
        if line[-1]==" ":
            line=line[0:-2]
        d[number]={"name":name,"address":line }

        print(d)
    r=None
    k=""
    for key, value in d.items():
        if phone in key:
            if r==None:
                r=value
                k=key

            elif r!=None:
                return None
    if r!=None:
        return r

print(find_in_agenda(
  "+34-600-123-456 Calle Gran Via 12 <Juan Perez>\nPlaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"
, "654"))