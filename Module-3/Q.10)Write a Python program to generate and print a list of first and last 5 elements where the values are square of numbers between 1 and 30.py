squares = [i**2 for i in range(1, 31)]
result = squares[:5] + squares[-5:]
print(result)