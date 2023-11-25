#lia
def calculate_probability(k, N):
    # Initialize a list to represent the number of Aa Bb organisms at each generation
    generation = [0] * (k + 1)
    # The 0th generation starts with one Aa Bb organism
    generation[0] = 1
    for gen in range(1, k + 1):
        # Each generation doubles in size
        generation[gen] = generation[gen - 1] * 2
    # Calculate the probability that at least N Aa Bb organisms are in the k-th generation
    probability = 0
    for i in range(N, generation[k] + 1):
        probability += (0.25 ** i) * (0.75 ** (generation[k] - i)) * comb(generation[k], i)
    return probability
# Function to calculate binomial coefficient
def comb(n, k):
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

k = 2
N = 1
result = calculate_probability(k, N)
print(result)