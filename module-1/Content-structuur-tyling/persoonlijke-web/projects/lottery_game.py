import random
import sys
import time

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

# Intro
slowprint('Welcome to the lucky lottery game.\n')
slowprint('How to play the game: \n')
slowprint ('1. Guess the secret number between 1 and 1000.\n')
slowprint ('2. You have the chance to guess the secret number 10 times.\n')
slowprint ("3. If you didn't guess the secret number, then you would move on to the next round.\n")
slowprint ('4. For each guessed number, the score is increased by 1.\n') #omhoog
slowprint ('5. After each round, you will be asked if you want to "guess another number?"\n')
slowprint ('6. the game is over after 20 numbers to guess.\n')
slowprint ('7. At the end, your final score will be reported.\n') #gemeldt
('____________________________________________')

score= 0
guess_limit = 10
guess_count = 0 
level_num = 1

while level_num < 20 :
   slowprint (f"ROND {level_num}") 
   random_nummer = random.randint(1,1000)
   while guess_count < guess_limit:
      guess= int (input('Guess the secret number between 1 and 1000:  '))
      guess_count += 1
      different= abs (random_nummer - guess) #absolute antwoord
      if different <= 50:
         slowprint ('YOU ARE HOT!! \n') 
      if different <= 20: 
         slowprint ('YOU ARE SO HOTT !! \n') 
      if guess > random_nummer: 
         slowprint("Your guess is too high! Please try again! \n")
      elif guess < random_nummer:
         slowprint('your guess is too low! Please try again! \n')
      if guess == random_nummer:
         break
   else:
      slowprint(f"You didn't guess the number, The number was {random_nummer}\n")
      guess_count = 0
      level_num += 1

   if guess == random_nummer:
      score +=1
      level_num += 1
      slowprint ('CORRECT!!') 
      slowprint (f'Your score is {score}')
      slowprint (f'You guessed the number in {guess_count} tries!') 
      guess_count = 0

   play_again = input("Play again? (y/n): \n")
   if play_again.lower() != "y":
      break

if level_num == 20 or play_again == 'n':
   slowprint ("You are at the end of the GAME!")
   slowprint (f"Your end score is {score} .")
   slowprint ("See you next time!!")
   slowprint('END OF THE GAME \n')