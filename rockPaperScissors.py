import random

print("Rock/Paper/Scissor")
user_choice=int(input("Enter the your choice 0 for rock/1 for paper/ 2 for scissor : "))

computer_choise= random.randint(0,2)
print("Computer choice :",computer_choise)

if computer_choise == user_choice:
    print("Match draw🤣🤣🤣")

elif computer_choise ==0 and user_choice ==2:
    print("You lose🤣🤣🤣")

elif user_choice ==0 and computer_choise ==2:
    print("You Win😍😍😍😍")

elif computer_choise > user_choice:
    print("You lose🤷🤷🤷🤷")

elif computer_choise < user_choice:
    print("You win😍😍😍😍")


