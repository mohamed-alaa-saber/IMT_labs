def add(num1,num2):
    return num1+num2

def main():
    mystr="MohamedAlaa"
    length=len(mystr)
    m=str("")
    n=str("")
    i=0
    for i in range(length):
        n1=mystr[i:i+1]
        print(n1)
        if n1.islower():
            print("0")
            n1=n1.upper()
            
        else:
            print("1")
            n1=n1.lower()
            
        m=m+n1
    print(m)
    
    
    
if __name__=="__main__":
    main()