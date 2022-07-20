echo off
gmtset FORMAT_DATE_MAP  yyyy-mm 
set ps=00_data_duration2.ps
set name=00_data_duration2.jpg
set year=1995
gmt psbasemap -JX17T/15 -R%year%-01-01T/2023-08-31T/-12/12 -Bxa2Yf6O1+l"Duration Time(year)" -By0+l"CGPS." -BWeSN -K -P -V > %ps%

rem Meinong EQ
echo 2016.09836 12 > tmp
echo 2016.09836 -12 >> tmp
gmt psxy tmp -R -J -W1,black -K -O -V  >> %ps%

rem -畫出各站time duration-
gmt psxy BKBL_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y6.5    >> %ps% 
gmt psxy CHKU_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CISH_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CK01_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CKGM_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CKST_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CKSV_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy CKUM_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy DANI_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy DJES_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy EQLD_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS28_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS29_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS30_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%




rem -站名-
echo 2022.5 0 BKBL | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y13 >> %ps%
echo 2022.5 0 CHKU | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CISH | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CK01 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CKGM | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CKST | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CKSV | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 CKUM | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 DANI | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 DJES | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 EQLD | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS28 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS29 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS30 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%

gmt psxy -R -J -T -O >> %ps%

del tmp*
psconvert %ps% -Tj -A 
%name%