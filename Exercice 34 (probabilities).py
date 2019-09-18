# 1. 1/6

# 2.
from random import randint


def experimental1(n):
    summary = 0
    for i in range(n):
        summary += randint(1, 6)
    return summary


# tests
tries = 5
print("Pour " + str(tries) + " lancers, on obtient " + str(experimental1(tries)))


# 3.
def experimental2(n):
    result_is_one = 0
    for i in range(n):
        if randint(1, 6) == 1:
            result_is_one += 1

    return result_is_one


# tests
tries = 5
print("Pour " + str(tries) + " lancers, 1 apparaît " + str(experimental2(tries)) + " fois")

# 4
attempts = [10, 123, 5376, 123456, (10 ** 9)]
for i in attempts:
    print("Pour " + str(i) + " lancers, 1 apparaît " + str(experimental2(i)) + " fois")

# on constate que les résultats sont presque proportionnels
