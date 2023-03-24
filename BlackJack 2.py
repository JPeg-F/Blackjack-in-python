import random
import csv

# sets the 3 rows name for the file csv
cardName = []
suitFace = []
cardValue = []
with open("War.csv", 'r') as csvfile:  # writes from war csv
    teamreader = csv.reader(csvfile, delimiter=',')
    for row in teamreader:
        cardName.append(row[0])  # appends all of them to the list
        suitFace.append(row[1])
        cardValue.append(int(row[2]))  # sets the third row as int to compare the cards
player_wins = 0
dealer_wins = 0
split_w = 0
while True:
    try:
        playerbalance = int(input("What do you want to set your balance to? "))
    except ValueError:
        print("Please enter a NUMBER")
        print()
    else:
        break
while playerbalance > 100000:
    print("You cannot go over $100000\n")
    while True:
        try:
            playerbalance = int(input("What do you want to set your balance to? "))
        except ValueError:
            print("Please enter a NUMBER")
            print()
        else:
            break
while playerbalance <= 0:
    print("You cannot bet or go under $0\n")
    while True:
        try:
            playerbalance = int(input("What do you want to set your balance to? "))
        except ValueError:
            print("Please enter a NUMBER")
            print()
        else:
            break
while True:
    if playerbalance <= 0:
        print("Your all out of cash")
        print("Game Stats: Your wins:", player_wins, "Dealer wins:", dealer_wins, "And splits:", split_w)
        reup = input("Do you want to re-up? y or n ").lower()  # ask the player to put more cash in if it runs out
        if reup == 'y':
            while True:
                try:
                    playerbalance = int(input("What do you want to set your balance to? "))
                except ValueError:
                    print("Please enter a NUMBER")
                    print()
                else:
                    break
            while playerbalance > 100000:
                print()
                print("You cannot go over $100000\n")
                while True:
                    try:
                        playerbalance = int(input("What do you want to set your balance to? "))
                    except ValueError:
                        print("Please enter a NUMBER")
                        print()
                    else:
                        break
            while playerbalance <= 0:
                print("You cannot bet or go under $0\n")
                while True:
                    try:
                        playerbalance = int(input("What do you want to set your balance to? "))
                    except ValueError:
                        print("Please enter a NUMBER")
                        print()
                    else:
                        break
        if reup == 'n':
            print("Danke und Auf Wiedersehen")
            break
    while True:
        try:
            print()
            playerbet = int(input("How much do you want to bet? "))
        except ValueError:
            print()
            print("Please enter a number")
        else:
            break
    while playerbet > playerbalance:
        print()
        print("Please bet something not above your balance\n ")
        playerbet = int(input("How much do you want to bet? "))
    ind = [i for i in range(52)]  # sets an empty index
    random.shuffle(ind)  # shuffles the index
    print()
    print('Let The Games Begin:')
    Hand1 = ["" for i in range(26)]  # makes empty hand for both players
    Hand2 = ["" for i in range(26)]
    print("Player      Dealer")  # the game starts by setting two hands for the player and dealer
    i = 0
    for i in range(26):
        Hand1[i] = ind.pop(0)  # pops the first card in the index
        Hand2[i] = ind.pop(0)
    print(cardName[Hand1[0]], suitFace[Hand1[0]], end="  ")  # hands the cards out
    print(cardName[Hand2[0]], suitFace[Hand2[0]])
    print(cardName[Hand1[1]], suitFace[Hand1[1]])
    sumE = cardValue[Hand1[0]] + cardValue[Hand1[1]]
    sumD4 = cardValue[Hand2[0]]
    print('You have a', sumE, "- Your dealer has", sumD4)
    if sumE > 21:
        print()
        print('You have gone bust with', sumE, "The dealer wins")
        lose = playerbalance - playerbet
        playerbalance = lose
        print("You have", lose)
        dealer_wins += 1
    elif sumE == 21:
        print()
        print('You have Blackjack. You win')
        win = playerbalance + playerbet
        playerbalance = win
        print("You have", win)
        player_wins += 1
    else:
        handsize2 = 3
        handsize = 2
        player = input('Do you want to Hit or Stand or Double Down. h - s - dd ').lower()

    if player == 'h':
        again = ' '
        while again != 'n' or again != 'N':
            print()
            print(cardValue[Hand1[handsize2 - 1]], suitFace[Hand1[handsize2 - 1]], end="  ")
            print()
            sumE = 0
            sumD4 = 0
            for i in range(handsize2):
                sumE = sumE + cardValue[Hand1[i]]
            for i in range(handsize):
                sumD4 = sumD4 + cardValue[Hand2[i]]
            if sumE > 21:
                print()
                print("You have gone bust with", sumE, "The Dealer wins")
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins = +1
                break
            elif sumE == 21:
                print()
                print("You have Blackjack")
                win = playerbalance + playerbet
                print("You have", win)
                print()
                playerbalance = win
                player_wins += 1
                break
            elif sumE < 21:
                print()
                print("Do you want to hit or stand. You have a", sumE)
                again = input("Enter y to hit or n to stand ")
                if again == 'n':
                    player = 'e'
                    break
                elif again == "y":
                    handsize += 1
                    handsize2 += 1
    if player == 'dd':
        again = ' '
        while again != 'n' or again != 'N':
            print()
            print(cardValue[Hand1[handsize2 - 1]], suitFace[Hand1[handsize2 - 1]], end="  ")
            print()
            sumE = 0
            sumD4 = 0
            for i in range(handsize2):
                sumE = sumE + cardValue[Hand1[i]]
            for i in range(handsize):
                sumD4 = sumD4 + cardValue[Hand2[i]]
            if sumE > 21:
                print()
                print("You have gone bust with", sumE, "The Dealer wins")
                playerbet = playerbet * 2
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins = +1
                break
            elif sumE == 21:
                print()
                print("You have Blackjack")
                playerbet = playerbet * 2
                win = playerbalance + playerbet
                print("You have", win)
                print()
                playerbalance = win
                player_wins += 1
                break
            elif sumE < 21:
                print()
                print("Do you want to hit or stand. You have a", sumE)
                again = input("Enter y to hit or n to stand ")
                if again == 'n':
                    player = 'e'
                    break
                elif again == "y":
                    handsize += 1
                    handsize2 += 1
    if player == 's':
        handsize = 2
        while True:
            print()
            print("\t ", cardValue[Hand2[handsize - 1]], suitFace[Hand2[handsize - 1]], end='  ')
            sumD4 = 0
            for i in range(handsize):
                sumD4 = sumD4 + cardValue[Hand2[i]]
            if sumD4 > 21:
                print()
                print('The Dealer has gone bust with', sumD4, "You win")
                win = playerbalance + playerbet
                print("You have", win)
                print()
                playerbalance = win
                player_wins += 1
                break
            elif sumD4 == 21:
                print()
                print('The Dealer has Blackjack you lose')
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins += 1
                break
            elif 17 <= sumD4 < 21 and sumD4 > sumE:
                print()
                print('The Dealer has a', sumD4, 'you lose')
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins += 1
                break
            elif 17 <= sumD4 < 21 and sumD4 < sumE:
                print()
                print('The Dealer has a', sumD4, 'you win')
                win = playerbalance + playerbet
                print("You have", win)
                playerbalance = win
                player_wins += 1
                print()
                break
            elif sumD4 == sumE and 21 > sumD4 >= 17:
                print()
                print('A split', sumD4, sumE)
                split = playerbet / 2
                playerbalance = playerbalance + split
                print("You have", playerbalance)
                split_w += 1
                print()
                break
            else:
                handsize += 1

    if player == 'e':
        handsize = 2
        while True:
            print()
            print("\t ", cardValue[Hand2[handsize - 1]], suitFace[Hand2[handsize - 1]], end='  ')
            sumD4 = 0
            sumE = 0
            for i in range(handsize):
                sumD4 = sumD4 + cardValue[Hand2[i]]
            for i in range(handsize2):
                sumE = sumE + cardValue[Hand1[i]]
            if sumD4 > 21:
                print()
                print('The Dealer has gone bust with', sumD4, "You win")
                win = playerbalance + playerbet
                print("You have", win)
                playerbalance = win
                player_wins += 1
                print()
                break
            elif sumD4 == 21:
                print()
                print('The Dealer has Blackjack you lose')
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins += 1
                break
            elif 17 <= sumD4 < 21 and sumD4 > sumE:
                print()
                print('The Dealer has a', sumD4, 'you lose')
                lose = playerbalance - playerbet
                playerbalance = lose
                print("You have", lose)
                print()
                dealer_wins += 1
                break
            elif 17 <= sumD4 < 21 and sumD4 < sumE:
                print()
                print('The Dealer has a', sumD4, 'you win')
                win = playerbalance + playerbet
                print("You have", win)
                playerbalance = win
                player_wins += 1
                print()
                break
            elif sumD4 == sumE and 21 > sumD4 >= 17:
                print()
                print('A split', sumD4, sumE)
                split = playerbet / 2
                playerbalance = playerbalance + split
                print("You have", playerbalance)
                print()
                split_w += 1
                break
            else:
                handsize += 1
