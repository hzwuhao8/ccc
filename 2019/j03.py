def main():
    lines = int(input())
    x = 1
    res = []
    while x <= lines:
        line = input()
        count = 0
        current = " "
        res1 = ""
        for c in line:
            if current == " ":
                count = 1
                current = c
            else:
                if c == current:
                    count = count + 1
                else:
                    res1 = res1 + str(count) + " " + current+ " "
                    count = 1
                    current = c
        res1 = res1 + str(count) + " " + current + " "
        res.append(res1.strip())
        x = x + 1
    print()
    for str2 in res:
        print(str2)


main()
