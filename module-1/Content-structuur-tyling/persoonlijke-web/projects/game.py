import random
import sys
import time

# function :
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

#Collection:
directions = ["left", "right", "forward", "backward"]

#variable:
score = 0
direction = "" 

#start of the game (intro) :
play = True

while play:
    name= input ("What's your name, adventurer?   ")
    slowprint("""
    \nYou woke up and found yourself in a dark forest.
If you want to survive ...
You have to solve the puzzles.

And every time you find the solution to a puzzle, your power will rise. 
Which is what you will need in the end to kill the beast and survive and get out of the forest
    """)
    ready= input (f'\nAre you ready {name}? (yes,no)  ')

    if ready.lower() == 'yes':
        slowprint('\nYou head into the forest. You hear crows cawwing in the distance.')
    else:
        slowprint(f'\nYou are not ready for this quest, see you next time {name}! ')
        exit()
    
    while direction not in directions:
        slowprint(""" 
To your left, you see a bear.
To your right, there is way into the forest.
There is a rock wall directly in front of you.
Behind you is a deep hole.
        """)
        
        direction = input("\nWhat direction do you move? \nleft / right / forward / backward \n")
        if direction.lower() == "left":
            slowprint(f"The bear eats you. Farewell, {name}")
            exit()
        elif direction.lower() == "right":
            slowprint("You head deeper into the forest.\n")
            score +=1
        elif direction.lower() == "forward":
            slowprint("You cannot scale the wall.\n")
            direction = "" 
        elif direction.lower() == "backward":
            slowprint(f'you fall into deep hole {name}, Cheerio!')
            exit()
        else:
            slowprint("I didn't understand that.\n")
    slowprint("=================================END OF CHAPTER 1=================================")

    slowprint('\n---- Chapter 2 ----')
    slowprint(f"""" Your power is still {score}.
Remember ...
You need to rise your power to kill the beast and survive. 
So you have to make sure to solve all the puzzles and get out the forest.
    """)
    slowprint('\nThere is a lockt box under the tree in front of you and there is a hint inside.. \nThe hint will help you to kill the beast. \nYou can just open it by finding the 5 numbers of the lock by solving the following code')

    choice= input (f'Are you ready to find the 5 numbers {name} ?\nType (yes) or (no):  ')
    if choice == 'no':
        slowprint(f'thats too bad {name}, see you next time! \nEND OF THE GAME')
        exit()
    elif choice == 'yes':
        slowprint(f'\nAWESOME {name}!')
    
    for num in range (1,6):
        number1 = random.randint (0,4)
        number2 = random.randint (0,4)
        answer  = number1 + number2
        lock_code = int(input((f"""Number {num} of the lock is: 
wat is {number1} + {number2} ? 
""")))
        if lock_code == answer:
            score +=1
    
    if score >= 5:
        slowprint(f""""Good job {name}! the box is open now.
The hint in the box is a message. the message is :

Hello {name} , 
We want to tell you an important secret about the beast. 
You can only kill the beast if your power is higher than his power.
Good luck.
        """)
    else:
        slowprint(f"You didn't find the four numbers of the lock, that means you lose the hint.")
    slowprint("=================================END OF CHAPTER 2=================================")

    slowprint('\n---- Chapter 3 ----')
    choice = input (f"""Hold on...
look forward,
There are zombie watching you.
.
..
..
He is coming to you..
Choose Quickly...
Do you want to fight him or to run?
""")

    if choice == 'fight':
        slowprint(f'Good choice {name}!')
        score += 1
    else:
        slowprint(f'YOU RUN .. You fell on a rock.. The zombie bites you and you die \nGAME OVER')
        exit()
    slowprint("=================================END OF CHAPTER 3=================================")

    slowprint('\n---- Chapter 4 ----') 
    choice = input (f"""
You're in a fight with the zombie .. what do you want to do?
A. Bite him?           success 30%
B. Push him?           success 45%
c. Throw stone at him? success 60%

What is your choice? A , B or C ?
""")
    if choice.lower() == 'c':
        slowprint(f"Good thinking {name} ...")
        score +=1
    else:
        slowprint(f'That was not the best choice {name} .. He was stronger than you and killed you! \nGAME OVER ')
        exit()
  
    choice= input(("""WAIT ... He is still alive ... 
Do you want to try to kill him with a tree trunk? 
success = 85%..
Take quickly a choice : 'yes' or 'no' ?   """))
    if choice == 'yes':
        slowprint(f"\nYou were born to be the savior of the world, good chocie {name}")
        score += 2
    else:
        ('\nThe zombie is running to you... \nHe was faster than you and killed you! \nGAME OVER ')
        exit()
    slowprint('You found a tree trunk and killed the zombie with it! ')
    slowprint("=================================END OF CHAPTER 4=================================")

    slowprint ('\n---- Chapter 5 ----')
    slowprint (f'You are doing great job {name}. Dont give up! \nYou are so close to the end!')
    choice = input ("""The place has become very dark.
Moonlight illuminating a small part of the forest...
..
...
Do you want to take a break and sleep? Or do you want to complete your way and fight the beast? 
What is your choice? (sleep) or (fight)  ?""")

    if choice.lower() == 'sleep':
        slowprint (f'Good chocie')
        score +=5
        slowprint("""You went under a big tree and fell asleep.
..
...
< The next morning >
the sun is shining..
you woke up and got ready to fight the beast..
""")
        slowprint("=================================END OF CHAPTER 5=================================")
    else:
        slowprint (f'You decide to stay awake and fight the beast!')

    slowprint ('\n---- Chapter 6 ----') 
    slowprint(""" It's the moment ..
You've done a great job so far..
But now ..
Is the time for confrontation ..
The monster is coming to you...
Your power level will be shown in seconds..
""")
    for loading in range (0,100,10):
        slowprint(f'loading {loading}%.')
    beast_power  = random.randint (10,15)
    slowprint(f'Your power level is {score} , and the beast power is {beast_power}')

    if score > beast_power:
        slowprint (f"""" The fight started!
The beast hit you hard.
<You lost some of your power.>
you got up and attacked him.
<He lost some of his power.>
He threw a big stone at you and you hit into the tree behind you.
<You lost some of your power.>
You used all your power and carried the tree and threw it at him.
<He lost all his strength.>
he is dying...
He is died! """)

        print (f""""YOU ARE A REAL HERO {name} ! 
YOU MADE IT AND KILLED THE BEAST! 
YOU SAVED THE WORLD ')
        print ('YOU WIN THE GAME""")
        print ("                          _,.-'') ,....")
        print ("                      .-'      /'     ")
        print ("                    /        /       /")
        print ("                  _:.   `. ,:.   _.-'")
        print ("                  /   `...'`  /.-'''.")
        print ("     ,       __../       \::,'     /    _.-.")
        print ("    /.\   .-'.--'\     ,' `'\     ,.  .'   _")
        print ("   | | |,'.'`     ;---'      ..--'  `/ ,-'' ''")
        print ("   \ | /,'      .'    \    ,'         `.   _.._")
        print ("   '|'/.-''-. ,'      `'''  _---_     ',-'")
        print ("     /// _.' / |                .        / ")
        print ("    /./.'  .'  |               _/ ,'      |")
        print ("   '/-'--'`    |           _.:.''`        |")
        print ("  .'           |         .'''\-'''`      .'")
        print ("  |'           \        /.//'/            /")
        print ("  ||          ,--    ._: ||_/           _/.-`")
        print ("  ||         |         |  '/     ._``:.`_..-'")
        print ("  ||         `.        `-''     //.:/.:-..-'" )
        print ("  ||          \       . /.''\  |||///'")
        print ("  ||        ,-'``\    \/|`'. : :_`/`")
        print ("  |'      ,'          | |/  \|  '/")
        print ("  '|     /  ,-'    _,-,\_\   '   ;")
        print ("   \\,_.' ,'   _,``  _/`-..__..-'")
        print ("    \[_`;.--''   _..'")
        print ("    / ='....----''\  _      YOU ARE")
        print ("    `-|'         '|/' |    MY Hero")
        print ("     || \         /_./")
        print (f"    |'  -----------          {name}!!!")
        print ("------------------------------------------------")
        print ('.\n.\n.\n.')
        again = input ("Do you want to play again? \ntype yes or no:  ")
        if again.lower() == 'no':
            print('See you next time superhero!')
            play = False
    else:
        slowprint (f"""" The fight started!
You hit the beast hard.
<He lost some of his power.>
He got up and attacked him.
<You lost some of your power.>
you threw a big stone at him and he hit into the tree behind him.
<He lost some of his power.>
He used all his power and carried the tree and threw it at you.
<you lost all his strength.>
you are dying...
you are died! 
GAME OVER ...""")
        exit()
        

