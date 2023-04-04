#
import time as tim


try:
    lfn = [
        '../Projects/letter_histogram/big2.uni',
        '../Projects/letter_histogram/El_martir_de_las_catacumbas.txt',
        '../Projects/letter_histogram/big1.txt',
        '../Projects/letter_histogram/El_jardin_del_amado.txt',
        '../Projects/letter_histogram/Los_aztecas.txt',
        '../Projects/letter_histogram/z2.txt',
        '../Projects/letter_histogram/zen_py.txt',
        '../Projects/letter_histogram/z1.txt',
        ]

    lfh = []                    # list files handles               
    for i in range(len(lfn)):
        lfh.append(open(lfn[i], 'r', encoding='utf-8', errors='ignore'))
        #lfh.append(open(lfn[i], 'r', errors='ignore'))

    lfslns = []                  # list files lines _ of all files 2Dlist
    for fh in lfh:
        lfslns.append(fh.readlines())

    i = 0
    for flns in lfslns:
        print('lfh[{}]: \n{}'.format(i, lfh[i]))
        print(flns)        
        tim.sleep(1)
        i += 1
        print(i)

    r = input('Press return to continue...')
    for fh in lfh:
        fh.close()
        print(fh, '.closed()')
    tim.sleep(4)

except LookupError as e:
    print(e)

except KeyboardInterrupt as e:
    print(e)
    
    
        
# -. lfh.append(open(lfn[i], 'r'))
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 728:
#character maps to <undefined>

# -. lfh.append(open(lfn[i], 'r', encoding='utf-8'))
##UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 2363:
##invalid start byte

#-- errors='ignore', solve the situacion
# https://github.com/minimaxir/textgenrnn/issues/8
# https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
        
        
   
