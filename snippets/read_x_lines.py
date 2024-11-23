# Read x lines looping over the file object

x = 20
with open('sshd.cnf', 'r', encoding='utf-8') as f:
    for i, ln in enumerate(f):
        print(i, '->', ln, end='')      # e/line contains an EOL
        if i == x:
            break