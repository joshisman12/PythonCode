import glob

edat = glob.glob(r'.\*_e_c.dat')
ndat = glob.glob(r'.\*_n_c.dat')
udat = glob.glob(r'.\*_u_c.dat')
eout = open(r'.\post_offset_e.dat','w')
nout = open(r'.\post_offset_n.dat','w')
uout = open(r'.\post_offset_u.dat','w')

endtime = open(r'.\possible_endtime.dat')
endtime_lines = endtime.readlines()[0].split()
endtime1 = float(endtime_lines[0])
endtime2 = float(endtime_lines[1])
endtime3 = float(endtime_lines[2])
endtime4 = float(endtime_lines[3])

eq_time =2016.09836
print(f'Earthquake time: {eq_time}')
print(f'Postseismic endtime: {endtime1}  {endtime2}  {endtime3}  {endtime4}')
for k in edat :
    inp = open(k)
    lines = inp.readlines()

    print('')
    print(f'Processing station: {k}')

    # Because some stations don't have the data of the specified poseismic end time,
    # thus using the data right before the specified time

    bf_eq_max_time = 0
    bf_postend_max_time1 = 0
    bf_postend_max_time2 = 0
    bf_postend_max_time3 = 0
    bf_postend_max_time4 = 0
    for i, line in enumerate(lines):
        time, pos = line.split()
        
        if float(lines[i].split()[0]) <= float(eq_time):
            bf_eq_max_time = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime1):
            bf_postend_max_time1 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime2):
            bf_postend_max_time2 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime3):
            bf_postend_max_time3 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime4):
            bf_postend_max_time4 = float(lines[i].split()[0])    

    for i, line in enumerate(lines) :
        time, pos = line.split()

        if float(time) == bf_eq_max_time :
            cos_offset = float(lines[i+1].split()[1])-float(pos)
            print(f'coseismic offset: {cos_offset}')
            cos_pos = float(lines[i+1].split()[1])
        if float(time) == bf_postend_max_time1 :
            postend_pos1 = float(pos)
            print(postend_pos1)
        if float(time) == bf_postend_max_time2 :
            postend_pos2 = float(pos)
            print(postend_pos2)
        if float(time) == bf_postend_max_time3 :
            postend_pos3 = float(pos)
            print(postend_pos3)
        if float(time) == bf_postend_max_time4 :
            postend_pos4 = float(pos)
            print(postend_pos4)
    post_offset1 = postend_pos1 - cos_pos
    post_offset2 = postend_pos2 - cos_pos
    post_offset3 = postend_pos3 - cos_pos
    post_offset4 = postend_pos4 - cos_pos
    eout.write(f'{k}  {post_offset1:8.2f}  {post_offset2:8.2f}  {post_offset3:8.2f}\
  {post_offset4:8.2f}\n')
    inp.close()
eout.close()

for k in ndat :
    inp = open(k)
    lines = inp.readlines()

    print('')
    print(f'Processing station: {k}')

    bf_eq_max_time = 0
    bf_postend_max_time1 = 0
    bf_postend_max_time2 = 0
    bf_postend_max_time3 = 0
    bf_postend_max_time4 = 0
    for i, line in enumerate(lines):
        time, pos = line.split()
        
        if float(lines[i].split()[0]) <= float(eq_time):
            bf_eq_max_time = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime1):
            bf_postend_max_time1 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime2):
            bf_postend_max_time2 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime3):
            bf_postend_max_time3 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime4):
            bf_postend_max_time4 = float(lines[i].split()[0])    

    for i, line in enumerate(lines) :
        time, pos = line.split()

        if float(time) == bf_eq_max_time :
            cos_offset = float(lines[i+1].split()[1])-float(pos)
            print(f'coseismic offset: {cos_offset}')
            cos_pos = float(lines[i+1].split()[1])
        if float(time) == bf_postend_max_time1 :
            postend_pos1 = float(pos)
            print(postend_pos1)
        if float(time) == bf_postend_max_time2 :
            postend_pos2 = float(pos)
            print(postend_pos2)
        if float(time) == bf_postend_max_time3 :
            postend_pos3 = float(pos)
            print(postend_pos3)
        if float(time) == bf_postend_max_time4 :
            postend_pos4 = float(pos)
            print(postend_pos4)
    post_offset1 = postend_pos1 - cos_pos
    post_offset2 = postend_pos2 - cos_pos
    post_offset3 = postend_pos3 - cos_pos
    post_offset4 = postend_pos4 - cos_pos
    nout.write(f'{k}  {post_offset1:8.2f}  {post_offset2:8.2f}  {post_offset3:8.2f}\
  {post_offset4:8.2f}\n')
    inp.close()
nout.close()

for k in udat :
    inp = open(k)
    lines = inp.readlines()

    print('')
    print(f'Processing station: {k}')

    bf_eq_max_time = 0
    bf_postend_max_time1 = 0
    bf_postend_max_time2 = 0
    bf_postend_max_time3 = 0
    bf_postend_max_time4 = 0
    for i, line in enumerate(lines):
        time, pos = line.split()
        
        if float(lines[i].split()[0]) <= float(eq_time):
            bf_eq_max_time = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime1):
            bf_postend_max_time1 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime2):
            bf_postend_max_time2 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime3):
            bf_postend_max_time3 = float(lines[i].split()[0])
        if float(lines[i].split()[0]) <= float(endtime4):
            bf_postend_max_time4 = float(lines[i].split()[0])    

    for i, line in enumerate(lines) :
        time, pos = line.split()

        if float(time) == bf_eq_max_time :
            cos_offset = float(lines[i+1].split()[1])-float(pos)
            print(f'coseismic offset: {cos_offset}')
            cos_pos = float(lines[i+1].split()[1])
        if float(time) == bf_postend_max_time1 :
            postend_pos1 = float(pos)
            print(postend_pos1)
        if float(time) == bf_postend_max_time2 :
            postend_pos2 = float(pos)
            print(postend_pos2)
        if float(time) == bf_postend_max_time3 :
            postend_pos3 = float(pos)
            print(postend_pos3)
        if float(time) == bf_postend_max_time4 :
            postend_pos4 = float(pos)
            print(postend_pos4)
    post_offset1 = float(postend_pos1) - float(cos_pos)
    post_offset2 = float(postend_pos2) - float(cos_pos)
    post_offset3 = float(postend_pos3) - float(cos_pos)
    post_offset4 = float(postend_pos4) - float(cos_pos)
    uout.write(f'{k}  {post_offset1:8.2f}  {post_offset2:8.2f}  {post_offset3:8.2f}\
  {post_offset4:8.2f}\n')
    inp.close()
uout.close()    
