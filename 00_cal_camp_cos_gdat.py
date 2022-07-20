import glob
import pandas as pd
import numpy as np

edat = glob.glob(r'D:\Hsinhua_fault\01.campaign\01_raw\*_e_g.dat')
ndat = glob.glob(r'D:\Hsinhua_fault\01.campaign\01_raw\*_n_g.dat')
udat = glob.glob(r'D:\Hsinhua_fault\01.campaign\01_raw\*_u_g.dat')
eout = open(r'.\camp_cos_offset_e.dat','w')
nout = open(r'.\camp_cos_offset_n.dat','w')
uout = open(r'.\camp_cos_offset_u.dat','w')

dat = [edat,ndat,udat]


eq_time =2016.09836
print(f'Earthquake time: {eq_time}')
for m in dat:
    for k in m :
        inp = open(k)
              
        lines = inp.readlines()
    
        #print('')
        #print(f'Processing station: {k}')

        # Because some stations don't have the data of the specified poseismic end time,
        # thus using the data right before the specified time

        bf_eq_max_time = 0
        for i, line in enumerate(lines):
            time, pos, err = line.split()

            #recursively find the time right before the earthquake
            if float(lines[i].split()[0]) <= float(eq_time):
                bf_eq_max_time = float(lines[i].split()[0])

        for i, line in enumerate(lines) :
            time, pos, err = line.split()

            if float(time) == bf_eq_max_time :
                cos_offset = float(lines[i+1].split()[1])-float(pos)
                cos_offset_err = (float(lines[i+1].split()[2])**2+float(err)**2)**(1/2)
                #print(f'coseismic offset: {cos_offset} +- {cos_offset_err}')
                cos_pos = float(lines[i+1].split()[1])
        if m == dat[0]:
            eout.write(f'{k}  {cos_offset:8.2f} {cos_offset_err:8.2f}\n')
        if m == dat[1]:
            nout.write(f'{k}  {cos_offset:8.2f} {cos_offset_err:8.2f}\n')
        if m == dat[2]:
            uout.write(f'{k}  {cos_offset:8.2f} {cos_offset_err:8.2f}\n')

        inp.close()
    eout.close()

#------------------------------#
df1 = pd.read_csv('camp_cos_offset_e.dat',sep = r'\s+', header = None, \
names = ['sta_path', 'pos', 'err'])

df2 = pd.read_csv('camp_cos_offset_n.dat',sep = r'\s+', header = None, \
names = ['sta_path', 'pos', 'err'])

df3 = pd.read_csv('camp_cos_offset_u.dat',sep = r'\s+', header = None, \
names = ['sta_path', 'pos', 'err'])

df4 = pd.read_csv('00_tmp_out.dat',sep = r'\s+', header = None, \
names = ['sta_name', 'lon', 'lat'])

#create empty dataframe
df_h_out = pd.DataFrame(columns = ['sta', 'lon', 'lat', 'e_offset', 'n_offset', 'eerr', 'nerr']) 

df_h_out['e_offset'] = df1['pos'] 
df_h_out['n_offset'] = df2['pos']
df_h_out['eerr'] = df1['err']
df_h_out['nerr'] = df2['err']
df_h_out['sta'] = df4['sta_name']
df_h_out['lon'] = df4['lon']
df_h_out['lat'] = df4['lat']

df_h_out.to_csv(r'.\camp_cos_offset_h.dat', header = None, index = None, sep = ' ')

df_v_out = pd.DataFrame(columns = ['sta', 'lon', 'lat', 'v_offset', 'verr']) 

df_v_out['sta'] = df4['sta_name']
df_v_out['lon'] = df4['lon']
df_v_out['lat'] = df4['lat']
df_v_out['v_offset'] = df3['pos']
df_v_out['verr'] = df3['err']

df_v_out.to_csv(r'.\camp_cos_offset_v.dat', header = None, index = None, sep = ' ')

#df_tmp = df1.loc[:, 'sta_path']
#df_tmp.head()
