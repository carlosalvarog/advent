def createFrame(names : ):
    a = "pl"
    max_l=0
    a.__len__
    for n in names:
        if (n.__len__>max_l):
            max_l=len(n)
    margin="****"+"*"*max_l
    total=margin+"\n"
    for n in names:
        total+="* " + n+ " "*(max_l-len(n)) +"*\n"
    total+=margin
    return total