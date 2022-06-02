import random

player1_score = 0
player2_score = 0

for i in range(3):
    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)

    if player1_value > player2_value:
        print("player 1 wins.")
        player1_score = player1_score + 1
    elif player2_value > player1_value:
        print("player 2 wins")
        player2_score = player2_score + 1
    else:
        print("It's a draw")

    input("Press enter to continue.")

print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)