def main():
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())

    b1 = int(input())
    b2 = int(input())
    b3 = int(input())

    score_A = a1 * 3 + a2 * 2 + a3 * 1
    score_B = b1 * 3 + b2 * 2 + b3 * 1
    res = ""
    if score_A > score_B:
        res = "A"
    else:
        if score_B > score_A:
            res = "B"
        else:
            res = "T"
    print(res)


main()
