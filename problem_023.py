# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
#  written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from itertools import combinations

def proper_divisors(num: int):
    divisors = []
    for x in range(1, num):
        if num % x == 0:
            divisors.append(x)
    sum = 0
    for x in divisors:
        sum += x
    return sum

abundant_numbers = []
for x in range(1, 28124):
    if proper_divisors(x) > x:
        abundant_numbers.append(x)

all_integers = [x for x in range(1, 28124)]
abundant_sums = []

for var in combinations(abundant_numbers, 2):
    abundant_sums.append(var[0] + var[1])

final_list = list(set(all_integers) - set(abundant_sums))

sum = 0
for x in final_list:
    sum += x

