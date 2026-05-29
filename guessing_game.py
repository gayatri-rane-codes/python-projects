import random 

def play():
    
    secret=random.randint(1,100)
    attempts=0
    max_attempts=10

    print(f"I've selected a number from 1 to 100. You have {max_attempts} to guess it right! ")
    print("All the best!")
    while attempts<max_attempts:
        try:
            guess=int(input("Enter a number from 1 to 100: "))
        except ValueError:
            print("Enter a whole number ")
            continue

        attempts+=1

        if secret<guess:
            print("Too high!")
        elif secret>guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            return 
    
    print(f"Out of attempts! The number was {secret}")

def main():
    while True:
        play()
        again=input("Play again? yes/no : ").strip().lower()
        if again != "yes":
            print("See you next time!")
            break

main()