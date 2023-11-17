# Analysis of temperature data

# Given the integer arraytemperaturesrepresenting daily temperatures, an arrayanswerthat satisfies the following conditions is returned, print out the days with the highest and lowest temperatures (the index in thetemperaturesarray starts from day 1) and the temperature for each day, and find the average temperature for the days given in the array.
# answer[i]is the number of days you have to wait after the i-th day to get a warmer temperature.
# If there is no future day for which this is possible, keepanswer[i]as 0.

# Constraints:
# 1 ≤ temperatures.length ≤ 10⁵
# 30 ≤ temperatures[i] ≤ 100


# Input
# The elements of the integer array temperatures representing the daily temperature are separated by one space each.


# Output
# Answer[i]is output in the first line.
# In the second line, the day when the temperature is highest and the day when the temperature is lowest among the temperature information on a given date is output.
# The third line outputs the average temperature on the given days.


# Sample Input 1
# 35 36 34 33 32 31 33 35

# Sample Output 1
# [1, 0, 5, 4, 2, 1, 1, 0]
# 2 6
# 33.625


def solve(N):
    waiting = [0] * len(N)
    min_temp, max_temp = N[0], N[0]
    for n in range(0, len(N)):
        for i in range(n + 1, len(N)):
            if N[i] > N[n]:
                waiting[n] += 1
                break
            waiting[n] += 1

        if min_temp >= N[n]:
            min_temp = N[n]
            min_day = n + 1
        elif max_temp <= N[n]:
            max_temp = N[n]
            max_day = n + 1
            
    waiting[max_day-1] = 0
    print(waiting)
    print(max_day, min_day)
    print(sum(N) / len(N))


N = list(map(int, input().split()))
solve(N)
