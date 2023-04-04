dividend = 14
divisor = 4
division = dividend / divisor
print('14 / 4 =', division, type(division))
int_div = dividend // divisor
print('14 // 4 =', int_div, type(int_div))
mod = dividend % divisor
print('14 % 4 =', mod, type(mod))
result = dividend // divisor * divisor + dividend % divisor
print('14 // 4 * 4 + 14 % 4 =', result, type(result))
# add lists
a = [1, 2, 3]
b = [ 6, 7, 8]
c = b + a
print(c)