shoes1 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38},
    {'type': 'R', 'size': 42},
    {'type': 'I', 'size': 41},
    {'type': 'I', 'size': 42}
]

def organizeShoes(shoes):
    dictsz={}
    shoes2=[]
    for zp in shoes:
        if zp["size"] not in dictsz:
            dictsz[zp["size"]]={"I":0,"R":0}
        if zp["type"]=="I":
            dictsz[zp["size"]]["I"]+=1
        if zp["type"]=="R":
            dictsz[zp["size"]]["R"]+=1
    print(dictsz)
    for size in dictsz.keys():
        shoes2+=min( dictsz[size]["I"],dictsz[size]["R"] )*[size]
    print(dictsz)
    print(shoes2)

organizeShoes(shoes1)
