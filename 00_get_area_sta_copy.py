import glob
import shutil #copy file to specified folder

inp1 = open(r'D:\Hsinhua_fault\josh\NCKU_CGNSS\sta\00_NCKU_CGNSS.gmt')
#lon,lat,station name
lines = inp1.readlines()
file_path = glob.glob(r'..\..\01_bern2time\*_?_b.dat')

for i in file_path:
    file_sta=i.split('\\')[3][3:7]
    file_name=i.split('\\')[3]
    for k, line in enumerate(lines):
        lon,lat,sta_name = line.split()
        if str(file_sta) == str(sta_name):
            original = i
            target = f'.\\{file_name}'
            print(original)
            print(target)
            shutil.copyfile(original,target)
inp1.close()            
    
'''
out = open(r'.\sta_list.dat','w')

lines1 = inp1.readlines()
lines2 = inp2.readlines()


for i in lines1:
    switch = 0
    for j in lines2:
        if j[0] != str(1):
            #print(i[20:25])
            #print(j[0:4])
            
            if str(i[20:24]) == str(j[0:4]):
                
                switch = 1
            
                   
    if switch == 0:
        out.write(f'{i[20:25]}')


out.close()
inp1.close()
inp2.close()
'''