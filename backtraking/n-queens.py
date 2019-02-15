
def check_attack(queens_candidate):
    queens_size = len(queens_candidate)
    queen_candidate = queens_candidate[-1]
    candidate_index = queens_size - 1

    if queens_size <= 1:
        return True

    for i in range(0, candidate_index):
        if abs(i - candidate_index) == abs(queens_candidate[i] - queen_candidate):
            return False

    return True


def n_queens(chess_size, queens=None):
    if not queens:
        queens = []
    if len(queens) == chess_size:
        return queens

    for i in range(0, chess_size):
        candidate = queens + [i]
        if i not in queens and check_attack(candidate):
            result = n_queens(chess_size, candidate)
            if result:
                print(result)
                return

    return False
