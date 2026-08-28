#week02_day03
#alitork 


#takin inputs (daryaft vorodi ha)
num1=float(input("please enter the first number :"))
num2=float(input("please enter the second number :"))
operator=input("please enter the oprator (+, -,* ,/, // ,% ,** )") 
num3=0
#gozashtan shoorot va amaliat 
if num2==0 : 
    print("second number cant be 0 ")
else :
 
    if operator=='+' :
        num3=num1+num2 
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
        print(f"operator {operator} is usefull for summanation")
    elif operator=='-' :
        num3=num1-num2 
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
        print(f"operator {operator} is usefull for decrement")
    elif operator=='/' :
        num3=num1/num2 
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3:.3f}") 
        print(f"operator {operator} is usefull for dividing")
    elif operator=='//':
        num3=num1//num2
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
        print(f"operator {operator} is usefull for divifing (sahih) numbers")
    elif operator=='%' :    
        num3=num1%num2 
        print(f"operator {operator} is usefull for ramaining")
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
    elif operator=='**' :
        num3=num1**num2 
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
        print(f"operator {operator} is usefull for calculating the power")
    elif operator=='*' :
        num3=num1*num2
        print(f"awsner with {num1} and {num2 } with opertaor {operator} = {num3}") 
        print(f"operator {operator} is usefull for multipliction")
    else : 
        print("wrong operator . please try again ")    


#mitonestam toolani tar konam ke baad mohasebe baad inke chap kar . ye dor dobare if/elif/else 
#baraye operator ha bezanam 


