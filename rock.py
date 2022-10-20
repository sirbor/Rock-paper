import random

def rock_paper_scissors():
    print("Lets play Rock Paper Scissors\n")

    r = "rock"
    p = "paper"
    s = "scissors"
    all_choices = (r, p, s)

    user = input(f"Enter a choice ((r), (p), (s)); ")

    if user not in all_choices:
        print ("\Invalid choice!\n")
        return

    computer = random.choice(all_choices)
    print(f"You chose {user}, computer chose {computer}.")

    if user == computer:
        print("Tie!\n")
    elif (
        (user == r and computer == s)
        or (user == p and computer == r)
        or (user == s and computer == p)
    ):
        print ("You win!\n")
    else:
        print("You lose!\n")
