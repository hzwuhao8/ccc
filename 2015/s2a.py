def my_main():
    J = int(input())
    A = int(input())
    data = [""]
    for i in range(J):
        t = input()
        data.append(t)

    total = 0
    for i in range(A):
        a, b = input().split()
        index = int(b)
        if 'L' == a:
            if (data[index]) == a:
                total += 1
                data[index] = ""
                # print((a,b))
        elif 'M' == a:
            if data[index] == a or data[index] == 'L':
                total += 1
                data[index] = ""
        elif 'S' == a:
            if data[index] != "":
                total += 1
                data[index] = ""
    print(total)


my_main()
