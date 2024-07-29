numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = len(numbers)
primes = []
not_primes = []
for j in range(a):
    if numbers[j] != 1:
        primes.append(numbers[j])
    for k in range(2, numbers[j]):
        if numbers[j] % k == 0:
            not_primes.append(numbers[j])
            primes.remove(numbers[j])
            break

print('Primes:', primes)
print('Not-primes', not_primes)

