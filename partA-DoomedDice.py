#Calculating Total Combinations While Rolling 2 Dices
total = 6 * 6
print(f'\nTotal Combinations Possible with 2 Dice: {total}')

#Formulae for Distribution of face values as well as combined sum of 2 Dices
distribution = [[(i, j) for j in range(1, 7)] for i in range(1, 7)]
dicesum = [[i + j for j in range(1, 7)] for i in range(1, 7)]

#Printing face values of 2 Dices 
print('\nDistribution Matrix for 2 Dice:')
for row in distribution:
    print(row)

#Printing Combined Sum
print('\nSum Distribution Matrix for 2 Dice:')
for row in dicesum:
    print(row)

#Probability Distribution for sum values (note: min_sum = 2, max_sum = 12)
print('\nProbability Distribution for all possible Sums:')
for i in range(2, 13):
    combinations = sum(1 for row in dicesum for val in row if val == i)
    probability = combinations / total
    standard = format(combinations / total * 100,'.2f')
    print(f'P(Sum = {i}): {probability} => {standard}')

