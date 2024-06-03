male=input("Enter your name : ")
female=input("Enter your partner name : ")
compain_string=male + female
lowerCase= compain_string .lower()

t=lowerCase.count("t")
r=lowerCase.count("r")
u=lowerCase.count("u")
e=lowerCase.count("e")
true=t + r + u + e

l=lowerCase.count("l")
o=lowerCase.count("o")
v=lowerCase.count("v")
e=lowerCase.count("e")
love=l + o + v + e

love_scope= int(str(true) +str(love))

if love_scope <10 or love_scope >90:
    print( f"Together forever and your score is {love_scope}")
elif love_scope >=40 or love_scope <=75:
    print(f"you are no soo good and your love score is {love_scope}")
else:
    print("just waste of time")
