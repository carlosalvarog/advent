def tree_height(tree):
  # Write your code here
    h=0
    a={}
    
    toCheck=[]
    if tree!={} or tree["value"]!=None:
        toCheck.append({"d":1,"v":tree})
    else:
        return 0

    while True:
        print(toCheck)
        if len(toCheck)==0:
            return h
        else:
            if toCheck[0]["v"]["left"]!=None:
                if h<toCheck[0]["d"]+1:
                    h=toCheck[0]["d"]+1
                toCheck.append({"d":toCheck[0]["d"]+1, "v":toCheck[0]["v"]["left"]})
            if toCheck[0]["v"]["right"]!=None:
                    if h<toCheck[0]["d"]+1:
                        h=toCheck[0]["d"]+1
                    toCheck.append({"d":toCheck[0]["d"]+1, "v":toCheck[0]["v"]["right"]})
            
            toCheck.pop(0)
        
    return h

tree = {
    'value': '🎁',
    'left': {
        'value': '🎄',
        'left': {
            'value': '⭐',
            'left': None,
            'right': None
        },
        'right': {
            'value': '🎅',
            'left': None,
            'right': None
        }
    },
    'right': {
        'value': '❄️',
        'left': None,
        'right': {
            'value': '🦌',
            'left': None,
            'right': None
        }
    }
}
print(tree_height(tree))
