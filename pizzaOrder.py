size=input("size of your pizza (S/M/L) : ")
bill =0

if size == "s" or size == "S":
    bill=100
    print(f"price of small pizza is {bill}")

elif size == "m" or size =="M":
    bill=200
    print(f"price of medium pizza is {bill}")
else:
    bill=300
    print(f"price of Large pizza is{bill}")

add_poperoni=input("you want pepperoni say (Y/n) : ")
if add_poperoni =="y" or  add_poperoni =="Y" :
    if size == "s" or size == "S":
        bill +=30
    else:
        bill +=50

cheess=input("do you want extra chess? say (Y/N) : ")
if cheess =="Y" or cheess =="y":
    bill +=50

print(f"Print your final bill is {bill}")