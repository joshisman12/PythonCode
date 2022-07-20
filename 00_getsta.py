import glob


inp = glob.glob(r'.\*.pos')
#out = open(r'.\sta_list.dat','w')

for i in inp:
    print(i[2:6])
    
    #out.write(f'{i[2:6]}\n')
#out.close()
