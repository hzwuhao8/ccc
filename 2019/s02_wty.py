import math


def get_res(num):

    def is_prime(num):
        root = math.sqrt(num)
        for i in range(2, int(root + 2)):
            if num % i == 0:
                return False

        return True


    if is_prime(num):
        return [str(num), str(num)]

    i = 1
    while i <= num:
        if (num - i) % 2:
            continue
        if is_prime(num - i) and is_prime(num + i):
            return [str(num - i), str(num + i)]
        i += 1



num_l = []
for i in range(int(input())):
    num_l.append(int(input()))

res_l = []

for i in num_l:
    res_l.append(get_res(i))

for i in res_l:
    print(" ".join(i))
