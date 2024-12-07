def fix_packages(packages):
  # Code here
    while True:
        if packages.count("(")==0:
            return packages
        i=packages.rfind("(")
        f=packages[i,:].find(")")
        packages= packages[0:i] + packages[i+1:f][::-1] + packages[f+1:]
    
