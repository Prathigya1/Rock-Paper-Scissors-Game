rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
image_game =[rock,paper,scissors]
user_choice = int(input("what do you choose? type '0' for rock,'1' for paper ,'2' for scissors "))
if user_choice>=0 and user_choice<=2:
    print(image_game[user_choice])
computer_choice=random.randint(0,2)
print(image_game[computer_choice])
print(f"computer chose{ computer_choice}")
if user_choice==0 and computer_choice==2:
    print("you win!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice < computer_choice:
    print("you loose!")
else:
    print("it's a tie!")