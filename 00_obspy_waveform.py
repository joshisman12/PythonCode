from obspy import read
import numpy as np
import matplotlib.pyplot as plt


st = read('*.SAC',format = 'sac')
stf = st.copy()

stf.detrend(type = 'demean')
stf.detrend(type = 'linear')
stf.taper(0.05, type='hann')

#--------------------------------------------#
# plot waveform
# dt = st[0].stats.starttime
# stf.plot(outfile = 'CHY063_waveform.png',starttime = dt + 15, endtime = dt + 15 + 44)
#--------------------------------------------#


#--------------------------------------------#
# plot spectrogram
# stf[0].spectrogram(log=True, title='CHY063 ENE' + str(st[0].stats.starttime), outfile = 'CHY063_ENE_spectrogram.png')
# stf[1].spectrogram(log=True, title='CHY063 ENN' + str(st[1].stats.starttime), outfile = 'CHY063_ENN_spectrogram.png')
# stf[2].spectrogram(log=True, title='CHY063 ENZ' + str(st[2].stats.starttime), outfile = 'CHY063_ENZ_spectrogram.png')
#--------------------------------------------#


#--------------------------------------------#
'''
# high pass
tre = st[2]
freq = 8.5
tre_filt = tre.copy()
tre_filt.filter('highpass', freq=freq, corners=2, zerophase=True)
freq = str(freq)
# plot raw and filtered data
t = np.arange(0, tre.stats.npts / tre.stats.sampling_rate, tre.stats.delta)
plt.subplot(211)
plt.axis([10,60,-450,400])
plt.plot(t, tre.data, 'k')
plt.ylabel('Raw Data')
plt.subplot(212)
plt.axis([10,60,-50,60])
plt.plot(t, tre_filt.data, 'k')
plt.ylabel('Highpassed Data')
plt.xlabel('Time [s]')
plt.suptitle('HHLA_ENZ '+str(tre.stats.starttime))
plt.text(50, 15, 'hp: '+freq+'Hz', size = 10)
plt.savefig('HHLA_ENZ_Highpass_'+freq+'Hz.png')
plt.show()
'''
#--------------------------------------------#

#--------------------------------------------#
# save file to ascii format
for tr in stf:
    channel = tr.stats.channel
    tr.write('2016.02.05.19.57.26.CHY063.'+channel+'.dat',format = 'TSPAIR')
