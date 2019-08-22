import ipdb


def find_min_swap(lenn, list_num, pivot=0, pointer=-1):
    ipdb.set_trace(context=10)
    if pivot == pointer:
        return 0

    left = list_num[0:pivot]
    right = list_num[pivot:]

    final_cont = 0
    cont_r = 0
    for i in range(len(right), 0, -1):
        if list_num[pivot] > right[i-1]:
            list_num[pivot], list_num[i-1] = list_num[i-1], list_num[pivot]
            return 1 + find_min_swap(lenn, list_num, i - 1, pivot)
        cont_r += 1

    if cont_r == len(right) and len(right) != len(list_num):
        final_cont += find_min_swap(lenn, right, 0, -1)

    cont_l = 0
    for i in range(0, len(left)):
        if list_num[pivot] < left[i]:
            list_num[pivot], list_num[i] = list_num[i], list_num[pivot]
            return 1 + find_min_swap(lenn, list_num, i, pivot)

        cont_l += 1

    if cont_l == len(left) and len(left) != len(list_num):
        final_cont += find_min_swap(lenn, left, -1, 0)

    return final_cont
