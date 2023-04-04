
##import this
import sys
import errno
import os

de = {i: (errno.errorcode[i], os.strerror(i)) for i in sorted(errno.errorcode)}

try:
    cnt = 0
    ag = 78
    print()
    for ln in open('zen_py.txt', 'r', encoding='utf-8'):
        cnt += 1
        
        if cnt <= 2:
            sys.stderr.write(ln.rjust(ag))
        else:
            print(ln.rjust(ag), end="")
    print()
except OSError as e:
    print(e)        # py3.11 has an extremely complete error information
    print(e.errno, de[e.errno])
except Exception as e:
    print(e)
except:
    print('Siamo Fouri')
    
print()
enter_sygn = '↵'    # chr(8629))
enter1_sygn = '⏎'   #print(chr(9166))
w = input('Press "Enter (↵)" to continue...')

try:
    cnt = 0
    ag = 76
    print()
    for ln in open('zen_py.txt', 'r', encoding='utf-8'):
        cnt += 1
        if ln.endswith('\n'):
            ln = ln.replace('\n', "")
        if cnt <= 2:
            sys.stderr.write(ln.center(ag)); print()
        else:
            print(ln.center(ag))
    print()
except OSError as e:
    print(e)        # py3.11 show extremely complete error information
    print(e.errno, de[e.errno])
except Exception as e:
    print(e)
except:
    print('Siamo Fouri')
            
##    zf = open('casa.txt', 'r')
##    ln = zf.readline()
##    print(ln)
##    for ln in zf.readline():
##        print(ln)
##        cnt += 1
##        if cnt <= 2:
##            sys.stderr.write(ln.rjust(76))
##        else:
##            print(ln.rjust(76)) 
  
    

###print(dir(this))
##
####for el in dir(this):
####    print(el)
##
##print(); print()
##print(this.__name__)
##print(this.__package__)
####print(this.__builtins__)
##print(this.c)
##print(this.d)
##print(this.i)
####print(this.s)

##t1 = 'a house\n'
##t2 = '7\n'
##t3 = 'a small great house\n'
##t4 = 'bigger house\n'
##for tx  in (t1, t2, t3, t4):
##    if tx.endswith("\n") == True:
####        txl = list(tx)
######        print(txl)
######        print(txl.pop(-1))
######        print(txl)
####        txl.pop(-1)
####        tx = "".join(txl)
####        print(tx)
##        tx = tx.replace('\n', "")
##    print(tx.center(50))
##stop

          

