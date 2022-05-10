def LIS(array_of_numbers):
    L = [1] * len(array_of_numbers)
    for i in range(1, len(array_of_numbers)):
        subproblems = [L[k] for k in range(i) if array_of_numbers[k] < array_of_numbers[i]]
        L[i] = 1 + max(subproblems, default = 0)
    return max(L)
