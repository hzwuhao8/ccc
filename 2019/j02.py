def main():
    lines = int(input())
    x = 1
    res = []
    while x <= lines:
        str1 = input()
        str2 = str1.strip().split(" ")
        count = int(str2[0])
        ch = str2[1]
        res1 = ch * count
        res.append(res1)
        x = x + 1
    for x in res:
        print(x)



main()

