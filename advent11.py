def decode(filename):
    p=filename.split("_")
    nog=p[1:].join("")
    f=nog.split(".")[1:]
    ff=f[0:len(f)].join("")
    return ff