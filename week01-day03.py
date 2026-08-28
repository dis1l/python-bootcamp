#ali-tork 
#week-01 
#day-03 
#first-task 

num1=float(input("enter first number : "))
num2=float(input("enter second number : "))
num3=float(input("enter third number : "))
num4=float(input("enter fourth number : "))

avg=(num1+num2+num3+num4)/4

print(f"average = {avg}")


#ali-tork 
#week-01 
#day-03 
#2nd-task 
#tabdil saat be daqiqe va sanie 

hours=int(input("how many hours you wanna eneter ? "))

minutes=hours*60 
seconds=minutes*60

print(f"in {hours} is {minutes} minutes and {seconds} seconds")



#ali-tork 
#week-01 
#day-03 
#3rd-task 
#masahat-zoozanaqe 

ghaede1=float(input("andaze qaede 1 ra vared kon : "))
ghaede2=float(input("andaze qaede 2 ra vared kon : "))
height=float(input("andaze ertefa ra vared kon : "))

area=(ghaede1+ghaede2)*height/2

print(f"masahat = {area}") 


#ali-tork 
#week-01 
#day-03 
#4th-task 
#hajm-ostovane 

radius=float(input("enter the radius : "))
height=float(input("enter the height  : "))

volume=3.14159*radius**2*height

print(f"voulume of ostovane = {volume}")


#ali-tork 
#week-01 
#day-03 
#5th-task 
#miangin addad dar ye khat 

num=input("enter your numbers (in a line please  ) : ")

num1=float(num.split()[0])
num2=float(num.split()[1])
num3=float(num.split()[2])

s=num1+num2+num3
avg=s/3

print(f"majmo={s}\naverage={avg}")


#ali-tork 
#week-01 
#day-03 
#6th-task 
#qeymat nahayi 

price=float(input("enter the price : "))
takhfif=int(input("enter the takhfif : "))
maliat=int(input("enter the maliat : "))

final_price=price-(price*takhfif/100)+(price*maliat/100)

print(f"final price = {final_price}")



#ali-tork 
#week-01 
#day-03 
#7th-task 
#tabdil vahed

meter=float(input("chand metr ? "))

cm=meter*100
mm=meter*1000
km=meter/1000

print(f"{meter} metr barabar :\n{cm} centimeter \n{mm} milimeter\n{km} kilometer")


#ali-tork 
#week-01 
#day-03 
#8th-task 
#hajm o masahat ba deqat 3 raqam ashar 

length=float(input("enter the length  : "))

area=6*length**2
volume=length**3

print(f"with length of {length} \narea={area:.3f}\nvolume={volume:.3f}")


#ali-tork 
#week-01 
#day-03 
#9th-task 
#avg-velocity 

length=float(input("enter the length (  in km please) : "))
total_time=float(input("enter the time ( in hour please ) : "))

velocity=length/total_time

print(f"with that length and time , average velocity = {velocity}km/h")

#ali-tork 
#week-01 
#day-03 
#10th-task 
#bmi  + (tabdil vahed ghad)

weight=float(input("enter your weight ( in kg please ) : "))
height=float(input("enter your height (in cm please ) : "))

height_in_meter = height/100 

bmi=weight/height_in_meter**2

print(f"your bmi = {bmi}")












