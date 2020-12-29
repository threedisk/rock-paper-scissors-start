import random
jolly = '''
888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888P""  ""9888888888888888888888888888
8888888888888888P"88888P          988888"9888888888888888888
8888888888888888  "9888            888P"  888888888888888888
888888888888888888bo "9  d8o  o8b  P" od88888888888888888888
888888888888888888888bob 98"  "8P dod88888888888888888888888
888888888888888888888888    db    88888888888888888888888888
88888888888888888888888888      8888888888888888888888888888
88888888888888888888888P"9bo  odP"98888888888888888888888888
88888888888888888888P" od88888888bo "98888888888888888888888
888888888888888888   d88888888888888b   88888888888888888888
8888888888888888888oo8888888888888888oo888888888888888888888
8888888888888888888888888888888888888888888888888Ojo 9888888
'''
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

print ('''
Welcome to Jankenpon Game\n 
Rock (0), Paper(1), Scissors(2)
''')

game_image = [rock,paper,scissors] #ANGELA CHOICE VIA GAME IMAGE INDEX
choice = int(input("What is your choice ? Rock(0), Paper(1) or Scissors(2)\n"))
if choice >= 3 or choice < 0:
  print (jolly)
  print ("You type invalid number, you lose")
else:
  print (game_image[choice]) #ANGELA CHOICE VIA GAME IMAGE INDEX

  computer_choice =random.randint(0,2)
  print ("Computer Choose: ") #ANGELA CHOICE VIA GAME IMAGE INDEX
  print (game_image[computer_choice]) #ANGELA CHOICE VIA GAME IMAGE INDEX

  # if computer_choice == 0:
  #   print (f"Computer choose: Rock\n{rock}")
  # elif computer_choice == 1:
  #   print (f"Computer choose: Paper\n{paper}")
  # else:
  #   print (f"Computer choose: Scissors\n{scissors}")

  # if choice == 0:
  #   print (f"You choose: Rock\n{rock}")
  # elif choice == 1:
  #   print (f"You choose: Paper\n{paper}")
  # else:
  #   print (f"You choose: Scissors\n{scissors}")

  if choice >= 3 or choice < 0:
    print ("You type invalid number")
  elif choice == computer_choice:
    print ("DRAW")
  elif choice == 0 and computer_choice == 2 :
    print ("You Win")
  elif computer_choice == 0 and choice == 2 :
    print ("Computer Win")
  elif computer_choice > choice:
    print ("Computer Win")
  elif choice > computer_choice:
    print ("You Win")
  else:
    print ("Wrong number")