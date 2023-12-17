from itertools import product

def unique_combinations(*sequences):
    for combination in product(*sequences):
        if len(set(combination)) == len(combination):
            yield combination

# Пример использования:
seq1 = [1, 2]
seq2 = ['a', 'b']
seq3 = [True, False]

for combination in unique_combinations(seq1, seq2, seq3):
    print(combination)