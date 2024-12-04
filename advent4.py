def createXmasTree(ornament, height):
    t=""
    for l in range(0,height):
        nl= (height-l-1)*"_" + (1+2*l)*ornament+ (height-l-1)*"_" + "\n"
        t+=nl
    t+=((height-1)*"_" + "#"+ (height-1)*"_" + "\n")*2
    return t[:-1]
createXmasTree("o",20)