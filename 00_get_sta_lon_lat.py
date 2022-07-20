import glob
CGPS_files = glob.glob(r'./ncu.final_igb14.pos/*.pos')
SGPS_files = glob.glob(r'./cgs.final_igb14.pos/*.pos')
out1 = open(r'./00_NCU_CGPS_sta.dat','w')
out2 = open(r'./00_NCU_SGPS_sta.dat','w')

for i in CGPS_files:
    inp = open(i,'r')
    lines = inp.readlines()
    for k, line in enumerate(lines):

        if str(line[0:12]) == 'Station name':
            sta_name = str(line.split()[3])
        
        if str(line[0:3]) == 'NEU':             
            lon = float(line.split()[5])
            lat = float(line.split()[4])
            Up  = float(line.split()[6])
    out1.write(f'{lon:.4f}  {lat:.4f}  {sta_name}\n')
    inp.close()
out1.close()    

for i in SGPS_files:
    inp = open(i,'r')
    lines = inp.readlines()
    for k, line in enumerate(lines):

        if str(line[0:12]) == 'Station name':
            sta_name = str(line.split()[3])
        
        if str(line[0:3]) == 'NEU':             
            lon = float(line.split()[5])
            lat = float(line.split()[4])
            Up  = float(line.split()[6])
    out2.write(f'{lon:.4f}  {lat:.4f}  {sta_name}\n')
    inp.close()
out2.close()    