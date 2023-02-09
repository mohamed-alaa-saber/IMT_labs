def cap(inp):
    inp_list=inp.split()
    out=" "
    for s in inp_list:
        out+=s.capitalize()
        out+=" "
    return out

def main():
    mysrt=str(input("enter"))
    mysrt=mysrt.split()
    
    for i,s in enumerate(mysrt):
        mysrt[i]=s.capitalize()
    
    mysrt=" ".join(mysrt)    
    print(mysrt)
    
    inp=str(input("enter"))
    cap(inp)
    print(cap(inp))
    




if __name__=="__main__":
    main()