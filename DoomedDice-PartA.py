total_combinations = 6 * 6
print(f'Total Combinations Possible with 2 Dice: {total_combinations}')
sum_distribution = [[i + j for j in range(1, 7)] for i in range(1, 7)]
distribution_matrix = [[(i, j) for j in range(1, 7)] for i in range(1, 7)]

print('\nDistribution Matrix for 2 Dice:')
for row in distribution_matrix:
    print(row)

print('\nSum Distribution Matrix for 2 Dice:')
for row in sum_distribution:
    print(row)

print('\nProbability Distribution for all possible Sums:')
for i in range(2, 13):
    combinations_for_sum = sum(1 for row in sum_distribution for val in row if val == i)
    probability = combinations_for_sum / total_combinations
    print(f'P(Sum = {i}): {probability}')
    
print('\nProbability Percentage Distribution for all possible Sums:')
for i in range(2, 13):
    combinations_for_sum = sum(1 for row in sum_distribution for val in row if val == i)*100
    probability = format(combinations_for_sum / total_combinations,".2f")
    print(f'P(Sum = {i}): {probability}%')
