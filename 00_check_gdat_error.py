import glob
inp = glob.glob(r'.\*g.dat')
out = open(r'.\00_error.dat','w')
for i in inp :
    sta = open(i)
    line = sta.readlines()
    out.write(f'{i}\n')
    

    out1 = open(f'.\\remove_error_gdat\\{i[2:17]}','w')

    
    for j in line :
        lines = j.split()
        if len(lines) < 3:
            if len(lines[0].split('-')) == 2:
                out.write(f'{j}')
                a = lines[0].split('-')[0]
                b = lines[0].split('-')[1]
                c = lines[1]

                out1.write(f'{a}  -{b}  {c}\n')
            else:
                out.write(f'####### manually remove! #######\n')
                out.write(f'{j}')
        else:
            out1.write(f'{j}')    
    out1.close()

sta.close()
out.close()