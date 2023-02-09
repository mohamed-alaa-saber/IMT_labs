#lab-3
#x=int(input("Enter your birth year: "))
#y=2023-x
#print("You are ",y," years old")
#'''write formated string'''  '''Doc string'''
#print(f"You are {y} years old")

#lab-4
#loan=int(input("Please enter the loan value:"))
#YearNum=int(input("Please enter the number of years:"))
#rate=YearNum*0.12
#newLoan=loan*(1+rate)
#month=newLoan/(YearNum*12)
#print(f"Your monthly installment is {month}")


#lab-5
#res=int(input("enter timer resolution"))
#hz=int(input("enter frequancy"))
#pr=int(input("enter prescaller value"))
#ticktime=pr/hz*(10**-6)
#overFLow=(ticktime*(2**res))*1000
#print(overFLow)



#lab-6
#names=['ahmed','ali','amr']
#password=[1394,6078,9345]
#n=str(input("name"))
#if n in names:   
#    p=int(input("pass"))
#    if p ==password[names.index(n)]:
#        print(f"welcom {n}")
#    else:
#        print("wrong password")
#else:
#    print("wrong username")

#other solution
#data={'ahmed':1394,'ali':6078,'amr':9345}
#n=str(input("name"))
#if n in data:
#    p=int(input("pass"))
#    if p==data[n]:
#        print(f"welcom {n}")


#lab=7
#string concatenation
#'mohamed'+'alaa'='mohamedalaa'
#n=str(input("enter name"))
#rev=""
#for ch in n:
#    rev=ch+rev
#print(rev)


#lab-8
#max=int(input("enter max"))
#i=1
#while (i<max):
#    print("*"*(i))
#    i=i+1
#i=max-2
#while (i > 0):
#    print("*"*(i))
#    i=i-1

 