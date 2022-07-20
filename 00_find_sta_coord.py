#find stations coordinates of the result stations
inp1 = open(r'.\TPN_All.Pos')
inp2 = open(r'.\sta_list.dat')
out = open(r'.\NCU_all_sta.dat','w')

lines1 = inp1.readlines()
lines2 = inp2.readlines()

for i in lines1 :
    #print(i)
    #print(i[22:26])
    #print(type(i[22:26]))
    

    for j in lines2 :
        #print(line[4])
        #
        #print(f'line4 type={type(line[4])}')
        #print(j.strip('\n'))
        #
        #print(f'j type={type(j)}')
        
        if i[22:26] == j.strip('\n') :
            print(i[22:26])
        #else: 
        #    print('error')            
            out.write(f'{i[2:26]}\n')

       
inp1.close()
inp2.close()
out.close()

