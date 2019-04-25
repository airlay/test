def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)



# reversed staircase

def reversed_staircasesR(steps):
    # 1 step, 2 steps and 3 steps allowed to climb the stairs
    # base cases
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    if steps == 1:
        return 1
    if steps == 2:
        return 1
    # if steps == 3:
    #     return 1
    # recursived case
    else:
        return reversed_staircasesR(steps - 1) + reversed_staircasesR(steps - 2)  # + reversed_staircasesR(steps - 3)


def reversed_staircaseDP(steps):
    # 1 step, 2 steps and 3 steps allowed to climb the stairs
    # base cases
    # result[3] = 1

    if steps < 0:
        return 0
    if steps == 0:
        return 1
    if steps == 1:
        return 1
    if steps == 2:
        return 1
    # if steps == 3:
    #     return 1
    # recursive case

    result = [None] * (steps+1)
    result[0] = 1  # zero step, remain there...ans: 1
    result[1] = 1
    result[2] = 1

    for i in range(3, steps+1):
        result[i] = result[i-1] + result[i-2]

    return result[steps]

from MyTimer import MTimer

l = 40
for i in range(800):
    with MTimer() as t:
        m = reversed_staircaseDP(i)
    print('it took {} ms to execute fibonnaci({}) = {}'.format(round(t.interval, 3) * 1000, i, m))


