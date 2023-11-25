#fibd


def rabbit_pairs(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        rabbits = [1, 1]  # Initialize a list to store the number of rabbit pairs for each month
        for month in range(2, n+1):
            if month < m:
                rabbits.append(rabbits[-1] + rabbits[-2])  # Before reaching maturity, rabbits reproduce as Fibonacci sequence
            else:
                rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[month - m])  # After reaching maturity, rabbits only reproduce once and subtract those that die
        return rabbits[-1]

n = 6 
m = 3  

total_rabbits = rabbit_pairs(n, m)
print(total_rabbits)