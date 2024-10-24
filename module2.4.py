def is_prime(num):
    if num == 1:
        return None
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if is_prime(number):
        primes.append(number)
    else:
        not_primes.append(number)
if 1 in primes:
    primes.remove(1)
if 1 in not_primes:
    not_primes.remove(1)

print("Primes:", primes)
print("Not Primes:", not_primes)