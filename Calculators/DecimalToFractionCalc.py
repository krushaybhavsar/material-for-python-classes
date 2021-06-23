decimal = float(input("What is the decimal? "))

for numer in range(1, 100):
    for denom in range(1, 100):
        if (numer/denom) == decimal:
            print(f"The decimal is equivalent to {numer}/{denom}")
            
# This is an inefficient approach since you can just use float.as_integer_ratio()
# The purpose of the excerise, however, is to get students thinking about nested for loops and code logic
