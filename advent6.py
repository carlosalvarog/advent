inBox([
  "####",
  "#* #",
  "#  #",
  "####"
])
def in_box(box):
    for l in box[1,:-1]:
        if("*" in l and (l.index("*")>0 and l.index("*")<len(l-1))):
            return True
    return False

