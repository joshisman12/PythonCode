inp = open(r'D:\Hsinhua_fault\josh\earthquake_catalog\CWB_EQ_19910101-20201209_1.dat')
out = open(r'D:\Hsinhua_fault\josh\earthquake_catalog\CWB_EQ_19910101-20201209.dat','w')
lines = inp.readlines()
for i, line in enumerate(lines):
    
    if line.find(",") == -1:
        print(line)
        
        out.write(f'{line}')
    else :
        time,lon,lat,mag,depth = line.split(',')
        out.write(f'{time}  {lon}  {lat}  {mag}  {depth}')
out.close()
inp.close()            