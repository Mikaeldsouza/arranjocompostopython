import math
import random

def total_possibilities(n,p):
  return n**p


def possibilities(obj,positions):
    total = total_possibilities(len(obj),positions)
    result_list = []

    while True:
        nw_base = []
        for i in range(positions):
            nw_base.append(random.choice(obj))

        if nw_base not in result_list:
            result_list.append(nw_base)

        if len(result_list) == total:
            break
    return result_list
    

def main():
    p  = possibilities([0,1,2], 3)
    for i in p:
        print(i)
    print(f"TOTAL: {len(p)}")


main()
