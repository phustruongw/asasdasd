with open('TIMTU.INP','r') as fin:
    s=fin.read().split()
lenmax=max(len(tu) for tu in s)
tumax=[tu for tu in s if len(tu)==lenmax]
with open('TIMTU.OUT','w') as fout:
    fout.write(str(tumax[-1].upper()))