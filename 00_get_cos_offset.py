inp = open(r'.\fit_r.out')
hout = open(r'.\00_cosh.dat','w')
vout = open(r'.\00_cosv.dat','w')

lines = inp.readlines()

for i, line in enumerate(lines) :

    if '#' in line :
        print(line[2:6])
    
        if lines[i+5][2] == '!':
            print(f'{lines[i+7].split()[2]} {lines[i+7].split()[4]}')
            ecos = float(lines[i+7].split()[2])
            eerr = float(lines[i+7].split()[4])
            ncos = float(lines[i+8].split()[2])
            nerr = float(lines[i+8].split()[4])
            ucos = float(lines[i+9].split()[2])
            uerr = float(lines[i+9].split()[4])
            hout.write(f'{line[2:6]}  {ecos:8.2f}  {ncos:8.2f}  {eerr:8.2f}  {nerr:8.2f}\n')
            vout.write(f'{line[2:6]}  {ucos:8.2f}  {uerr:8.2f}\n')
inp.close()
hout.close()
vout.close()        
