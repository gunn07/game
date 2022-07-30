import time
import random

b = ["", "Swordman", "Archer", "Axman" , "Wizard", "Spearman", "Sniper"]
Game_on = True
Enemy_Kind = "hi"
level = 1
Enemy_Final = ""
a = 1
attack = ""
Character = ""

def Restart():
  global b
  global Game_on
  global Enemy_Kind
  global level
  global Enemy_Final
  global a
  global attack
  
  b = ["", "Swordman", "Archer", "Axman" , "Wizard", "Spearman", "Sniper"]
  Game_on = True
  Enemy_Kind = "hi"
  level = 1
  Enemy_Final = ""
  a = 1
  attack = ""
  


def fight():
  global Attack_choice
  global level
  global Result
  global a
  print("{} has found!\n".format(Enemy_Final))
  time.sleep(1)
  Attack_choice = input("Chose your skill \n{}".format(attack))
  if Attack_choice == "1" and a%2 == 0:
    Result = True
    level += 1
    print("You won!")
  elif Attack_choice == "2" and a%2 == 1:
    Result = True
    level += 1
    print("You won!")
  elif Attack_choice == "2" and a%2 == 0:
    Result  = False
  elif Attack_choice == "1" and a%2 == 1:
    Result = False
  else:
    print("Type the proper option")
    fight()

def Enemy_name():
  global a
  global level
  global Enemy_Final
  global Enemy_Kind

  
  a = random.randrange(1,7)
  
  if a%2 == 0: #원거리
    Enemy_skill = b[a]
  elif a%2 == 1:
    Enemy_skill = b[a]

  if level ==1:
      Front_name = "low"
  elif level ==2:
      Front_name = "intermediate"
  elif level ==3:
      Front_name = "high"

  Enemy_Final = "{} rank {} ({})".format(Front_name, Enemy_Kind, Enemy_skill)


def result():
  global Result
  global Game_on
  if Result == False:
    print("You lose")
    End()

      

def End():
  Quest = input("Would you play again? \n y or n")
  Quest = Quest.lower()
  if Quest == "y":
    Game()
  if Quest == "n":
    print("Bye!")
    quit()



def Character_Choice():
  global Enemy_Kind
  global attack
  global Character
  print("Chose Your side")
  Character = input("Angel or Demon  ")
  Character = Character.lower()
  if Character == "angel":
    Enemy_Kind = "Demon"
    attack = "Light Slash (1)  Shining Star (2)"
  elif Character == "demon":
    Enemy_Kind = "angel"
    attack = "Dark Shadow (1)  Death Beam (2)"
  if Character == "angel":
    time.sleep(0.5)
    print("Good choice!\n")
    print("Tip:\nYour first skill is effective to close-attack enemy\nYour second skill is effective to far-attack enemy\n")
  elif Character == "demon":
    time.sleep(0.5)
    print("Good choice!\n")
    print("Tip:\nYour first skill is effective to close-attack enemy\nYour second skill is effective to far-attack enemy\n")
  else:
    print("Type the proper option")
    Character_Choice()










def Game():
  while Game_on == True:
    Restart()
    
    print("""Welcom to the Fantasia!
      
There is a war between angel and Demon
      
You have to chose one side and help them\n""")
    time.sleep(2)
    Character_Choice()
    for i in range(1,4):
      vvv()
    good()

    
def vvv():
    Enemy_name()
    time.sleep(1)
    fight()
    time.sleep(1)
    result()

def good():
  print("You leaded the war to {}'s victory!\nWell done!".format(Character))
  End()
    



Game()