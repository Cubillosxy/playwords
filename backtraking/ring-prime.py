import ipdb


def check_prime(num):
    return all(num % i for i in range(2, num))


def prime_ring_problem(max_weight, result=None):
    if not result:
        result = [1]

    if len(result) == max_weight and check_prime(result[-1] + 1):
        print(result)
        return

    for i in range(2, max_weight + 1):
        if i not in result and check_prime(result[-1] + i):
            _next = result + [i]
            prime_ring_problem(max_weight, _next)



