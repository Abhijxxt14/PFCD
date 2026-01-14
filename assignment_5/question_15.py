# Question 15
# Modify a script to play 1,000,000 games of craps. Use two dictionaries, wins and losses, 
# to track the number of games won and lost for each roll number. Update these dictionaries 
# as the simulation progresses. For example, a key-value pair of 4: 50217 in the wins 
# dictionary would mean that 50,217 games were won on the 4th roll. At the end of the 
# simulation, display:
# (i) The percentage of games won.
# (ii) The percentage of games lost.
# (iii) The percentage of games resolved on each roll.
# (iv) The cumulative percentage of games resolved up to each roll.

import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    """Play one game of craps. Returns (result, roll_number) where result is 'win' or 'lose'"""
    roll_number = 1
    first_roll = roll_dice()
    
    # Check for immediate win or loss
    if first_roll in [7, 11]:
        return 'win', roll_number
    elif first_roll in [2, 3, 12]:
        return 'lose', roll_number
    
    # Point established
    point = first_roll
    
    while True:
        roll_number += 1
        current_roll = roll_dice()
        
        if current_roll == point:
            return 'win', roll_number
        elif current_roll == 7:
            return 'lose', roll_number

def simulate_craps(num_games=1000000):
    wins = {}
    losses = {}
    total_wins = 0
    total_losses = 0
    
    print(f"Simulating {num_games:,} games of craps...")
    
    for i in range(num_games):
        result, roll_number = play_craps()
        
        if result == 'win':
            total_wins += 1
            wins[roll_number] = wins.get(roll_number, 0) + 1
        else:
            total_losses += 1
            losses[roll_number] = losses.get(roll_number, 0) + 1
    
    # Display results
    print(f"\nSimulation complete!")
    print(f"Total games: {num_games:,}")
    print()
    
    # (i) Percentage of games won
    win_percentage = (total_wins / num_games) * 100
    print(f"Percentage of wins: {win_percentage:.2f}%")
    
    # (ii) Percentage of games lost
    loss_percentage = (total_losses / num_games) * 100
    print(f"Percentage of losses: {loss_percentage:.2f}%")
    
    # (iii) and (iv) Percentage resolved on each roll and cumulative
    print(f"\nPercentage of wins/losses resolved on each roll (based on total number of rolls):")
    print()
    print(f"{'Rolls':<8} | {'% Resolved on this roll':<25} | {'Cumulative % of games resolved'}")
    print("-" * 80)
    
    max_roll = max(max(wins.keys(), default=0), max(losses.keys(), default=0))
    cumulative_resolved = 0
    
    for roll in range(1, max_roll + 1):
        wins_on_roll = wins.get(roll, 0)
        losses_on_roll = losses.get(roll, 0)
        total_on_roll = wins_on_roll + losses_on_roll
        
        percentage_on_roll = (total_on_roll / num_games) * 100
        cumulative_resolved += percentage_on_roll
        
        print(f"{roll:<8} | {percentage_on_roll:>6.2f}%{' ':<18} | {cumulative_resolved:>6.2f}%")

# Run simulation (using smaller number for quick testing, change to 1000000 for full simulation)
num_games = int(input("Enter number of games to simulate (default 10000): ") or "10000")
simulate_craps(num_games)
