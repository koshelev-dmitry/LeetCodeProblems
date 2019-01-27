def smallest_v(A):
    max_val = 1
    for a in A:
        if a > max_val:
            return max_val
        max_val += a
    return max_val

def all_sums(A):
    result = []
    for i in range(len(A)):
        for j in range(i, len(A)+1):
            result.append(sum(A[i:j+1]))
    return set(result)

def all_sums(A):
    result = [A[i]+A[j] for i in range(len(A)) for j in range(len(A)) if i != j]


    num_set = set(result)
    max_constr_number = 1
    while max_constr_number in num_set:
        max_constr_number += 1
    print(num_set)
    return max_constr_number

print(all_sums([1,1,1,1,1,5,10]))