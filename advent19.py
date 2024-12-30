def distribute_weight(weight: int) -> str:
    boxRepresentations = {
  1: [" _ ", "|_|"] ,
  2: [" ___ ", "|___|"],
  5: [" _____ ", "|     |", "|_____|"],
  10: [" _________ ", "|         |", "|_________|"]
  }
    d={10:0,5:0,2:0,1:0}
    if(weight >= 10):

        d[10]=weight//10
        weight-=d[10]*10
    if(weight >= 5):
        d[5]=weight//5
        weight-=d[5]*5
    if(weight >= 2):
        d[2]=weight//2
        weight-=d[2]*2
    if(weight >= 1):
        d[1]=weight//1
        weight-=d[1]*1

    print(d)
    t=""
    if d[10]>0:
        t+=boxRepresentations[10][0] +   boxRepresentations[10][0][1::] *max((d[10]-1),0)+ "\n"
        t+=boxRepresentations[10][1] +   boxRepresentations[10][1][1::] *max((d[10]-1),0)+"\n"

        t+=boxRepresentations[10][2] +   boxRepresentations[10][2][1::] *max((d[10]-1),0)+"\n"
    if t!="" and d[5]==1:
        t="|" + t[1:6]+"|" +t[7::]
        t=" _____ \n|     |\n"+t
    print(t)

distribute_weight(29)

