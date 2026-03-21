from itertools import permutations

letters = ('T','W','O','F','U','R')
digits = range(10)

print("\n========== CRYPTARITHMETIC PROBLEM ==========\n")
print("          TWO")
print("        + TWO")
print("        --------")
print("          FOUR\n")

for perm in permutations(digits, len(letters)):

    mapping = dict(zip(letters, perm))

    # Leading letters cannot be zero
    if mapping['T'] == 0 or mapping['F'] == 0:
        continue

    two = mapping['T']*100 + mapping['W']*10 + mapping['O']
    four = mapping['F']*1000 + mapping['O']*100 + mapping['U']*10 + mapping['R']

    if two + two == four:

        print("Solution Found")
        print("====================================")

        for k,v in mapping.items():
            print(f"{k} = {v}")

        print("\nComputed Values")
        print("------------------------------------")
        print("TWO  =", two)
        print("FOUR =", four)

        print("\nVerification")
        print("------------------------------------")
        print(f"{two} + {two} = {four}")

        print("\n====================================")

        break