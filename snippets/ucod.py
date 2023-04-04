# This will be a module - unicode chars por py
# lot of constant few functions (for jm-use)
# https://www.amp-what.com/unicode/search/square

dic = {
    
    'hea1': ('♥', 9829), 'hea2': ('❤', 10084), 'hea3': ('❥', 10085),
    'hea4': ('♡', 9825), 'hea5': ('❤', 10084), 'heart': ('heaN', -1),

    'cir1': ('⚫', 9899), 'cir2': ('●', 9679),'cir3': ('○', 9675),

    'tri1': ('▲', 9650),

    'rec1': (98),

    'ret1': ('↵', 8629), 'ret2': ('⏎', 9166), 'ret3': ('↩', 8617),
    'ret4': ('↵', 8629), 'ret5': ('⏎', 9166), 'return': ('retN', -1),

    'sqr1': ('■', 9633),
    
    }

def help():
    print("prtchars('hea') --> 'hea' first 3 letters")
    
def prtchars(tr=0):
    print()
    try:
        if tr == 0:
            print(dic)
        else:
            for k in dic.keys():
                if tr in k:
                    print(k, ': ', dic[k], '\t- ucode.dic[', k,
                          '][0]', sep="")
    except BaseException as e:
        print(" !! ERROR !!: prtchars atgument must be string")
        print(e)
    finally:
        print()
          

if __name__ == '__main__':
    prtchars()
    prtchars('hea')
    prtchars(8)
    
for i in [9644, 9645, 9601, 9602, 9603, 9620, 9646, 9647]:
    print(i, chr(i), end="  ")
print(); print()
for i in range(9608, 9622):
     print(i, chr(i), end="  ")
print(); print()
print(' -  ' + chr(9644))

##import unicodedata as ud
##print(dir(ud))





##print()
##enter_sygn = '↵'    # chr(8629))
##enter1_sygn = '⏎'   #print(chr(9166))
##w = input('Press "Enter (↵)" to continue...')
##
##tri = '▲'       # 9650
##sqr = '■'       # 9633
##cir = '⬤'       # 11044
