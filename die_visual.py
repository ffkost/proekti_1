

'''import pandas
import plotly.express as px

from die import Die

#Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#fig = px.bar(x=poss_results, y=frequencies)
fig.show()

print(frequencies)

print(results)'''

import pandas
import plotly.express as px
from random import randint
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
def get_die_sides(a):
    flag = 1
    while flag:
        b = input(f"{a} (must be between 2 and 10): ")#ifnot infloop
        if b.isdigit():
            sides = int(b)
            if 2 <= sides <= 10:
                flag = 0
                return sides
            else:
                print("Invalid input! Please enter a number between 2 and 10.")
        else:
            print("Invalid input! Please enter a valid number.")
die1_N_sides = get_die_sides("Enter the number of sides for the first die")
die2_N_sides = get_die_sides("Enter the number of sides for the second die")
die_1 = Die(die1_N_sides)
die_2 = Die(die2_N_sides)
while True:
    try:
        num_rolls = int(input("Enter the number of rolls (e.g., 5000000): "))
        if num_rolls > 0:
            break
        else:
            print("Please enter a positive number!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
results = []
for roll_num in range(num_rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1) #
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = f"Results of Rolling a {die_1.num_sides}-sided Die and a {die_2.num_sides}-sided Die {num_rolls} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
#fig.write_html('dice_visual_d6d10.html') # for save html

print(frequencies)

print(results)

# Create two D6 dice.
#die_1 = Die()  #
#die_2 = Die()  #

# Create a D6 and a D10.
#die_1 = Die()
#die_2 = Die(10)
#fig = px.bar(x=poss_results, y=frequencies)