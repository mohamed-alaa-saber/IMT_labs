def inp(u):
    stat=str(u)
    return stat.split()



def main():
    print("hallo")
    x=input()
    act=list()
    doing=list()
    done=list()
    while (x != "end"):
        
        if x!="end":
            act=inp(x)
            print(act)
            if act[0]=="add":
                doing.append(act[1:])
            elif act[0]=="finish":
                doing.remove(act[1:])
                done.append(act[1:])
            elif act[0]=="doing":
                print(doing)
            elif act[0]=="done":
                print(done)
            else:
                print("error")
            x=input()
        else:
            continue
        
    
    
    
    
    
    
if __name__=="__main__":
    main()