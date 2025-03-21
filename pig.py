from random import randint

min_val = 1
max_val = 6

plrs = int(input("Number of players: "))
pts = {i: 0 for i in range(plrs)}

end = "\n\n"
print(end)

def roll(plr):
    curr_roll = randint(min_val, max_val)
    print(f"It looks like you rolled a {curr_roll}.", end=end)
    
    if curr_roll == 1:
        print("Sadly this means you cannot continue rolling and your points are gone. Sorry!", end=end)
        pts[plr] = 0
    else:
        pts[plr] += curr_roll
        print("Because your roll wasn't a 1, your roll's value has been added to your points.", end=end)
        print(f"Your points: {pts[plr]}.", end=end)
    
    return curr_roll

for plr in range(plrs):
    print(f"It is Player {plr + 1}'s turn. Let's see what you roll...", end=end)
    rolling = True
    curr_roll = roll(plr)
    
    while rolling and curr_roll != 1:
        again = input("Do you wish to roll again? [yes || no]: ")
        print(end)
        
        if again == "yes":
            print("Alright, rolling the die again...", end=end)
            curr_roll = roll(plr)
        elif again == "no":
            rolling = False
            print(f"Player {plr + 1} has finished rolling. Moving on to Player {plr + 2}...", end=end)

print("All players have now finished rolling. Let's see the winner...", end=end)
print(f"The winner is Player {max(pts) + 1} with {pts[max(pts)]} points!", end=end)