import itertools as i
import math as m
import time

'''
func = [["(", ""],
        ["ptorial(", "p!"],
        ["dptorial(", "p!!"],
        ["dstorial(", "s!!"],
        ["storial(", "s!"]]
'''

# Factorial = ftorial()
# Double factorial = dftorial
# Double plustorial = dptorial
# Double subtorial = dstorial
# Square root = m.sqrt()
# Plustorial = ptorial()
# Subtorial = storial()
# Binary Logarithm = m.log2()

def isint(n):
    if n%1 == 0:
        return True
    return False

def ftorial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+1, 0, 1):
            sum *= x
    else:
        for x in range(n-1, 0, -1):
            sum *= x
    return sum

def ptorial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+1, 0, 1):
            sum += x
    else:
        for x in range(n-1, 0, -1):
            sum += x
    return sum

def storial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+1, 0, 1):
            sum -= x
    else:
        for x in range(n-1, 0, -1):
            sum -= x
    return sum

def dftorial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+2, 0, 2):
            sum *= x
    else:
        for x in range(n-2, 0, -2):
            sum *= x
    return sum

def dptorial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+2, 0, 2):
            sum += x
    else:
        for x in range(n-2, 0, -2):
            sum += x
    return sum

def dstorial(n):
    if not isint(n):
        return None
    sum = n
    if n <= 0:
        for x in range(n+2, 0, 2):
            sum -= x
    else:
        for x in range(n-2, 0, -2):
            sum -= x
    return sum

def evaluate(numbers, target):
    operations = ["+", "-", "/", "*"]
    opas = ["+", "-"]
    opmd = ["/", "*"]

    fout = open("snj.txt", "w")

    for x in range(len(numbers)):
        n = numbers[x]
        numbers[x] = {
                    str(n):n,
                    "{}!".format(n):ftorial(n),
                    "{}p!".format(n):ptorial(n),
                    "{}s!".format(n):storial(n),
                    "{}p!p!".format(n):ptorial(ptorial(n)),
                    "{}s!s!".format(n):storial(storial(n)),
                    "{}p!s!".format(n):storial(ptorial(n)),
                    "{}s!p!".format(n):ptorial(storial(n)),
                    "{}!!".format(n):dftorial(n),
                    "{}p!!".format(n):dptorial(n),
                    "{}s!!".format(n):dstorial(n)
                    }
        if isint(m.sqrt(n)):
            numbers[x][str(n) + "sqrt"] = m.sqrt(n)
        if n == 4 or n == 2 or n == 8:
            numbers[x][str(n) + "blog"] = int(m.log2(n))
        for y in list(numbers[x].items())[::-1]:
            if list(numbers[x].values()).count(y[1]) > 1:
                del numbers[x][y[0]]

    for x in numbers:
        fout.write(str(x) + "\n")

    fout.write("\n")

    sets = list(i.product(numbers[0].items(), numbers[1].items(), numbers[2].items(), numbers[3].items(), numbers[4].items()))
    np = list(i.product(operations, repeat=4))
    op = list(i.product(opas, opmd, opas, operations))
    # fp = list(i.product(func, func))

    counter = 0
    start = time.time()

    # n1 op n2 op n3 op n4 op n5
    for x in sets:
        for y in np:
            try:
                counter += 1
                if eval("{}{}{}{}{}{}{}{}{}".format(
                        x[0][1],
                        y[0],
                        x[1][1],
                        y[1],
                        x[2][1],
                        y[2],
                        x[3][1],
                        y[3],
                        x[4][1])) == target:
                    fout.write(f'{x[0][0]}{y[0]}{x[1][0]}{y[1]}{x[2][0]}{y[2]}{x[3][0]}{y[3]}{x[4][0]}\n')
                    break
            except ZeroDivisionError:
                continue
        if time.time()-start > 30:
            fout.write(f'Timed out. Ran a total of {counter} calculations in {round(time.time()-start,5)}s')
            fout.close()
            return 0
    # (n1 op n2) op (n3 op n4) op n5
    for x in sets:
        for y in op:
            #for z in fp:
            counter += 1
            try:
                if eval("({}{}{}){}({}{}{}){}{}".format(
                        x[0][1],
                        y[0],
                        x[1][1],
                        y[1],
                        x[2][1],
                        y[2],
                        x[3][1],
                        y[3],
                        x[4][1])) == target:
                    fout.write(f'({x[0][0]}{y[0]}{x[1][0]}){y[1]}({x[2][0]}{y[2]}{x[3][0]}){y[3]}{x[4][0]}\n')
                    # fout.write(f'({x[0][0]}{y[0]}{x[1][0]}){z[0][1]}{y[1]}({x[2][0]}{y[2]}{x[3][0]}){z[1][1]}{y[3]}{x[4][0]}\n')
                    break
                '''
                if eval("{}({}{}{})){}{}({}{}{})){}{}".format(
                        z[0][0],
                        x[0][1],
                        y[0],
                        x[1][1],
                        y[1],
                        z[1][0],
                        x[2][1],
                        y[2],
                        x[3][1],
                        y[3],
                        x[4][1])) == target:
                    fout.write(f'({x[0][0]}{y[0]}{x[1][0]}){z[0][1]}{y[1]}({x[2][0]}{y[2]}{x[3][0]}){z[1][1]}{y[3]}{x[4][0]}\n')
                    break
                '''
            except:
                continue
        if time.time()-start > 30:
            fout.write(f'Timed out. Ran a total of {counter} calculations in {round(time.time()-start,5)}s')
            fout.close()
            return 0
    # (n1 op n2 op n3) op n4 op n5
    for x in sets:
        for y in op:
            # for z in fp:
            counter += 1
            try:
                if eval("({}{}{}){}({}{}{}{}{})".format(
                    x[0][1],
                    y[0],
                    x[1][1],
                    y[1],
                    x[2][1],
                    y[2],
                    x[3][1],
                    y[3],
                    x[4][1])) == target:
                        fout.write(f'({x[0][0]}{y[0]}{x[1][0]}){y[1]}({x[2][0]}{y[2]}{x[3][0]}{y[3]}{x[4][0]})\n')
                        '''
                        if eval("{}({}{}{})){}{}({}{}{}{}{}))".format(
                        z[0][0],
                        x[0][1],
                        y[0],
                        x[1][1],
                        y[1],
                        z[1][0],
                        x[2][1],
                        y[2],
                        x[3][1],
                        y[3],
                        x[4][1])) == target:
                            # fout.write(f'({x[0][0]}{y[0]}{x[1][0]}){z[0][1]}{y[1]}({x[2][0]}{y[2]}{x[3][0]}{y[3]}{x[4][0]}){z[1][1]}\n')
                        '''
                        break
            except:
                continue
        if time.time()-start > 30:
            fout.write(f'Timed out. Ran a total of {counter} calculations in {round(time.time()-start,5)}s')
            fout.close()
            return 0

    fout.write(f'Ran a total of {counter} calculations in {round(time.time()-start,5)}s')
    fout.close()