import math

P = int(input())
N = int(input())
R = int(input())
total = N
days = 0
current_day = N
if R == 1:
    days = int(P / N)
    # print(days)
    if N * (days + 1) < P:
        days = days + 1
else:
    days = math.log((R - 1) * P / N + 1) / math.log(R) - 1
    # days = 1
    days = int(days)
    total = N * (math.pow(R, days + 1) - 1) / (R - 1)
    while total <= P:
        days = days + 1
        total = N * (math.pow(R, days + 1) - 1) / (R - 1)
        # print(days, total)

print(days)
