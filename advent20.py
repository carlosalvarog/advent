def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
  # Escribe tu código aquí
    keys1= set(received)
    m={}
    e={}
    keys2= set(expected)
 
    for k in set(keys1+keys2):
        a= expected.count(k)-received.count(k)
        if a>0:
            m[k]=a
        if a<0:
            e[k]=-a

    return {"missing":m, "extra":e}   
        

