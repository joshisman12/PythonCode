'''
Python code to calculate postseismic offset, using 2 way to define postseismic
endtime. End_time1 is decided when the slope variation is 0, end_time2 is
decided when the slope variation is below 0.002

###Postseismic offset and endtime are only just reference, we can decide different
endtime to calculate the postseismic displacement field

'''

import glob

cdat = glob.glob(r'..\*_e_c.dat')
out = open(r'.\post_endtime.dat','w')
eq_time =2016.09836
print(f'Earthquake time: {eq_time}')
for k in cdat :
    inp = open(k)
    lines = inp.readlines()
    print('')
    print(f'Processing station: {k}')
    
    bf_eq_max_time = 0
    for j, line in enumerate(lines) :
        time, pos = line.split()

        if float(lines[j].split()[0]) <= float(eq_time):
            bf_eq_max_time = float(lines[j].split()[0])
               
    end_time = 0     
    end_time1 = 0
    end_time2 = 0
    final_endtime = 0          
    for i, line in enumerate(lines) :
        time, pos = line.split()
        
        if float(time) == bf_eq_max_time :
            cos_offset = float(lines[i+1].split()[1])-float(pos)
            print(f'coseismic offset: {cos_offset}')
            cos_pos = lines[i+1].split()[1]
          
        last_pos = lines[len(lines)-1].split()[1]
        last_time = lines[len(lines)-1].split()[0]
        
        if i != len(lines)-1 : #i+1 can't excess the last one
            if float(time) > bf_eq_max_time :
                post_pos = lines[i].split()[1]
                post_time = lines[i].split()[0]
                post_pos_1 = lines[i+1].split()[1]
                post_time_1 = lines[i+1].split()[0]
                #print(last_time)
                #print(post_time)

                if (float(last_time) - float(post_time)) > 0.003 : #one day before the last day
                    slope = (float(last_pos) - float(post_pos)) /  (float(last_time) - \
                    float(post_time))
                    slope_1 = (float(last_pos) - float(post_pos_1)) /  (float(last_time) - \
                    float(post_time_1))
                    #print(slope_1 - slope)
                    #if (abs(slope) < abs(slope_1)) and (abs(slope - slope_1) > 0.001) :
                    #    end_time = time
                    #else :    
                    #    print(time)
                    if abs(slope) > abs(slope_1)  :
                        end_time1 = float(time)
                    else: 
                        print(end_time1)
                        break #need the first day of slope_1 > slope, cause the slope may
                              #change back again  
                    
    for i, line in enumerate(lines) :
        time, pos = line.split()
    
        if i != len(lines)-1 :
            if float(time) > bf_eq_max_time :
                post_pos = lines[i].split()[1]
                post_time = lines[i].split()[0]
                post_pos_1 = lines[i+1].split()[1]
                post_time_1 = lines[i+1].split()[0]

                if (float(last_time) - float(post_time)) > 0.003 : 
                    slope = (float(last_pos) - float(post_pos)) /  (float(last_time) - \
                    float(post_time))
                    slope_1 = (float(last_pos) - float(post_pos_1)) /  (float(last_time) - \
                    float(post_time_1))    

                    if abs(slope - slope_1) > 0.002 :
                        end_time2 = float(time)
                    else :
                        print(end_time2)
                        break
    if float(end_time1) >= float(end_time2) :
        final_endtime = end_time1
    else :
        final_endtime = end_time2    
    print(final_endtime) 
    for i, line in enumerate(lines) :
        time, pos = line.split()       
        if float(time) == final_endtime :
            end_pos = lines[i].split()[1]
            print(end_pos)
            print(cos_pos)
            post_offset = float(end_pos) - float(cos_pos)
            print(f'postseismic offset: {post_offset}')
            out.write(f'{k}    {end_time1:10.5f}    {end_time2:10.5f}\
    {final_endtime:10.5f}    {post_offset:8.2f}\n')
    



        #if float(time) > eq_time : 
        #    sum = 0
        #    for n in range(1,5): #if the station stays at same position for five straight days,
        #                         #then  I will define the first day of the five straight days
        #                         #as the end time of the postseismic offset
        #        sum = sum + float(lines[i+n].split()[1])-float(pos)
        #    if sum == 0 :
        #        end_time = time
        #        end_pos = pos
        #        post_offset = float(pos) - float(cos_pos)
        #        print(f'postseismic end time: {time}')
        #        print(f'postseismic offset: {post_offset}')
        #        out.write(f'{k} {time}  {post_offset}\n')
        #        break
    inp.close() 
out.close()       