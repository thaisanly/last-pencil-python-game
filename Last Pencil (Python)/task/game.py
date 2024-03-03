import random

players = ['John', 'Jack']

pencils = input("How many pencils")

while not pencils.isnumeric() or int(pencils) <= 0:
    if not pencils.isnumeric():
        pencils = input("The number of pencils should be numeric")
    elif int(pencils) <= 0:
        pencils = input("The number of pencils should be positive")

pencils = int(pencils)

first_player_turn = input("Who will be the first (" + ', '.join(players) + "):")

while first_player_turn not in players:
    first_player_turn = input("Choose between 'John' and 'Jack'")

# swap player turn for looping
players.insert(0, players.pop(players.index(first_player_turn)))


def show_winner(player_turn):
    print([x for x in players if x != player_turn][0] + " won!")
    exit()


while pencils > 0:

    for player in players:

        print("|" * pencils)

        take_count = 0

        # Player turn
        if player == 'John':

            take_count = input(f"{player}'s turn!")

            while not take_count.isnumeric() or int(take_count) > 3 or int(take_count) <= 0 or int(
                    take_count) > pencils:
                if not take_count.isnumeric() or int(take_count) > 3 or int(take_count) <= 0:
                    take_count = input("Possible values: '1', '2' or '3'")
                elif int(take_count) > pencils:
                    take_count = input("Too many pencils were taken")

            take_count = int(take_count)

        # Bot turn
        else:
            print(f"{player}'s turn:")

            if pencils % 4 == 0:
                take_count = 3
            elif pencils % 4 == 3:
                take_count = 2
            elif pencils % 4 == 2:
                take_count = 1
            elif pencils == 3:
                take_count = 2
            elif pencils == 2:
                take_count = 1
            elif pencils == 1:
                take_count = 1
            else:
                take_count = random.randint(1, min(3, pencils))

            print(take_count)

        if pencils - take_count == 0:
            show_winner(player)
        else:
            pencils -= take_count
