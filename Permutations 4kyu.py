from itertools import permutations as permutation

def permutations(string):
    join = lambda x: [''.join(el) for el in x]
    return set(join(permutation(list(string))))

print(sorted(permutations('gynq')))
