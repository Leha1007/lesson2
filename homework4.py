numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = len(numbers)
primes = []
not_primes = []
for elem in numbers:
    if elem != 1:
        primes.append(elem)
    for k in range(2, elem):
        if elem % k == 0:
            not_primes.append(elem)
            primes.remove(elem)
            break

print('Primes:', primes)
print('Not-primes', not_primes)
