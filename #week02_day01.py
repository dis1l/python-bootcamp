#week02_day01 
#alitork 

#task 1 
#odd or even ? (zoj ya fard)

num=int(input("enter your number : "))

if num%2==0 : 
    print(f"{num} is even")
else : 
    print(f"{num} is odd")
#else => num%2!=0 

#task 2 
#young or old (bozorgsal ya nojavan)

age=int(input("enter your age : "))

if age>=18 : 
    print("you are old ")
else : 
    print("you are young")
#else => age<18

#albate kamel tar ine 
age=int(input("enter your age : "))

if age<0 : 
    print("its not possible")
else :     
    if age>=18 : 
        print("you are old ")
    else : 
        print("you are young")


#task3 
# find the max (maximum ro peyda kon)        

#num1=float(input("enter the first number :"))
#num2=float(input("enter the second number :"))

#if(num1>num2) : 
    #print(f"{num1} is greater than {num2}")
#elif (num1==num2) : 
    print("they both equal")
#else : 
    #print(f"{num2} is greater than {num1}")        
    #else => num2>num1

#kamel taresh :)
num1=float(input("enter the first number :"))
num2=float(input("enter the second number :"))


if(num1<0) : 
    num1=num1*-1
if (num2<0) : 
    num2=num2*-1

if(num1>num2) : 
    print(f"{num1} is greater than {num2}")
elif (num1==num2) : 
    print("they both equal")
else : 
    print(f"{num2} is greater than {num1}")        
    #else => num2>num1



