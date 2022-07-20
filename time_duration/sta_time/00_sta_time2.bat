echo off
gmtset FORMAT_DATE_MAP  yyyy-mm 
set ps=00_data_duration2.ps
set name=00_data_duration2.jpg
set year=2006
gmt psbasemap -JX17T/15 -R%year%-01-01T/2023-08-31T/-12/12 -Bxa2Yf6O1+l"Duration Time(year)" -By0+l"CGPS." -BWeSN -K -P -V > %ps%

rem Meinong EQ
echo 2016.09836 12 > tmp
echo 2016.09836 -12 >> tmp
gmt psxy tmp -R -J -W1,black -K -O -V  >> %ps%

rem -畫出各站time duration-
gmt psxy GS31_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y6.5    >> %ps% 
gmt psxy GS32_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS33_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS34_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS35_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS51_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS73_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS74_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS75_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS79_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS88_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS89_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS96_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy GS97_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%




rem -站名-
echo 2022.5 0 GS31 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y13 >> %ps%
echo 2022.5 0 GS32 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS33 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS34 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS35 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS51 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS73 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS74 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS75 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS79 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS88 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS89 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS96 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 GS97 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%

gmt psxy -R -J -T -O >> %ps%

del tmp*
psconvert %ps% -Tj -A 
%name%