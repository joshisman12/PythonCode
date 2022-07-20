import re
inp = open(r'D:\Hsinhua_fault\josh\earthquake_catalog\GDMScatalog_2020_202012.txt')
out = open(r'D:\Hsinhua_fault\josh\earthquake_catalog\CWB_GDMS_1900_202012.list','w')
lines = inp.readlines()

for i,line in enumerate(lines):
    if i > 0 :
        result = re.split('-|:| |\n',line)
        print(result)
        print(f'{result[0]} {result[1]} {result[2]} {result[3]} {result[4]} {result[5]} 0 {result[7]} {result[6]} {result[8]} {result[9]} 0')
        out.write(f'{result[0]} {result[1]} {result[2]} {result[3]} {result[4]} {result[5]} 0 {result[7]} {result[6]} {result[8]} {result[9]} 0\n')
inp.close()
out.close()        
