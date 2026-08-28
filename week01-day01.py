#ali-tork
#first-week
#1st-day
# #first task 
#hello world ! ro chap kon :) 

print("hello , world !") 
print('hello python !')
#ham ba '' ham ba "" mishe nevesht 
#ravesh dovom 
print("hello world\nhello python")



#ali tork 
#first-week
#1st-day
#third-task
#ashnayi ba input 

#ravesh aval 
#dar input hamegi be soorat str (sring o character save mishan )

name=input('whats your name ? ')
print(name)

#ravesh dovom (second method )

print(input("whats your name "))


#ali tork 
#first-week
#1st-day
#foyrth-task
#ashnayi ba int o float va class

number=int(input("enter your number : "))
#alan harchi che addad che harf vared konim be soorat str


#ravesh aval 
#dar print nemishe ham st ham int ya float bashe 
#dar natije number be soorat int vared mishe va dar print qablesh str mizarim ta be soorat str vared she 
print("your number = " + str(number) )
print(type(number))


#ravesh dovom 

number1=str(number)
#alan number1 mishe str number ke  number khodesh int 
print("your number = " + number1 )

print(type(int(number1)))




#ali-tork
#first-week
#1st-day 
#5th-task 
#dayaft name
name=input("whats your name ? ")

print("hello , "  + name + "!" )



#ali-tork 
#first-week
#1st-day
#6th-task 
#daryaft name va estefade as f-string 

name=input("whats your name ? ")

#ravesh aval 
print(f"i am  {name} and i am studying python ")

#ravesh dovom 
print(f"i am  {input("whats your name ? ")} and i am studying python ")

#f-string be jay inke as + baray be ham chasbandan estefade beshe 
#va baraye inke mostaqim int float str vared print konim :) 





#ali-tork 
#first-week
#1st-day
#7th-task
#radius hamoon shoa khodemoone 
shoaa=float(input("enter your radius : ")) 

#a(area) hamoon masahat

#sakhtan formul masahat
a=shoaa**2*3.14 

# chap masahat - estefade az f-string baraye rahat tar neveshtan
print(f"masahat = {a}")