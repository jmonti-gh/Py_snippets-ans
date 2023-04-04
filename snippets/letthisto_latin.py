# TO-DO:
  # Review all mesagges to users -- all!
# accept big files -.readlines(buffer) <- 1sr objective --> DONE
      # - buffer is in bytes _ compute buff function of RAM - psutil mod _later
  # format 1st presentation -prsntn() - f-strigs, w/more? <- this version?
  # V-graph alpha orderr , and letters fill sym ¿?, when¿?
  # guess (try to discover) Alphabet, funct of % letters frecuency
      # posible later, have to load tables several idioms.
  # ... others and old notes, view: letthisto_latin_2.py

# New TO-DO.. add Total Nbrs of Ocurrencies.. to the graphs..

# https://stackoverflow.com/questions/4518641/how-to-round-a-floating-point-number-up-to-a-certain-decimal-place
# http://openbookproject.net/pybiblio/practice/wilson/loan.php


import ucod         # own mod to manage unicode symbols

# only make funct in case to use the code more than once

def presentation(dic, sort_label):                 # presention(dict, string)
    ''' Shows alpha(dl{}) or num(dlvo{}) results and percentage of relative
    frecuency (dp{}). main entities i'll use:
            dp{} -> letter:percent dic
            to -> total ocurrancies all letters (100%) 
            psum -> sum(all_percent) == 100.0 '''
    print()
    print('-. Letter frecuency analysis of', fn, ':')
    print('-' * 68)
    print('--', sort_label, 'sort --')
    print()
    llt, ltm, lfr = 'Letter', 'Times', 'Relative Frecuency'     # labels
    s, tot, z = '-', 'Total', ' '
    print(f'  {llt:<8} {ltm:<8} {lfr:<9}')
    print(f'  {(s * len(llt)):<8} {(s * len(ltm)):<8} {(s * len(lfr)):<9} ')
    for k, v in dic.items():
        print(f' {k:^8} {dic[k]:>6} {dp[k]:12.2f} ')
    print(f'  {(s * len(llt)):<8} {(s * len(ltm)):<8} {(s * len(lfr)):<9} ')
    print(f'  {tot:^8} {to:>5} {psum:12.2f}')


