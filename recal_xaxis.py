import glob
dat = glob.glob(r'.\2016.02.05.19.57.26.CHY063.*.dat')
print(dat)

for k in dat:

    inp = open(k)
    channel = k[29:32]
    lines = inp.readlines()

    out = open(f'.\\2016-02-05T19.57.27.000.CHY063.'+channel+'.dat','w')
    for i, line in enumerate(lines):
        if i > 0:
            # reference time
            time0, pos0 = lines[1].split()
            minutes0 = time0[14:16]
            seconds0 = time0[17:26]

            time, pos = line.split()
            pos = float(pos)
            minutes = time[14:16]
            seconds = time[17:26]

            # final time, the Meinong earthquake occurred time is 2016-02-05T19:57:27:000 (written in onesecond)
            # this time is set to be zero
            timef = float(seconds) - float(seconds0) + (float(minutes) - float(minutes0))*60 + 7

            # format : seconds after earthquake time, position
            out.write(f'{timef:5.3f}   {pos:5.3f}\n')

    out.close()
    inp.close()