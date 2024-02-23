class Player:
    def __init__(self, name, batting_average, bowling_average):
        self.name = name
        self.batting_average = batting_average
        self.bowling_average = bowling_average

def compare_players(player1, player2):
    # Compare players based on their batting averages
    if player1.batting_average > player2.batting_average:
        return 1
    elif player1.batting_average < player2.batting_average:
        return -1
    else:
        # If batting averages are the same, compare based on bowling averages
        if player1.bowling_average > player2.bowling_average:
            return 1
        elif player1.bowling_average < player2.bowling_average:
            return -1
        else:
            return 0

def sort_players(queue):
    # Bubble sort implementation
    n = len(queue)
    for i in range(n - 1):
        for j in range(n - i - 1):
            player1 = queue[j]
            player2 = queue[j + 1]
            if compare_players(player1, player2) == -1:
                # Swap players
                queue[j], queue[j + 1] = queue[j + 1], queue[j]

def display_rankings(queue):
    rank = 1
    for player in queue:
        print(f"Rank {rank}: {player.name}")
        rank += 1

def search_player(queue, name):
    for player in queue:
        if player.name == name:
            return player
    return None

def update_and_sort_players(queue, update_name, new_batting_average, new_bowling_average):
    update_player = search_player(queue, update_name)

    if update_player:
        update_player.batting_average = new_batting_average
        update_player.bowling_average = new_bowling_average

        print("\nPlayer performance updated successfully!")
        print(f"Name: {update_player.name}")
        print(f"Updated Batting Average: {update_player.batting_average}")
        print(f"Updated Bowling Average: {update_player.bowling_average}")

        # After updating, sort the players
        sort_players(queue)
    else:
        print(f"\nPlayer '{update_name}' not found.")

# Create a queue to store the players
player_queue = []

# Enqueue players with their performance metrics
player_queue.append(Player("Player A", 50.5, 20.2))
player_queue.append(Player("Player B", 45.6, 18.9))
player_queue.append(Player("Player C", 55.2, 25.1))
player_queue.append(Player("Player D", 42.1, 19.5))

while True:
    # Display the current player queue with their performance
    print("\nCurrent Player Queue:")
    display_rankings(player_queue)

    # Sort the players based on performance
    sort_players(player_queue)

    # Display the rankings
    print("\nPlayer Rankings:")
    display_rankings(player_queue)

    # Option to update a player's performance
    update_name = input("\nEnter the name of the player to update (type 'exit' to stop): ")

    if update_name.lower() == 'exit':
        break

    new_batting_average = float(input("Enter new batting average: "))
    new_bowling_average = float(input("Enter new bowling average: "))

    # Update and sort players
    update_and_sort_players(player_queue, update_name, new_batting_average, new_bowling_average)

# Display the final rankings before exiting
print("\nFinal Player Rankings:")
display_rankings(player_queue)