def h_drw(p='-', sort='a'):       # draw horizontal histo graph
    ''' main entities i'll use:
            dl -> letter:count dic
            lvrs -> list value reverse sorted
            dlvo -> letters:count dic reverse sorted (max-min) by values '''
    # compute div value to make prop lines in no small counts
    div = (lvrs[0] // 60 + 1)

    if sort == 'a':
        dic = dl
        tit = '-. Horizontal latin-letters histogram alphabeticaly sorted:'
    else:
        dic = dlvo
        tit = '-. Horizontal latin-letters histogram numericaly sorted:'

    print('\n' + tit + '\n', '-' * (len(tit) + 2), '\n')
    for k in dic:
        if p == 'key' or len(p) > 1:
            #print(k, k * (dic[k] // div), dic[k], '/', dp[k], '%')
            print(f'{k} {k * (dic[k]//div)} {dic[k]} / {dp[k]:3.2f} %')
        else:
            #print(k, p * (dic[k] // div), dic[k], '/', dp[k], '%')
            print(f'{k} {p * (dic[k]//div)} {dic[k]}/{dp[k]:3.2f}%')
    print()

    
def vn_drw(p='*'):       # draw vertical histo graph rev-num sorted
    ''' main entities i'll use:
            dl -> letter:count dic
            lvrs -> list value reverse sorted
            dlvo -> letters:count dic reverse sorted (max-min) by values '''
    # compute div value to make prop lines in no small counts
    t = 30                      # tower - max visible hight
    div = (lvrs[0] // t + 1)
    
    tit = '-. Vertical latin-letters histogram numericaly sorted:'
        
    # mk v-graph w/ title
    print('\n' + tit + '\n', '-' * (len(tit) + 1))
    hm = lvrs[0] // div             # max. height
    for h in range(hm +1, 0, -1):
        f = 'i'                     # initial
        #for k, v in dlvo.items():
        for v in dlvo.values():
            v = v // div
            if v >= h:
                if f == 'i':        # write inital line chars
                    ylab = str(round(h*100/hm, 1))
                    if ylab == '100.0': ylab = '100.'
                    if len(ylab) < 4:
                        ylab = ' '+ ylab
                    print(' ', ylab, ' |', end=" ")
                    f = 'c'         # cont
                print(p, end=" ")              # write next values
        print()
    print(" " * 7, "-" * (len(dlvo) * 2))    # bottom h-line

    # print x-label (letters)
    f = 'i'    # initial
    for k in dlvo.keys():
        if f == 'i':
            print(" " * 8, k, end=" ")
            f = 'c' # cont
        else:
             print(k, end=" ")
    print()

    # print x-label (all digits)
    qdm = len(str(lvrs[0]))   # quant digs max, cause lvrs[0] is the gratest
    for i in range(qdm):
        f = 'i'    # initial
        for v in dlvo.values():
            vtrin = str(v)
            dgs = qdm - len(vtrin)      # diff digits b/max (qdm) an actual
            vtrin = vtrin + ' ' * dgs   # now all same qdigs
            if f == 'i':
                print(" " * 8, vtrin[i], end=" ")
                f = 'c' # cont
            else:
                print(vtrin[i], end=" ")
        print()


def vA_drw(p='*'):       # draw vertical histo graph Alpha sorted
    ''' main entities i'll use:
            dl -> letter:count dic
            lvrs -> list value reverse sorted '''
    # compute div value to make prop lines in no small counts
    t = 30                      # tower - max visible hight
    div = (lvrs[0] // t + 1)    # to make a proportional scale
    
    tit = '-. Vertical latin-letters histogram Alpha sorted:'
        
    # mk v-graph w/ title
    print('\n' + tit + '\n', '-' * (len(tit) + 1))
    print()

    # print graph from top to bottom - frw 1st line, then secon.. an so on
    # The pint here is de x position
    
    hm = lvrs[0] // div             # max. height
    f2, cld = True, 1               # f2: write var%, cld: count lett to-drw
    for h in range(hm, 0, -1):
        f = 'i'                 # initial - 1st chars of the lines
        for v in dl.values():
            v = v // div
            if f == 'i':
                #lvrs = list value reverse sorted
                # i will need here: list letters value rev-sorted
                # better mk it in same place mk dlvo (or lvrs?), to see

                #but first freo var% wen a new point is writen
                if f2:
                    ptg = 'var%'
                    f2 = False
                else:
                    ptg = '    '
                print(' ', ptg, ' |', end=" ")
                f = 'c'         # cont w/ other p in the same line
            if v >= h:
                print(p, end=" ")
            else:
                print(' ', end=" ")
        print()

    print(" " * 7, "-" * (len(dl) * 2))    # bottom h-line
                
            
##    for h in range(hm +1, 0, -1):   # (hm+1) to 0, 
##        f = 'i'                     # initial - 1st chars of the lines
##        for v in dl.values():
##            v = v // div
##            if v >= h:
##                if f == 'i':        # write inital line chars
##                    ylab = str(round(h*100/hm, 1))
##                    if ylab == '100.0': ylab = '100.'
##                    if len(ylab) < 4:
##                        ylab = ' '+ ylab
##                    print(' ', ylab, ' |', end=" ")
##                    f = 'c'         # cont
##                print(p, end=" ")              # write next values
##            else:
##                print(' ', end=" ")             # write next values
##        print()
##    print(" " * 7, "-" * (len(dl) * 2))    # bottom h-line

    # print x-label (letters)
    f = 'i'    # initial
    for k in dl.keys():
        if f == 'i':
            print(" " * 8, k, end=" ")
            f = 'c' # cont
        else:
             print(k, end=" ")
    print()

    # print x-label (all digits)
    qdm = len(str(lvrs[0]))   # quant digs max, cause lvrs[0] is the gratest
    for i in range(qdm):
        f = 'i'    # initial
        for v in dl.values():
            vtrin = str(v)
            dgs = qdm - len(vtrin)      # diff digits b/max (qdm) an actual
            vtrin = vtrin + ' ' * dgs   # now all same qdigs
            if f == 'i':
                print(" " * 8, vtrin[i], end=" ")
                f = 'c' # cont
            else:
                print(vtrin[i], end=" ")
        print()



### -------- main -------------------------------------------------------
    
try:
    dl = {chr(i): 0 for i in range(97, 123)} # letter:count dic was born w/v=0

    # Open text file conteinig the text w/letter to count
    fn = 'z2.txt'
    #fh = open('z1.txt', 'r', encoding='utf-8')
    #fh = open('zen_py.txt', 'r', encoding='utf-8')
    #fh = open(fn, 'r', encoding='utf-8')
    fh = open(fn, 'r')

    # count letters --fill--> dl.values
    buffer = 2 ** 20
    lst_lns = fh.readlines(buffer)    # list_lines
    while lst_lns:
        for ln in lst_lns:          
            for k in dl.keys():     
                c = ln.lower().count(k)     # count 'k'lower_letter_ver  in ln
                dl[k] += c                  # acumulate values in dl.keys
        lst_lns = fh.readlines(buffer)
    #print(dl)

    # mk a list containing reverse sorted values of dl -use later
    lvrs = []                   # list value reverse sorted born
    for k in dl.keys():
        lvrs.append(dl[k])
        lvrs.sort(reverse=True) # Max to min -> lvrs[0] gratest val

    # mk new letters:count dic reverse sorted (max-min) by values -use lvrs
    dlvo = {}                       # dic letter values ordered
    for val in lvrs:
        for k,v in dl.items():
            if v == val:
                dlvo.update({k: v}) # same keys, other order
    #print(dlvo)
    ''' dlvo escentialy has the same content as dl but they have diff sort,
    dl is key_alpha_sort and dlvo es value_revers_sort -always keys are
    latin alphabet letters '''

    # Compute Relative frecuencies of letters in file readed

    to = sum(lvrs)         # total ocurrencies equiv 100% = Sum
    to2 = sum(dl.values())

    # test
    if to != to2:
        raise ArithmeticError   # here make my own exception

    ''' i can mk new dic w/% or make a tuple of values in the same dic, will
        choose the first for simplicity in reading and not to have to rewrite '''
        
    dp = {}                 # dict of percentages {letter: relative_percentage}
    for k, v in dl.items():
        dp[k] = v / to * 100
    
    # test: sum of dp.values must be 100
    psum = sum(dp.values())
    if not (psum > 99.9999 and psum < 100.0003):
        raise ArithmeticError   # here make my own exception

    ## First presentation, alpha_sort: letter, times, relative frecuency
    presentation(dl, 'Alphabetical')
    
    # Pause..
    print("\nPress 'Return (", ucod.dic['ret1'][0], ")' to continue"
          " with Numerical Order: ")
    i = input()

    ## Sec presentation, num_sort: letter, times, relative frec
    presentation(dlvo, 'Numerical')
    
    
## ask user which vA_draw want  -- DRY - funct..?
    print()
    a = input("Do you want to see Vertical graph (y - n)? ").lower()
    while a != 'n':         # defualt yes: while not expressed 'n' DO-IT
        
        print()
        sym = input("Enter the symbol you want to fill (e.g '*' '_') -"
                "'key' for letters:  ")
        if len(sym) > 1: sym = sym[0]
        elif len(sym) == 0: sym = '*'
        
        vA_drw(p=sym)  # call funct that make the work

        a = input("\nDo you want to try another V-graph (y - n)? ").lower()


#### ask user which h_draw want
##    print()
##    a = input("Do you want to see Horizontal graph (y - n)? ").lower()
##    while a == 'y':
##        
##        print()
##        sym = input("Enter the symbol you want for filling (e.g '*' '_') -"
##                "'key' for letters:  ")
##        if len(sym) > 1 and sym != 'key': sym = sym[0]
##        elif len(sym) == 0: sym = '*'
##            
##        srt = input("Alphabetical or Numerical order? (a or n): ").lower()
##
##        h_drw(p=sym, sort=srt)  # call funct that make the work
##
##        a = input("Do you want to try another H-graph (y - n)? ").lower()
##
#### ask user which vn_draw want  -- DRY - funct..?
##    print()
##    a = input("Do you want to see Vertical graph (y - n)? ").lower()
##    while a == 'y':
##        
##        print()
##        sym = input("Enter the symbol you want to fill (e.g '*' '_') -"
##                "'key' for letters:  ")
##        if len(sym) > 1: sym = sym[0]
##        elif len(sym) == 0: sym = '*'
##        
##        vn_drw(p=sym)  # call funct that make the work
##
##        a = input("\nDo you want to try another V-graph (y - n)? ").lower()
    
    

except FileNotFoundError as e:
    print(e)
    
