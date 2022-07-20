#change remove_20210526's results with same stations in remove_Ching.para
inp1 = open(r'D:\Hsinhua_fault\josh\NCU_CGPS\00_Ching_fitting\00_fit\01_remove\remove_20210526.para')
inp2 = open(r'D:\Hsinhua_fault\josh\NCU_CGPS\00_Ching_fitting\00_fit\01_remove\remove_Ching.para')
out = open(r'D:\Hsinhua_fault\josh\NCU_CGPS\00_Ching_fitting\00_fit\01_remove\remove_tmp.para','w')

lines1 = inp1.readlines()
lines2 = inp2.readlines()

for i in lines1 :
    switch=0
    
    for j in lines2 :
        if i[0:4] == j[0:4] : #if once if condition established, then switch = 1, it won't write the origin results in remove_20210526 and be replaced by remove_Ching.para
            switch = 1
            print(i[0:4])
            out.write(f'{j}')

    if switch == 0:
        out.write(f'{i}')

                   
inp1.close()
inp2.close()
out.close()

