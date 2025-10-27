def rps(p1,p2):
    if p1 == p2:
        print("It's a draw!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!") 

print(rps("paper","scissors"))