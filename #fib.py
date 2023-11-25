#fib
def rabbit_pairs(n, k):
    starting_rabbits = [1, 1]
    for i in range(2, n+1):
        next_rabbits = starting_rabbits[i - 1] + k * starting_rabbits[i - 2] 
        #fibonacci series but we multiply by k cause we get k*pairs each generation
        starting_rabbits.append(next_rabbits)
    return starting_rabbits[n - 1]
n = 28
k = 5
result = rabbit_pairs(n, k)
print(result)