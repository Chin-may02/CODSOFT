import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return (1, user, computer)
    else:
        return (-1, user, computer)

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_needed = (n // 2) + 1

    while player_wins < wins_needed and computer_wins < wins_needed:
        result, user, computer = play()
        if result == 0:
            print(f'Tie! Both chose {user}.')
        elif result == 1:
            player_wins += 1
            print(f'You won! you chose {user} which beats computers choice {computer}.')
        else:
            computer_wins += 1
            print(f'You lost! computer chose {computer} which beats your choice {user}.')

    if player_wins > computer_wins:
        print(f'You won the best of {n} games!')
    else:
        print(f'The computer won the best of {n} games.')

if __name__ == '__main__':
    while True:
        rounds = int(input("Enter number of rounds: "))
        if rounds % 2 == 1:
            play_best_of(rounds)
        else:
            print("Please enter an odd number")

        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing! Goodbye")
            break
