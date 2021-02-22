
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


def is_prime(num):
    return all(num % i for i in range(2, num))


def prime_ring_problem(max_weight, circle=None):
    # by default circle init with 1
    if not circle:
        circle = [1]

    if len(circle) == max_weight and is_prime(circle[-1] + circle[0]):
        # if circle is complete
        print(circle)
        return

    for i in range(1, max_weight + 1):
        # if element no in list and sum is prime
        if i not in circle and is_prime(circle[-1] + i):
            _next = circle + [i]
            prime_ring_problem(max_weight, circle + [i])
