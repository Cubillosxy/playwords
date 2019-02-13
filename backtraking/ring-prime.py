import ipdb


def check_result(result):
    _sum = result[0] + result[-1]
    # check if is prime
    return all(_sum % i for i in range(2, _sum))


def find_closest_prime(num):
    pass


def prime_ring_problem(result, max_weight):
    if not result:
        result = [1]

    #ipdb.set_trace(context=15)

    if len(result) == max_weight:
        if check_result(result):
            # is a result
            print (result)
        else:
            print('bad--------', result)

    for i in range(result[-1] + 1, max_weight + 1):
        _next = result + [i]
        prime_ring_problem(_next, max_weight)
