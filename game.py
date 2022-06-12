import random
from urllib.parse import uses_netloc

# is_playing =True

# while is_playing:
#     print("game is already initialized")
#     #game list in an array like square bracket
# gameList=["Rock","Scissors","Paper"]


gameList = ["Rock","Scissors","Paper"]
userChoice=str(input("enter a value from the list:  "))
computerChoice = random.choice(gameList)
if userChoice  in gameList :
    print("Working")
else:
    print("invalid valid please input a real value")

print(computerChoice)


print(random.choice(gameList))
print("my choice for the game is :" +userChoice)
print("Computer choince is  :"+ computerChoice)

if userChoice =="Rock" and computerChoice =="Scissors":
    print("rock beats scissor so i win")
elif userChoice =="Paper" and computerChoice =="Rock":
    print("Paper beats rock so i win")
elif userChoice == "Scissors" and computerChoice =="Paper":
    print("Scissors beats  paper so i win")
elif  computerChoice =="Rock" and userChoice =="Scissors":
    print("rock beats scissor so computer wins")
elif computerChoice =="Paper" and userChoice =="Rock":
    print("Paper beats rock so computer wins")
elif computerChoice =="Scissors" and userChoice =="Paper":
    print("Scissors beats paper so computer win")
# s    # print("lets start all over again!!!")

    



