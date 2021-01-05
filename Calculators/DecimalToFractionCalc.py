decimal = float(input("What is the decimal? "))

for numer in range(1, 100):
    for denom in range(1, 100):
        if (numer/denom) == decimal:
            print(f"The decimal is equivalent to {numer}/{denom}")