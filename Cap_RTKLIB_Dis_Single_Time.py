import pandas as pd
import os
import numpy as np
import datetime
from obspy import UTCDateTime

#path = os.getcwd()
#print(path)
#os.chdir('50Hz')
sta = 'HHLA'

time_output = 'relative' # absolute
data = pd.read_table('.\\50Hz\\'+sta+'036t.16o.pos', sep='\s+', skiprows=18,\
                     usecols=[1,2,3,4],names=['time','epos','npos','upos'])

after_sec  = 120
before_sec = -10
sampling  = 50

data['index1'] = data.index.values
et = data[data['time']=='19:57:26.000']  
#et = data[data['time']=='19:57:26.000']  (seismogram time)
#et = data[data['time']=='19:57:47.000']  (Fit SMS time)
#et = data[data['time']=='19:57:27.000']  (GPS time)
# Meinong earthquake original time 19:57:27.00 UTC  [GPS time = UTC time + 17 at 2016]

e_index = int(et['index1'])
e_abs_t = str(et['time'])
e_epos = float(et['epos'])
e_npos = float(et['npos'])
e_upos = float(et['upos'])
print(e_index, e_epos, e_npos, e_upos)

o_index =[]
o_abs_t = []
o_epos =[]
o_npos =[]
o_upos =[]
for i in range(0,len(data)):
    d_index = int(data['index1'][i])
    d_abs_t = str(data['time'][i])
    d_epos = float(data['epos'][i])
    d_npos = float(data['npos'][i])
    d_upos = float(data['upos'][i])
    
    o_index.append(d_index-e_index)  #Time relative to event time
    o_abs_t.append(d_abs_t)          #UTC time
    o_epos.append(d_epos-e_epos)     #Locations relative to event locations
    o_npos.append(d_npos-e_npos)
    o_upos.append(d_upos-e_upos)
    
out = np.column_stack([o_index, o_abs_t,o_epos, o_npos, o_upos])
outDf = pd.DataFrame(out,columns=['index1', 'o_abs_t','epos', 'npos', 'upos'])
# output result is 'cm'!!!!!!    
outDf['epos'] = [float(i)*100 for i in outDf['epos'].tolist()]
outDf['npos'] = [float(i)*100 for i in outDf['npos'].tolist()]
outDf['upos'] = [float(i)*100 for i in outDf['upos'].tolist()]
outDf['index1'] = outDf['index1'].values.astype(int)

result_time = [i for i in np.linspace(before_sec,after_sec,int((after_sec-before_sec)*sampling)+1)]
c_outDf = outDf[(outDf['index1']<=after_sec*sampling) & (outDf['index1']>=before_sec*sampling)]
c_outDf['index1']=result_time
np.savetxt('.\\50Hz\\'+sta+'_RTKLIB_50Hz_120sec.dat', c_outDf, fmt='%12.5f  %11s  %10.5f %10.5f %10.5f')
    