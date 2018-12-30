#
def myprint(x):
    pass
    print(x)


def myinput():
    day = int(input())
    even = int(input())
    weekend = int(input())
    return (day, even, weekend)

def plan_A(day , even , weekend ):
    total = 0
    p1 = 25 * max((day - 100),0)
    p2 = 15 * even
    p3 = 20 * weekend
    total = p1 + p2 + p3
    return total

def plan_B(day,even,weekend):
    total = 0
    p1 = 45 * max((day - 250), 0)
    p2 = 35 * even
    p3 = 25 * weekend
    total = p1 + p2 + p3
    return total


def main():
    (day, even, weekend) = myinput()
    t1 = plan_A(day, even, weekend)
    t2 = plan_B(day, even, weekend)
    print(f"Plan A costs {t1/100}")
    print(f"Plan B costs {t2/100}")
    if t1 > t2 :
        res = f"Plan B is cheapest."
    elif t1 < t2 :
        res = f"Plan A is cheapest."
    else:
        res = "Plan A and B are the same price."
    print(res)


assert plan_A( 251,10,60) == 5125, f"plan_A( 251,10,60)= {plan_A( 251,10,60)}"
assert plan_B( 251,10,60) == 1895, f"plan_A( 251,10,60)= {plan_B( 251,10,60)}"

main()
