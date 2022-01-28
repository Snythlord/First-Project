import itertools
import threading
import time
import sys
import random
from time import sleep

ans = input("Hello! Let's play rock paper scissors! Yes or No? ")

if ans == "No":
    print("Oh, ok. Goodbye!")
    sleep(3)
    quit()

if ans == "Yes" or "y" or "yes" "Y":


    done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.05)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True
possible_actions = [" rock", " paper", " scissors"]
computer_action = random.choice(possible_actions)
ans = input("Rock, Paper or Scissors? ")  
print(f"\nYou chose {ans}, computer chose{computer_action}.\n")
if ans == computer_action:
    print(f"Both players selected{ans}. It's a tie!")
elif ans == " rock" or " Rock":
    if computer_action == " scissors":
        print("Rock smashes scissors! You win!") 
    else:
        print("Paper covers rock! You lose.")
elif ans == " paper" or " Paper":
    if computer_action == " rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif ans == " scissors":
    if computer_action == " paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

