#week02-day02
#task2_tax_calculator.py

#takin inputs / daryaft vorodi ha 
name=input("enter your name :")
salary=int(input("enter your salary : "))
marriage=input("are you single or married ?(enter S or M) ").lower()
#.lower() bekhater in neveshtam ke age S ya M ya s ya m vared kard to sharti ke qarare benvisam kar kone 

#mohasebe maliat 

maliat=salary
if salary>=50000000 and salary<100000000 :
    maliat=salary*10/100 
elif salary>=100000000 and salary<200000000 :
    maliat=salary*20/100
elif salary>200000000 :
    maliat=salary*30/100
    #else => salary<50000000  : chon maliat nist niaz be neveshtan nist !
    
 #mohasebe takhfif   
takhfif=0
if marriage=='s' or marriage=='m' : 
    if marriage=='m' :
        takhfif+=maliat*10/100
else : 
    print("wrong input !")

#mahosebe mablaq nahayi 
final_price=maliat-takhfif 

#chap info 
print("\n")
print(f"gozaresh mohasebati\n {name}") 

print(f" salary in a month = {salary:,}")
print(f"maliat mohasebe shod = {maliat:,}")
print(f"takhfif = {takhfif:,}")
print(f"mablaq qabel pardakht = {final_price:,}")

print("\n tashakor az pardakht be moqe shoma")

#f"{harchi:,} => be soorat hezargan joda mikonad ! 
