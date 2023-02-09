
def main():
    N=int(input("number of operations"))
    l=list()
    for i in range(N):
        todo=input()
        g=todo.split(" ")
        print(g)
        if g[0]=="insert":
            ind=int(g[1])
            ob=int(g[2])
            # l.insert(int(g[1]),int(g[2]))
            l.insert(ind,ob)
        elif g[0]=="remove":
            re=int(g[1])
            # l.remove(int(g[1]))
            l.remove(re)
        elif g[0]=="print":
            print(l)
            

    

if __name__=="__main__":
    main()