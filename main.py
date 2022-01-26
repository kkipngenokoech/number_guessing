import random
from IPython.display import clear_output
attempts_list=[]
def show_score():
    if len(attempts_list)<=0:
        print("there is no current high score,it is yours for the taking!^")
    else:
        print(f"the current high score is {min(attempts_list)} attempts")
def start_game():
    random_number=int(random.randint(1,10))
    print("hello traveller!welcome to the game of guesses")
    player_name=input("enter your name:")
    #clear_output()
    wanna_play=input(f"hi {player_name},would you like to play the guessing game?(yes/no)").title()
    clear_output()
    attempts=0
    show_score()
    while wanna_play.lower()=="yes":
        try:
            guess=input("pick a number between 1 and 10:")
            clear_output()
            if int(guess)<1 or int(guess)>10:
                raise  ValueError("please guess a number between the given range")
            if int(guess)==random_number:
                print("Bingo!you got it")
                attempts+=1
                attempts_list.append(attempts)
                print(f"it took your {attempts}")
                play_again=input("would you like to play again?(enter yes or no)")
                attempts=0
                show_score()
                random_number=random.randint(1,10)
                if play_again.lower()=="no":
                    print("thats cool,have a good one")
                    break
            elif int(guess)>random_number:
                print(f"it is lower than {guess}")
                attempts+=1
            elif int(guess)<random_number:
                print(f"it is higher than {guess}")
                attempts+=1
        except ValueError as err:
            print("oh no!thats not a valid  value,try again...")
            print(f"{err}")
    else:
        print("thats cool ,have a good one")
if __name__=='__main__':
    start_game()

