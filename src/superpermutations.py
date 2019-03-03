import itertools
import math
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <string>".format(sys.argv[0]))
        exit(1)
    k = sys.argv[1]
    elems = list("".join(x) for x in itertools.permutations(k))
    check = elems.copy()
    print("Permutations: ", ", ".join(elems))
    msg = elems[0]
    elems.remove(msg)
    print("{}\t(add {})".format(msg, msg))
    while elems:
        found = False
        for try_len in range(len(k) - 1, 0, -1):
            if not found:
                seek = msg[-try_len:]
                for e in elems:
                    if e.startswith(seek):
                        add = e[try_len:]
                        msg += add
                        elems.remove(e)
                        print("{}\t(add {})".format(add, e))
                        found = True
                        break
    # Double-check all items are found in string
    for x in check:
        if x not in msg:
            print("Error: {} not found", x)
    a = len(k)
    print(msg)
    print("length=", len(msg))
    print("a + a! -1=", (a + math.factorial(a) - 1))
