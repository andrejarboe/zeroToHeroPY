def count_primes(num):
    count = 0 
    index = 0

    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):
            if x % y == 0:
                break
            else:
                primes.append(x)
                x += 2
    print(primes)
    return len(primes)

count_primes(100)