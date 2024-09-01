import random

def rando(range_start, range_end, count):
    if count > (range_end - range_start + 1):
        raise ValueError("Count is larger than the range of numbers available.")
    
    return random.sample(range(range_start, range_end + 1), count)

# Example usage:
unique_randoms = rando(1, 50, 5)
print("Unique random numbers:", unique_randoms)
