import random
import time

# LIST, INPUTS, INITIALIZATION
carddeck = ["A♠", "A♣", "A♦", "A♥", "2♠", "2♣", "2♦", "2♥", "3♠", "3♣", "3♦", "3♥", "4♠", "4♣", "4♦", "4♥", "5♠", "5♣",
            "5♦", "5♥", "6♠", "6♣", "6♦", "6♥", "7♠", "7♣", "7♦", "7♥", "8♠", "8♣", "8♦", "8♥", "9♠", "9♣", "9♦", "9♥",
            "10♠", "10♣", "10♦", "10♥", "J♠", "J♣", "J♦", "J♥", "Q♠", "Q♣", "Q♦", "Q♥", "K♠", "K♣", "K♦", "K♥"]
startgame = input(
    "This is a program for Texas Hold'em Poker. There needs to be two players. Player 1 take the computer and type 'DEAL' when ready ")
player1holdings = 1000
player2holdings = 1000
startgamevariable = 0


# VALUE FUNCTION
def valuefunction(card):
    if card == carddeck[0] or card == carddeck[1] or card == carddeck[2] or card == carddeck[3]:
        cardvalue = 14
    elif card == carddeck[4] or card == carddeck[5] or card == carddeck[6] or card == carddeck[7]:
        cardvalue = 2
    elif card == carddeck[8] or card == carddeck[9] or card == carddeck[10] or card == carddeck[11]:
        cardvalue = 3
    elif card == carddeck[12] or card == carddeck[13] or card == carddeck[14] or card == carddeck[15]:
        cardvalue = 4
    elif card == carddeck[16] or card == carddeck[17] or card == carddeck[18] or card == carddeck[19]:
        cardvalue = 5
    elif card == carddeck[20] or card == carddeck[21] or card == carddeck[22] or card == carddeck[23]:
        cardvalue = 6
    elif card == carddeck[24] or card == carddeck[25] or card == carddeck[26] or card == carddeck[27]:
        cardvalue = 7
    elif card == carddeck[28] or card == carddeck[29] or card == carddeck[30] or card == carddeck[31]:
        cardvalue = 8
    elif card == carddeck[32] or card == carddeck[33] or card == carddeck[34] or card == carddeck[35]:
        cardvalue = 9
    elif card == carddeck[36] or card == carddeck[37] or card == carddeck[38] or card == carddeck[39]:
        cardvalue = 10
    elif card == carddeck[40] or card == carddeck[41] or card == carddeck[42] or card == carddeck[43]:
        cardvalue = 11
    elif card == carddeck[44] or card == carddeck[45] or card == carddeck[46] or card == carddeck[47]:
        cardvalue = 12
    elif card == carddeck[48] or card == carddeck[49] or card == carddeck[50] or card == carddeck[51]:
        cardvalue = 13
    return cardvalue


