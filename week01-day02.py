#ali-tork 
#week-01 
#2nd-day
#first-task 

#daryaft se addad va majmoe anha 

num1=int(input("enter first number : ")) 
num2= int(input("enter second number : "))
num3=int(input('enter third number : '))

#majmoo 
s=num1+num2+num3

print(f"summanation of numbers = {s}")


#ali-tork
#week-01
#2nd-day
#2nd-task 

#miangin vazni 

#daryaft addad
num1=int(input("enter your first number  : "))
num2=int(input("enter your second number  : "))
num3=int(input("enter your third number  : "))

#daryaft vazn ha 
weight1=int(input("enter your first weight  : "))
weight2=int(input("enter your second weight  : "))
weight3=int(input("enter your third weight  : "))

#mohasebe mingin vazni 

avg=((num1*weight1)+(num2*weight2)+(num3*weight3))/(weight1+weight2+weight3)

#chap miangin vazni ba f-string
print(f"hasel miangin vazni = {avg}")


#ali-tork 
#week-01
#2nd-day
#third-task 
#rooz be saat o daqiqe o sanie


#daryaft tedad rooz 
days=int(input("how many days u wanna enter : "))

#tabdil ha
#ravesh aval 
hours=days*24 #har rooz 24 saat
minutes=hours*60  #har saat = 60 daqiqe 
seconds=minutes*60 #har daqiqe = 60 sannie 

#ravesh dovom
#hours=days*24
#minutes=days*1440
#seconds=days*86400

#chap kardan be tor khyli kotah 
print(f" days = {days}\nminutes = {minutes}\nseconds = {seconds}")



#ali-tork 
#week-01
#2nd-day
#4th-task

#daryaft qeymat va takhfif 

price=float(input("enter the price : "))

takhfif=int(input("chand darsad takhfif darid ? ")) #takhfif be engilisi yadam raft :) 

#mohasebe kol qeymat pardakhti
total_price=price-(price*takhfif/100)

print(f"total price you have to pay = {total_price}")


#ali-tork 
#week-01
#2nd-day
#5th-task 

#mohasebe masahat o mohit ba deqat se raqam aashar 

#daryaft shoaa 
radius=float(input("enter the radius"))

#mohasebe masahat va mohit ( a va p )
area=radius**2*3.14159
p=2*3.14159*radius

#chap masahat va mohit ta se raqam aashar
#barraye se raqam ham ravesh format hast ham ravesh {af:.3f} 
print(f" area = {area:.3f}")
print(f"mohit = {p:.3f}") #esmm engilisie mohit yadam raft 


#ali-tork 
#week-01
#2nd-day
#6th-task

#MOHASEBE m be cm mm km 

#daryaft meter
m=float(input("enter meter : ")) 

#mohasebat
cm=m*100
mm=m*1000
km=m/1000

#chap maqadir
print(f"in cm ={cm}\nin mm = {mm}\nin km = {km}")




#ali-tork 
#week-01
#2nd-day
#7th-task 

#mohasebe masahat va hajm mokeab 

#daryaft tool 
length=float(input("enter the length of the cube : "))

#mohasebat 
#ravesh aval 
area=6*(length**2)
volume=length**3 

#chap maqadir 
print(f"area = {area} m^2\nvolume = {volume} m^3 ")

#ravesh dovom
#area=6*length*length
#volume=length*length*length




#ali-tork
#week-01
#2nd-day
#8th-task 

#mohasebe masahat ba formul heron 

#daryaft azlaa
zeel1=float(input("enter your first zeel : ")) #zeel be engilisi yadam nist bekhoda
zeel2=float(input("enter your second zeel : "))
zeel3=float(input("enter your third zeel : "))

#mohasebat
#baraye tavan ** ke midonim  baray radical ke tavan 0.5 hastesh be soorat zir minvisim 
p=(zeel1+zeel2+zeel3)/2
area=(p*(p-zeel1)*(p-zeel2)*(p-zeel3))**0.5

#chap 
print(f"area = {area}")


#ali-tork
#week-01 
#2nd-day
#9th-task 
#mohasebe avg . vorodi dar yek khat !
#baraye in kar bayad az input.split ( ) estefade kard

#daryaft 3 addad 
numbers = input("please enter 3 numbers : ")

#tabdil be se addad (split)
#ravesh aval
num=numbers.split() 
num1=float(num[0])
num2=float(num[1])
num3=float(num[2])

#mohasebe
avg=(num1+num2+num3)/3

print (f"average = {avg}") 

#ravesh dovom ( be tor mostaqim )
#num1=numbers.split()[0]
#num2=numbers.split()[1]
#num3=numbers.split()[2]


#ali-tork
#week-01 
#2nd-day
#10th-task 

#mohasebe sood morakab 


#daryaft vorodi ha
price=float(input("enter the price : ")) 
nerkh_sood_salane=float(input("enter the nerkh_sood_salane"))
years=int(input("how many years ?" ))
tedad_dafaat=int(input("how mant times ? "))


#formula
mablaq_nahayi=price*(1+nerkh_sood_salane/(tedad_dafaat*100))**(tedad_dafaat*years)

print(f"mablaq nahayi ={mablaq_nahayi}")