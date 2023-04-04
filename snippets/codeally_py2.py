# codeally py2
# Convert binary number to decimal number

def bin_to_dec(bin_num):
    weight, dec_num = len(bin_num) - 1 , 0
    for bit in bin_num:
        dec_num += int(bit) * 2 ** weight
        weight -= 1
    return dec_num

for bn in ['110', '110000011', '111001', '111100', '001101100010111010110000']:
    print(bn, ' -> ', bin_to_dec(bn))

