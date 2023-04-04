# codeally py1
# Multiplying until get one-digit number

def mult_till_one(num):
    while num > 9:
        #print(num, end=' - ')
        fst = int(num/10)
        snd = num - fst * 10
        num = fst * snd
    return num

def mto(num):
    str_num = str(num)
    while len(str_num) > 1:
        res = 1
        for d in str_num:
            res *= int(d)
        str_num = str(res)
    return res

for n in [22, 19, 91, 47, 57, 92]:
    print(n, '  f1 -> ', mult_till_one(n), '  f2 -> ', mto(n))

print('-' * 60)

for n in [122, 719, 791, 12947, 13857, 3242]:
    print(n, '  f2 -> ', mto(n))


