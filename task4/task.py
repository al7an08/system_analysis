from collections import defaultdict
from functools import reduce
from math import log2


def calculate_counts():
    cnts_ab, cnts_a, cnts_b = defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(1, 7):
        for j in range(1, 7):
            sum_val, prod_val = i + j, i * j
            cnts_ab[(sum_val, prod_val)] += 1 
            cnts_a[sum_val] += 1
            cnts_b[prod_val] += 1
    return cnts_ab, cnts_a, cnts_b


def calculate_probabilty(mass: defaultdict) -> dict:
    return {key: (value / 36) for key, value in mass.items()}

def round_values(entropies: [float]) -> [float]:
    return [round(e, 2) for e in entropies]

def calculate_entropy(mass: dict) -> float:
    return reduce(lambda e, prob: e - prob * log2(prob), mass.values(), 0)



def main() -> list:
    cnts_ab, cnts_a, cnts_b = calculate_counts()
    prob_ab = calculate_probabilty(cnts_ab)
    prob_a = calculate_probabilty(cnts_a)
    prob_b = calculate_probabilty(cnts_b)

    entropy_ab = calculate_entropy(prob_ab)
    entropy_a = calculate_entropy(prob_a)
    entropy_b = calculate_entropy(prob_b)

    entropy_b_given_a = entropy_ab - entropy_a
    information_a_about_b = entropy_b - entropy_b_given_a

    return round_values([entropy_ab, entropy_a, entropy_b, entropy_b_given_a, information_a_about_b])


print(main())