def main():
    data={}
    while True:
        print("|"+"*"*30+"|")
        print("1 for add \n 2 for print \n 3 for delete")
        print("|"+"*"*30+"|")
        inp=int(input("enter the number"))
        
        if inp==1:
            id=input("id: ")
            name=input("name: ")
            job=input("job: ")
            salary=input("salary: ")
            data[id]=[name,job,salary]
        elif inp==2:
            print_id=str(input("id:"))
            if print_id not in data:
                print("error")
            else:
                print("name is: ",data[print_id][0])
                print("job is:",data[print_id][1])
                print("salary is:",data[print_id][2])
            
        elif inp ==3:
            del_id=input("id:")
            if del_id not in data:
                print("error")
            else:
                data[del_id].pop()
        else:
            print("error")
    
    
    
    
    
if __name__=="__main__":
    main()