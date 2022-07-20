import glob

gdat = glob.glob(r'./inp/*g.dat')

for i in gdat : 
    inp = open(i)
    sta = i[6:21] #ts_????_?_g.dat
    lines = inp.readlines()

    #cal average
    total = 0
    for j, line in enumerate(lines): 
        time, pos, err = line.split()
        time = float(time)
        pos = float(pos)
        err = float(err)
        if time >= 2012:
            total = total + pos
    average = total / len(lines)

    #cut time
    out = open(f'./out/{sta}','w')            
    for k, line in enumerate(lines):
        time, pos, err = line.split()
        time = float(time)
        pos = float(pos)
        err = float(err)
        if time >= 2012:
            pos_out = pos - average
            out.write(f'{time:10.5f}   {pos_out:7.2f}    {err:7.2f}\n')

    
     


