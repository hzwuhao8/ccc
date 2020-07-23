s = input()
t = input()

flag = True
for i in range(len(t)):
    tmp_t = t[i:] + t[0:i]
    # print(tmp_t)
    if s.find(tmp_t) > -1:
        flag = False
        break
if flag:
    print("no")
else:
    print("yes")
