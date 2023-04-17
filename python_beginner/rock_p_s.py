import random

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

rps = [rock, paper, scissors]

choice = int(input("Which one would you like to choose:\n" +
                   "Type 0 for rock, 1 for paper or 2 for scissors\n"))
if choice>=3 or choice <0:
    print("invalid number you looooose!")
else:
    choice_pc = random.randint(0, 2)

    if choice == choice_pc:
        print("DRAW")

    elif choice == 1 and choice_pc == 2 or choice == 2 and choice_pc == 1 or choice == 1 and choice_pc == 0:
        print(f"you won: your choice was : {rps[choice]}")
        print(f"pc's choice was : {rps[choice_pc]}")
    else:
        print(f"you lost : your choice was : {rps[choice]}")
        print(f"pc's choice was : {rps[choice_pc]}")