while startgame.upper() == "DEAL":
    while startgamevariable == 0:
        print("Player 1 has $" + str(player1holdings) + ", Player 2 has $" + str(player2holdings) + ", give computer to Player 1")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)
        player1card1 = ""
        player1card2 = ""
        player2card1 = ""
        player2card2 = ""
        player1hand = ""
        player2hand = ""
        flopcard1 = ""
        flopcard2 = ""
        flopcard3 = ""
        turn = ""
        river = ""
        cardvalue = 0
        player1card1value = 0
        player1card2value = 0
        player2card1value = 0
        player2card2value = 0
        flopcard1value = 0
        flopcard2value = 0
        flopcard3value = 0
        turnvalue = 0
        rivervalue = 0
        flop = ""
        board = ""
        pot1 = 0
        pot2 = 0
        pot3 = 0
        pot4 = 0
        player1betamount1 = 0
        player2betamount1 = 0
        player1betamount2 = 0
        player2betamount2 = 0
        player1betamount3 = 0
        player2betamount3 = 0
        player1betamount4 = 0
        player2betamount4 = 0
        player1fullhand = []
        player2fullhand = []
        player1fullhandvalues = []
        player2fullhandvalues = []
        paircount1 = 0
        paircount2 = 0
        holder = 0
        player1finalhand = ""
        player2finalhand = ""
        i = 0
        x = 0
        y = 0
        w = 0
        player1straightcount = 0
        player2straightcount = 0
        suitcount1 = 0
        suitcount2 = 0
        player1flushcount = 0
        player2flushcount = 0
        player1fold = 0
        player2fold = 0
        foldvar = 0
        player1pairvalue = 0
        player2pairvalue = 0
        player1pairlist = []
        player2pairlist = []
        player1straightlist = []
        player2straightlist = []
        player1flushlist = []
        player2flushlist = []

        # PLAYER 1 CARDS
        player1card1 = random.choice(carddeck)
        player1card2 = random.choice(carddeck)
        while player1card2 == player1card1:
            player1card2 = random.choice(carddeck)
        player1hand = player1card1 + " " + player1card2
        print("Player 1: your hand is: " + player1hand + ", you have $" + str(player1holdings))

        # PLAYER 1 PRE-FLOP BET
        player1betamount1 = input("How much would you like to bet? ")
        if str(player1betamount1.upper()) == "FOLD":
            print("PLAYER 2 WINS!")
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player1betamount1 = int(player1betamount1)
        if player1betamount1 > player1holdings:
            player1betamount1 = input("You don't have enough for this bet. How much would you like to bet? ")
        print("Give computer to player 2")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 2 CARDS
        player2card1 = random.choice(carddeck)
        while player2card1 == player1card1 or player2card1 == player1card2:
            player2card1 = random.choice(carddeck)
        player2card2 = random.choice(carddeck)
        while player2card2 == player1card1 or player2card2 == player1card2 or player2card2 == player2card1:
            player2card2 = random.choice(carddeck)
        player2hand = player2card1 + " " + player2card2
        print("Player 2: your hand is: " + player2hand + ", you have $" + str(player2holdings))

        # PLAYER 2 PRE-FLOP BET
        player2betamount1 = input(
            "Player 2: The current bet is " + str(player1betamount1) + ". Bet your desired amount or enter in FOLD ")
        if str(player2betamount1.upper()) == "FOLD":
            print("PLAYER 1 WINS!")
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player2betamount1 = int(player2betamount1)
        if player2betamount1 > player2holdings:
            player2betamount1 = input("You don't have enough for this bet. How much would you like to bet? ")

        # MATCHING PRE-FLOP
        while player2betamount1 != player1betamount1:
            while player1betamount1 < player2betamount1:
                print("Give computer to player 1")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player1betamount1
                player1betamount1 = input("Player 1: How much would you like to bet? The current bet is " + str(
                    player2betamount1) + ". Your hand is " + player1hand + " ")
                if str(player1betamount1.upper()) == "FOLD":
                    print("PLAYER 2 WINS!")
                    player2holdings += foldvar
                    player1holdings -= foldvar
                    player1fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player1betamount1 = int(player1betamount1)
                    if player1betamount1 > player1holdings:
                        player1betamount1 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player1fold == 1:
                break
            while player2betamount1 < player1betamount1:
                print("Give computer to player 2")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player2betamount1
                player2betamount1 = input("Player 2: How much would you like to bet? The current bet is " + str(
                    player1betamount1) + ". Your hand is " + player2hand + " ")
                if str(player2betamount1.upper()) == "FOLD":
                    print("PLAYER 1 WINS!")
                    player1holdings += foldvar
                    player2holdings -= foldvar
                    player2fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player2betamount1 = int(player2betamount1)
                    if player2betamount1 > player2holdings:
                        player2betamount1 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player2fold == 1:
                break
        if player1fold == 1 or player2fold == 1:
            break
        player1holdings -= player1betamount1
        player2holdings -= player2betamount1

        # FLOP
        flopcard1 = random.choice(carddeck)
        while flopcard1 == player1card1 or flopcard1 == player1card2 or flopcard1 == player2card1 or flopcard1 == player2card2:
            flopcard1 = random.choice(carddeck)
        flopcard2 = random.choice(carddeck)
        while flopcard2 == player1card1 or flopcard2 == player1card2 or flopcard2 == player2card1 or flopcard2 == player2card2 or flopcard2 == flopcard1:
            flopcard2 = random.choice(carddeck)
        flopcard3 = random.choice(carddeck)
        while flopcard3 == player1card1 or flopcard3 == player1card2 or flopcard3 == player2card1 or flopcard3 == player2card2 or flopcard3 == flopcard1 or flopcard3 == flopcard2:
            flopcard3 = random.choice(carddeck)
        flop = flopcard1 + " " + flopcard2 + " " + flopcard3
        print("Give computer to player 1")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 1 POST-FLOP BET
        print("The flop is: " + flop + ", Your hand is " + player1hand)
        player1betamount2 = input(
            "Player 1: How much would you like to bet? You have $" + str(player1holdings) + " left ")
        if str(player1betamount2.upper()) == "FOLD":
            print("PLAYER 2 WINS!")
            player2holdings += (player1betamount1 + player2betamount1)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player1betamount2 = int(player1betamount2)
        if player1betamount2 > player1holdings:
            player1betamount2 = input("You don't have enough for this bet. How much would you like to bet? ")
        print("Give computer to player 2")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 2 POST-FLOP BET
        print("The flop is: " + flop + ", Your hand is " + player2hand)
        player2betamount2 = input("Player 2: The current bet is " + str(player1betamount2) + ". You have $" + str(
            player2holdings) + ". Bet your desired amount or enter in FOLD ")
        if str(player2betamount2.upper()) == "FOLD":
            print("PLAYER 1 WINS!")
            player1holdings += (player1betamount1 + player2betamount1)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player2betamount2 = int(player2betamount2)
        if player2betamount2 > player2holdings:
            player2betamount2 = input("You don't have enough for this bet. How much would you like to bet? ")

        # MATCHING POST-FLOP
        while player2betamount2 != player1betamount2:
            while player1betamount2 < player2betamount2:
                print("Give computer to player 1")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player1betamount2
                player1betamount2 = input("BOARD: " + flop + "     Player 1: How much would you like to bet? The current bet is " + str(
                    player2betamount2) + ". Your hand is " + player1hand + " ")
                if str(player1betamount2.upper()) == "FOLD":
                    print("PLAYER 2 WINS!")
                    player2holdings += foldvar
                    player1holdings -= foldvar
                    player1fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player1betamount2 = int(player1betamount2)
                    if player1betamount2 > player1holdings:
                        player1betamount2 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player1fold == 1:
                break
            while player2betamount2 < player1betamount2:
                print("Give computer to player 2")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player2betamount2
                player2betamount2 = input("BOARD: " + flop + "     Player 2: How much would you like to bet? The current bet is " + str(
                    player1betamount2) + ". Your hand is " + player2hand + " ")
                if str(player2betamount2.upper()) == "FOLD":
                    print("PLAYER 1 WINS!")
                    player1holdings += foldvar
                    player2holdings -= foldvar
                    player2fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player2betamount2 = int(player2betamount2)
                    if player2betamount2 > player2holdings:
                        player2betamount2 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player2fold == 1:
                break
        if player1fold == 1 or player2fold == 1:
            break
        player1holdings -= player1betamount2
        player2holdings -= player2betamount2

        # TURN
        turn = random.choice(carddeck)
        while turn == player1card1 or turn == player1card2 or turn == player2card1 or turn == player2card2 or turn == flopcard1 or turn == flopcard2 or turn == flopcard3:
            turn = random.choice(carddeck)
        board = flop + " " + turn
        print("Give computer to player 1")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 1 POST-TURN BET
        print("The board is: " + board + ", Your hand is " + player1hand)
        player1betamount3 = input(
            "Player 1: How much would you like to bet? You have $" + str(player1holdings) + " left ")
        if str(player1betamount3.upper()) == "FOLD":
            print("PLAYER 2 WINS!")
            player2holdings += (player1betamount1 + player2betamount1 + player1betamount2 + player2betamount2)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player1betamount3 = int(player1betamount3)
        if player1betamount3 > player1holdings:
            player1betamount3 = input("You don't have enough for this bet. How much would you like to bet? ")
        print("Give computer to player 2")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 2 POST-TURN BET
        print("The board is: " + board + ", Your hand is " + player2hand)
        player2betamount3 = input("Player 2: The current bet is " + str(player1betamount3) + ". You have $" + str(
            player2holdings) + ". Bet your desired amount or enter in FOLD ")
        if str(player2betamount3.upper()) == "FOLD":
            print("PLAYER 1 WINS!")
            player1holdings += (player1betamount1 + player2betamount1 + player1betamount2 + player2betamount2)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player2betamount3 = int(player2betamount3)
        if player2betamount3 > player2holdings:
            player2betamount3 = input("You don't have enough for this bet. How much would you like to bet? ")

        # POST-TURN MATCHING
        while player2betamount3 != player1betamount3:
            while player1betamount3 < player2betamount3:
                print("Give computer to player 1")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player1betamount3
                player1betamount3 = input("BOARD: " + board + "     Player 1: How much would you like to bet? The current bet is " + str(
                    player2betamount3) + ". Your hand is " + player1hand + " ")
                if str(player1betamount3.upper()) == "FOLD":
                    print("PLAYER 2 WINS!")
                    player2holdings += foldvar
                    player1holdings -= foldvar
                    player1fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player1betamount3 = int(player1betamount3)
                    if player1betamount3 > player1holdings:
                        player1betamount3 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player1fold == 1:
                break
            while player2betamount3 < player1betamount3:
                print("Give computer to player 2")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player2betamount3
                player2betamount3 = input("BOARD: " + board + "     Player 2: How much would you like to bet? The current bet is " + str(
                    player1betamount3) + ". Your hand is " + player2hand + " ")
                if str(player2betamount3.upper()) == "FOLD":
                    print("PLAYER 1 WINS!")
                    player1holdings += foldvar
                    player2holdings -= foldvar
                    player2fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player2betamount3 = int(player2betamount3)
                    if player2betamount3 > player2holdings:
                        player2betamount3 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player2fold == 1:
                break
        if player1fold == 1 or player2fold == 1:
            break
        player1holdings -= player1betamount3
        player2holdings -= player2betamount3

        # RIVER
        river = random.choice(carddeck)
        while river == player1card1 or river == player1card2 or river == player2card1 or river == player2card2 or river == flopcard1 or river == flopcard2 or river == flopcard3 or river == turn:
            river = random.choice(carddeck)
        board = flop + " " + turn + " " + river
        print("Give computer to player 1")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 1 POST-RIVER BET
        print("The board is: " + board + ", Your hand is " + player1hand)
        player1betamount4 = input(
            "Player 1: How much would you like to bet? You have $" + str(player1holdings) + " left ")
        if str(player1betamount4.upper()) == "FOLD":
            print("PLAYER 2 WINS!")
            player2holdings += (
                        player1betamount1 + player2betamount1 + player1betamount2 + player2betamount2 + player1betamount3 + player2betamount3)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player1betamount4 = int(player1betamount4)
        if player1betamount4 > player1holdings:
            player1betamount4 = input("You don't have enough for this bet. How much would you like to bet? ")
        print("Give computer to player 2")
        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # PLAYER 2 POST-RIVER BET
        print("The board is: " + board + ", Your hand is " + player2hand)
        player2betamount4 = input("Player 2: The current bet is " + str(player1betamount4) + ". You have $" + str(
            player2holdings) + ". Bet your desired amount or enter in FOLD ")
        if str(player2betamount4.upper()) == "FOLD":
            print("PLAYER 1 WINS!")
            player1holdings += (
                        player1betamount1 + player2betamount1 + player1betamount2 + player2betamount2 + player1betamount3 + player2betamount3)
            print("Give computer to player 1")
            time.sleep(0)
            for x in range(100):
                print()
            time.sleep(0)
            break
        player2betamount4 = int(player2betamount4)
        if player2betamount4 > player2holdings:
            player2betamount4 = input("You don't have enough for this bet. How much would you like to bet? ")

        # POST-RIVER MATCHING
        while player2betamount4 != player1betamount4:
            while player1betamount4 < player2betamount4:
                print("Give computer to player 1")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player1betamount4
                player1betamount4 = input("BOARD: " + board + "     Player 1: How much would you like to bet? The current bet is " + str(
                    player2betamount4) + ". Your hand is " + player1hand + " ")
                if str(player1betamount4.upper()) == "FOLD":
                    print("PLAYER 2 WINS!")
                    player2holdings += foldvar
                    player1holdings -= foldvar
                    player1fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player1betamount4 = int(player1betamount4)
                    if player1betamount4 > player1holdings:
                        player1betamount4 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player1fold == 1:
                break
            while player2betamount4 < player1betamount4:
                print("Give computer to player 2")
                time.sleep(0)
                for x in range(100):
                    print()
                time.sleep(0)
                foldvar = player2betamount4
                player2betamount4 = input("BOARD: " + board + "     Player 2: How much would you like to bet? The current bet is " + str(
                    player1betamount4) + ". Your hand is " + player2hand + " ")
                if str(player2betamount4.upper()) == "FOLD":
                    print("PLAYER 1 WINS!")
                    player1holdings += foldvar
                    player2holdings -= foldvar
                    player2fold = 1
                    print("Give computer to player 1")
                    time.sleep(0)
                    for x in range(100):
                        print()
                    time.sleep(0)
                    break
                else:
                    player2betamount4 = int(player2betamount4)
                    if player2betamount4 > player2holdings:
                        player2betamount4 = input(
                            "You don't have enough for this bet. How much would you like to bet? ")
            if player2fold == 1:
                break
        if player1fold == 1 or player2fold == 1:
            break
        player1holdings -= player1betamount4
        player2holdings -= player2betamount4

        time.sleep(0)
        for x in range(100):
            print()
        time.sleep(0)

        # FULL HAND LISTS
        player1fullhand.append(player1card1)
        player1fullhand.append(player1card2)
        player1fullhand.append(flopcard1)
        player1fullhand.append(flopcard2)
        player1fullhand.append(flopcard3)
        player1fullhand.append(turn)
        player1fullhand.append(river)
        player2fullhand.append(player2card1)
        player2fullhand.append(player2card2)
        player2fullhand.append(flopcard1)
        player2fullhand.append(flopcard2)
        player2fullhand.append(flopcard3)
        player2fullhand.append(turn)
        player2fullhand.append(river)

        # VALUE ASSIGNMENT
        player1card1value = valuefunction(player1card1)
        player1card2value = valuefunction(player1card2)
        player2card1value = valuefunction(player2card1)
        player2card2value = valuefunction(player2card2)
        flopcard1value = valuefunction(flopcard1)
        flopcard2value = valuefunction(flopcard2)
        flopcard3value = valuefunction(flopcard3)
        turnvalue = valuefunction(turn)
        rivervalue = valuefunction(river)

        # DETERMINE PLAYER 1 HAND -- PAIRS
        for i in range(len(player1fullhand)):
            holder = valuefunction(player1fullhand[i])
            for x in range(len(player1fullhand)):
                if x != i:
                    if valuefunction(player1fullhand[x]) == holder:
                        paircount1 += 1
                        player1pairlist.append(valuefunction(player1fullhand[x]))

        paircount1 /= 2

        # DETERMINE PLAYER 2 HAND -- PAIRS
        for i in range(len(player2fullhand)):
            holder = valuefunction(player2fullhand[i])
            for x in range(len(player2fullhand)):
                if x != i:
                    if valuefunction(player2fullhand[x]) == holder:
                        paircount2 += 1
                        player2pairlist.append(valuefunction(player1fullhand[x]))
        paircount2 /= 2

        # VALUE LISTS
        player1fullhandvalues.append(player1card1value)
        player1fullhandvalues.append(player1card2value)
        player1fullhandvalues.append(flopcard1value)
        player1fullhandvalues.append(flopcard2value)
        player1fullhandvalues.append(flopcard3value)
        player1fullhandvalues.append(turnvalue)
        player1fullhandvalues.append(rivervalue)
        player2fullhandvalues.append(player2card1value)
        player2fullhandvalues.append(player2card2value)
        player2fullhandvalues.append(flopcard1value)
        player2fullhandvalues.append(flopcard2value)
        player2fullhandvalues.append(flopcard3value)
        player2fullhandvalues.append(turnvalue)
        player2fullhandvalues.append(rivervalue)

        # DETERMINE PLAYER 1 HAND -- STRAIGHT
        for i in range(len(player1fullhand)):
            if player1fullhandvalues[i] + 1 == player1card1value or player1fullhandvalues[i] + 1 == player1card2value or \
                    player1fullhandvalues[i] + 1 == flopcard1value or player1fullhandvalues[i] + 1 == flopcard2value or \
                    player1fullhandvalues[i] + 1 == flopcard3value or player1fullhandvalues[i] + 1 == turnvalue or \
                    player1fullhandvalues[i] + 1 == rivervalue:
                if player1fullhandvalues[i] + 2 == player1card1value or player1fullhandvalues[
                    i] + 2 == player1card2value or player1fullhandvalues[i] + 2 == flopcard1value or \
                        player1fullhandvalues[i] + 2 == flopcard2value or player1fullhandvalues[
                    i] + 2 == flopcard3value or player1fullhandvalues[i] + 2 == turnvalue or player1fullhandvalues[
                    i] + 2 == rivervalue:
                    if player1fullhandvalues[i] + 3 == player1card1value or player1fullhandvalues[
                        i] + 3 == player1card2value or player1fullhandvalues[i] + 3 == flopcard1value or \
                            player1fullhandvalues[i] + 3 == flopcard2value or player1fullhandvalues[
                        i] + 3 == flopcard3value or player1fullhandvalues[i] + 3 == turnvalue or player1fullhandvalues[
                        i] + 3 == rivervalue:
                        if player1fullhandvalues[i] + 4 == player1card1value or player1fullhandvalues[
                            i] + 4 == player1card2value or player1fullhandvalues[i] + 4 == flopcard1value or \
                                player1fullhandvalues[i] + 4 == flopcard2value or player1fullhandvalues[
                            i] + 4 == flopcard3value or player1fullhandvalues[i] + 4 == turnvalue or \
                                player1fullhandvalues[i] + 4 == rivervalue:
                            player1straightcount += 1
                            player1straightlist.append(player1fullhandvalues[i])
                            player1straightlist.append(player1fullhandvalues[i] + 1)
                            player1straightlist.append(player1fullhandvalues[i] + 2)
                            player1straightlist.append(player1fullhandvalues[i] + 3)
                            player1straightlist.append(player1fullhandvalues[i] + 4)
            if player1straightcount == 0:
                if player1straightcount == 1 and max(player1straightlist) == 6:
                    if (
                            player1card1value == 14 or player1card2value == 14 or flopcard1value == 14 or flopcard2value == 14 or flopcard3value == 14 or turnvalue == 14 or rivervalue == 14) and (
                            player1card1value == 2 or player1card2value == 2 or flopcard1value == 2 or flopcard2value == 2 or flopcard3value == 2 or turnvalue == 2 or rivervalue == 2) and (
                            player1card1value == 3 or player1card2value == 3 or flopcard1value == 3 or flopcard2value == 3 or flopcard3value == 3 or turnvalue == 3 or rivervalue == 3) and (
                            player1card1value == 4 or player1card2value == 4 or flopcard1value == 4 or flopcard2value == 4 or flopcard3value == 4 or turnvalue == 4 or rivervalue == 4) and (
                            player1card1value == 5 or player1card2value == 5 or flopcard1value == 5 or flopcard2value == 5 or flopcard3value == 5 or turnvalue == 5 or rivervalue == 5):
                        player1straightcount += 1
                        player1straightlist.append(14)
                        player1straightlist.append(2)
                        player1straightlist.append(3)
                        player1straightlist.append(4)
                        player1straightlist.append(5)

        # DETERMINE PLAYER 2 HAND -- STRAIGHT
        for i in range(len(player2fullhand)):
            if player2fullhandvalues[i] + 1 == player2card1value or player2fullhandvalues[i] + 1 == player2card2value or \
                    player2fullhandvalues[i] + 1 == flopcard1value or player2fullhandvalues[i] + 1 == flopcard2value or \
                    player2fullhandvalues[i] + 1 == flopcard3value or player2fullhandvalues[i] + 1 == turnvalue or \
                    player2fullhandvalues[i] + 1 == rivervalue:
                if player2fullhandvalues[i] + 2 == player2card1value or player2fullhandvalues[
                    i] + 2 == player2card2value or player2fullhandvalues[i] + 2 == flopcard1value or \
                        player2fullhandvalues[i] + 2 == flopcard2value or player2fullhandvalues[
                    i] + 2 == flopcard3value or player2fullhandvalues[i] + 2 == turnvalue or player2fullhandvalues[
                    i] + 2 == rivervalue:
                    if player2fullhandvalues[i] + 3 == player2card1value or player2fullhandvalues[
                        i] + 3 == player2card2value or player2fullhandvalues[i] + 3 == flopcard1value or \
                            player2fullhandvalues[i] + 3 == flopcard2value or player2fullhandvalues[
                        i] + 3 == flopcard3value or player2fullhandvalues[i] + 3 == turnvalue or player2fullhandvalues[
                        i] + 3 == rivervalue:
                        if player2fullhandvalues[i] + 4 == player2card1value or player2fullhandvalues[
                            i] + 4 == player2card2value or player2fullhandvalues[i] + 4 == flopcard1value or \
                                player2fullhandvalues[i] + 4 == flopcard2value or player2fullhandvalues[
                            i] + 4 == flopcard3value or player2fullhandvalues[i] + 4 == turnvalue or \
                                player2fullhandvalues[i] + 4 == rivervalue:
                            player2straightcount += 1
                            player2straightlist.append(player2fullhandvalues[i])
                            player2straightlist.append(player2fullhandvalues[i] + 1)
                            player2straightlist.append(player2fullhandvalues[i] + 2)
                            player2straightlist.append(player2fullhandvalues[i] + 3)
                            player2straightlist.append(player2fullhandvalues[i] + 4)
            if player2straightcount == 0:
                if (
                        player2card1value == 14 or player2card2value == 14 or flopcard1value == 14 or flopcard2value == 14 or flopcard3value == 14 or turnvalue == 14 or rivervalue == 14) and (
                        player2card1value == 2 or player2card2value == 2 or flopcard1value == 2 or flopcard2value == 2 or flopcard3value == 2 or turnvalue == 2 or rivervalue == 2) and (
                        player2card1value == 3 or player2card2value == 3 or flopcard1value == 3 or flopcard2value == 3 or flopcard3value == 3 or turnvalue == 3 or rivervalue == 3) and (
                        player2card1value == 4 or player2card2value == 4 or flopcard1value == 4 or flopcard2value == 4 or flopcard3value == 4 or turnvalue == 4 or rivervalue == 4) and (
                        player2card1value == 5 or player2card2value == 5 or flopcard1value == 5 or flopcard2value == 5 or flopcard3value == 5 or turnvalue == 5 or rivervalue == 5):
                    player2straightcount += 1
                    player2straightlist.append(14)
                    player2straightlist.append(2)
                    player2straightlist.append(3)
                    player2straightlist.append(4)
                    player2straightlist.append(5)
            if player2straightcount == 1 and max(player2straightlist) == 6:
                if (
                        player2card1value == 14 or player2card2value == 14 or flopcard1value == 14 or flopcard2value == 14 or flopcard3value == 14 or turnvalue == 14 or rivervalue == 14) and (
                        player2card1value == 2 or player2card2value == 2 or flopcard1value == 2 or flopcard2value == 2 or flopcard3value == 2 or turnvalue == 2 or rivervalue == 2) and (
                        player2card1value == 3 or player2card2value == 3 or flopcard1value == 3 or flopcard2value == 3 or flopcard3value == 3 or turnvalue == 3 or rivervalue == 3) and (
                        player2card1value == 4 or player2card2value == 4 or flopcard1value == 4 or flopcard2value == 4 or flopcard3value == 4 or turnvalue == 4 or rivervalue == 4) and (
                        player2card1value == 5 or player2card2value == 5 or flopcard1value == 5 or flopcard2value == 5 or flopcard3value == 5 or turnvalue == 5 or rivervalue == 5):
                    player2straightcount += 1
                    player2straightlist.append(14)
                    player2straightlist.append(2)
                    player2straightlist.append(3)
                    player2straightlist.append(4)
                    player2straightlist.append(5)

        # DETERMINE PLAYER 1 HAND -- FLUSH
        for i in range(len(player1fullhand)):
            holder = player1fullhand[i][1]
            for x in range(len(player1fullhand)):
                if x != i:
                    if player1fullhand[x][1] == holder:
                        suitcount1 += 1
                        player1flushlist.append(valuefunction(player1fullhand[x]))
        if suitcount1 >= 20:
            player1flushcount = 1

        # DETERMINE PLAYER 2 HAND -- FLUSH
        for i in range(len(player2fullhand)):
            holder = player2fullhand[i][1]
            for x in range(len(player2fullhand)):
                if x != i:
                    if player2fullhand[x][1] == holder:
                        suitcount2 += 1
                        player2flushlist.append(valuefunction(player1fullhand[x]))
        if suitcount2 >= 20:
            player2flushcount = 1

        # ASSIGNING FINAL HAND
        # PAIRS
        if paircount1 == 1:
            player1finalhand = "1 PAIR"
        if paircount1 == 2:
            player1finalhand = "2 PAIR"
        if paircount1 == 3:
            player1finalhand = "3 KIND"
        if paircount1 == 4:
            player1finalhand = "FULL HOUSE"
        if paircount1 == 6:
            player1finalhand = "4 KIND"
        if paircount2 == 1:
            player2finalhand = "1 PAIR"
        if paircount2 == 2:
            player2finalhand = "2 PAIR"
        if paircount2 == 3:
            player2finalhand = "3 KIND"
        if paircount2 == 4:
            player2finalhand = "FULL HOUSE"
        if paircount2 == 6:
            player2finalhand = "4 KIND"

        # STRAIGHT
        if player1straightcount >= 1:
            player1finalhand = "STRAIGHT"
        if player2straightcount >= 1:
            player2finalhand = "STRAIGHT"

        # FLUSH
        if player1flushcount >= 1:
            player1finalhand = "FLUSH"
        if player2flushcount >= 1:
            player2finalhand = "FLUSH"

        # HIGH CARD
        if paircount1 == 0 and player1straightcount == 0 and player1flushcount == 0:
            player1finalhand = "HIGH CARD OF " + player1fullhand[
                player1fullhandvalues.index(max(player1fullhandvalues))]
        if paircount2 == 0 and player2straightcount == 0 and player2flushcount == 0:
            player2finalhand = "HIGH CARD OF " + player2fullhand[
                player2fullhandvalues.index(max(player2fullhandvalues))]

        # END GAME PRINT STATEMENTS
        print(board)
        print("Player 1 (" + player1hand + ") had a " + player1finalhand + "!")
        print("Player 2 (" + player2hand + ") had a " + player2finalhand + "!")

        # WINNER DETERMINATION
        # PAIRS
        if paircount1 == 1:
            player1finalhand = 1
        if paircount1 == 2:
            player1finalhand = 2
        if paircount1 == 3:
            player1finalhand = 3
        if paircount1 == 4:
            player1finalhand = 6
        if paircount1 == 6:
            player1finalhand = 7
        if paircount2 == 1:
            player2finalhand = 1
        if paircount2 == 2:
            player2finalhand = 2
        if paircount2 == 3:
            player2finalhand = 3

        # STRAIGHT
        if player1straightcount >= 1:
            player1finalhand = 4
        if player2straightcount >= 1:
            player2finalhand = 4

        # FLUSH
        if player1flushcount >= 1:
            player1finalhand = 5
        if player2flushcount >= 1:
            player2finalhand = 5

        # PAIR CONT
        if paircount2 == 4:
            player2finalhand = 6
        if paircount2 == 6:
            player2finalhand = 7

        # HIGH CARD
        if paircount1 == 0 and player1straightcount == 0 and player1flushcount == 0:
            player1finalhand = 0
        if paircount2 == 0 and player2straightcount == 0 and player2flushcount == 0:
            player2finalhand = 0

        # END ROUND
        totalearningsplayer1 = player2betamount1 + player2betamount2 + player2betamount3 + player2betamount4
        totalearningsplayer2 = player1betamount1 + player1betamount2 + player1betamount3 + player1betamount4
        if player2finalhand > player1finalhand:
            print("PLAYER 2 WINS!")
            player2holdings += (totalearningsplayer1 + totalearningsplayer2)
        elif player2finalhand == player1finalhand:
            if player2finalhand == 0:
                if max(player2fullhandvalues) > max(player1fullhandvalues):
                    print("PLAYER 2 WINS!")
                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif max(player1fullhandvalues) > max(player2fullhandvalues):
                    print("PLAYER 1 WINS!")
                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif max(player1fullhandvalues) == max(player2fullhandvalues):
                    player1fullhandvalues.remove(max(player1fullhandvalues))
                    player2fullhandvalues.remove(max(player2fullhandvalues))
                    if max(player2fullhandvalues) > max(player1fullhandvalues):
                        print("PLAYER 2 WINS!")
                        player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                    elif max(player1fullhandvalues) > max(player2fullhandvalues):
                        print("PLAYER 1 WINS!")
                        player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                    elif max(player1fullhandvalues) == max(player2fullhandvalues):
                        player1fullhandvalues.remove(max(player1fullhandvalues))
                        player2fullhandvalues.remove(max(player2fullhandvalues))
                        if max(player2fullhandvalues) > max(player1fullhandvalues):
                            print("PLAYER 2 WINS!")
                            player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                        elif max(player1fullhandvalues) > max(player2fullhandvalues):
                            print("PLAYER 1 WINS!")
                            player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                        elif max(player1fullhandvalues) == max(player2fullhandvalues):
                            player1fullhandvalues.remove(max(player1fullhandvalues))
                            player2fullhandvalues.remove(max(player2fullhandvalues))
                            if max(player2fullhandvalues) > max(player1fullhandvalues):
                                print("PLAYER 2 WINS!")
                                player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                            elif max(player1fullhandvalues) > max(player2fullhandvalues):
                                print("PLAYER 1 WINS!")
                                player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                            elif max(player1fullhandvalues) == max(player2fullhandvalues):
                                player1fullhandvalues.remove(max(player1fullhandvalues))
                                player2fullhandvalues.remove(max(player2fullhandvalues))
                                if max(player2fullhandvalues) > max(player1fullhandvalues):
                                    print("PLAYER 2 WINS!")
                                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                                elif max(player1fullhandvalues) > max(player2fullhandvalues):
                                    print("PLAYER 1 WINS!")
                                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                                elif max(player1fullhandvalues) == max(player2fullhandvalues):
                                    print("TIE!")
                                    player1holdings += totalearningsplayer1
                                    player2holdings += totalearningsplayer2
            elif player2finalhand == 1 or player2finalhand == 2 or player2finalhand == 3 or player2finalhand == 6 or player2finalhand == 7:
                if max(player1pairlist) > max(player2pairlist):
                    print("PLAYER 1 WINS!")
                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif max(player1pairlist) < max(player2pairlist):
                    print("PLAYER 2 WINS!")
                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif player1pairvalue == player2pairvalue:
                    if max(player2fullhandvalues) > max(player1fullhandvalues):
                        print("PLAYER 2 WINS!")
                        player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                    elif max(player1fullhandvalues) > max(player2fullhandvalues):
                        print("PLAYER 1 WINS!")
                        player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                    elif max(player1fullhandvalues) == max(player2fullhandvalues):
                        player1fullhandvalues.remove(max(player1fullhandvalues))
                        player2fullhandvalues.remove(max(player2fullhandvalues))
                        if max(player2fullhandvalues) > max(player1fullhandvalues):
                            print("PLAYER 2 WINS!")
                            player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                        elif max(player1fullhandvalues) > max(player2fullhandvalues):
                            print("PLAYER 1 WINS!")
                            player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                        elif max(player1fullhandvalues) == max(player2fullhandvalues):
                            player1fullhandvalues.remove(max(player1fullhandvalues))
                            player2fullhandvalues.remove(max(player2fullhandvalues))
                            if max(player2fullhandvalues) > max(player1fullhandvalues):
                                print("PLAYER 2 WINS!")
                                player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                            elif max(player1fullhandvalues) > max(player2fullhandvalues):
                                print("PLAYER 1 WINS!")
                                player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                            elif max(player1fullhandvalues) == max(player2fullhandvalues):
                                player1fullhandvalues.remove(max(player1fullhandvalues))
                                player2fullhandvalues.remove(max(player2fullhandvalues))
                                if max(player2fullhandvalues) > max(player1fullhandvalues):
                                    print("PLAYER 2 WINS!")
                                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                                elif max(player1fullhandvalues) > max(player2fullhandvalues):
                                    print("PLAYER 1 WINS!")
                                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                                elif max(player1fullhandvalues) == max(player2fullhandvalues):
                                    print("TIE!")
                                    player1holdings += totalearningsplayer1
                                    player2holdings += totalearningsplayer2

            elif player2finalhand == 4:
                if max(player2straightlist) > max(player1straightlist):
                    print("PLAYER 2 WINS!")
                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif max(player2straightlist) < max(player1straightlist):
                    print("PLAYER 1 WINS!")
                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                else:
                    print("TIE!")
                    player1holdings += totalearningsplayer1
                    player2holdings += totalearningsplayer2

            elif player2finalhand == 5:
                if max(player2flushlist) > max(player1flushlist):
                    print("PLAYER 2 WINS!")
                    player2holdings += (totalearningsplayer1 + totalearningsplayer2)
                elif max(player2flushlist) < max(player1flushlist):
                    print("PLAYER 1 WINS!")
                    player1holdings += (totalearningsplayer1 + totalearningsplayer2)
                else:
                    print("TIE!")
                    player1holdings += totalearningsplayer1
                    player2holdings += totalearningsplayer2

        elif player1finalhand > player2finalhand:
            print("PLAYER 1 WINS!")
            player1holdings += (totalearningsplayer1 + totalearningsplayer2)

        # RESTART GAME
        print("PLAYER 1 HAS $" + str(player1holdings))
        print("PLAYER 2 HAS $" + str(player2holdings))
        startgame = input("Enter 'DEAL' to deal again ")