with open('panda.inp','r') as fin:
    a=int(fin.readline())
if a>0:
    with open('panda.out','w') as fout:
        fout.write('P')
else:
    with open('panda.out','w') as fout:
        fout.write('A')