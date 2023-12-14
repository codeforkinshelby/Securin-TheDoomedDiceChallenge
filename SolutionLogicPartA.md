THE DOOMED DICE CHALLENGE - SOLUTION - Part A

Upon contemplating and reading the question, 
No. of Dices: 2 (6 sided)

Values in dices range from 1 to 6

Thus, 
Minimum combined sum = 1 + 1 = 2
Maximum combined sum = 6 + 6 = 12

Now for total combinations possible, since there are 2 six-sided dice, the combination would be 6*6 (6 is the number of face values on given dice):
Total = 6*6 = 36

2. If we look at the Values distribution:
S = {
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)
(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)
(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)
} 
[total of 36 combinations] or 6x6 matrix

Now going further, finding the possible sum for the above combinations
2, 3, 4, 5, 6, 7
3, 4, 5, 6, 7, 8
4, 5, 6, 7, 8, 9
5, 6, 7, 8, 9, 10
6, 7, 8, 9, 10, 11
7, 8, 9, 10, 11, 12

Formula for Probability,

Probability = (No. of favorable outcomes / Total outcomes in sample space)

For example 
To find the probability of getting Sum = 2 when rolling both dice,
Now for getting Sum value as 2, the only possible dice outcome is
Dice A = 1
Dice B = 1
Sum = 1+1 = 2

P(Sum = 2) = (probability of getting 1 while rolling Dice A)*(probability of getting 1 while rolling Dice B)

Now, 
Probability of getting 1 in Dice A = (when outcome is 1/ total outcomes possible)
P(1) = ⅙
Similarly for Dice B also the probability of getting 1 is ⅙

Thus, P(Sum = 2) = ⅙*⅙ = 1/36 = 0.02777 = 2.77%

Similarly finding all the probabilities we get,
P(Sum = 2): 0.027777777777777776 = 2.78
P(Sum = 3): 0.05555555555555555 = 5.56
P(Sum = 4): 0.08333333333333333 = 8.33
P(Sum = 5): 0.1111111111111111 = 11.11
P(Sum = 6): 0.1388888888888889 = 13.89
P(Sum = 7): 0.16666666666666666 = 16.67
P(Sum = 8): 0.1388888888888889 = 13.89
P(Sum = 9): 0.1111111111111111 = 11.11
P(Sum = 10): 0.08333333333333333 = 8.33
P(Sum = 11): 0.05555555555555555 = 5.56
P(Sum = 12): 0.027777777777777776 = 2.78
 
Logic for it is 
 Iterating through the range of starting from 2 to 12 
 Finding combinations for each sum in the distribution
 Computing the probability value for that sum combination
 Printing the computed probability value
