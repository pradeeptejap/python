def print_primes_in_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# Example usage:
start_range = 10
end_range = 50
prime_numbers = print_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}:", prime_numbers)
