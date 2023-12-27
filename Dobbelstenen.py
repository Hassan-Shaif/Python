import random


# Create 2 lists
die_1 = [1, 2, 3, 4, 5, 6]
die_2 = [1, 2, 3, 4, 5, 6]

# Shuffle both dice
random.shuffle(die_1)
random.shuffle(die_2)

# Level 1:

# Set the number of rolls to 50
num_rolls = 50
outcome_list = []

# Loop to roll the dice 50 times
for i in range(num_rolls):
    roll_1 = random.choice(die_1)
    roll_2 = random.choice(die_2)
    total = roll_1 + roll_2
    outcome_list.append(total)
print(outcome_list)

# Level 2

# Change the number of rolls to 10,000
num_rolls = 10000git

# Create an empty dictionary
count_dict = {}

# Loop to roll the dice 10,000 times
for i in range(num_rolls):
    roll_1 = random.choice(die_1)
    roll_2 = random.choice(die_2)
    total = roll_1 + roll_2
    outcome_list.append(total)

# Loop to count how many times each number appears and add it to the dictionary
for number in outcome_list:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1
print(count_dict)

