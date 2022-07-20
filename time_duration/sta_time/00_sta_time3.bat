echo off
gmtset FORMAT_DATE_MAP  yyyy-mm 
set ps=00_data_duration3.ps
set name=00_data_duration3.jpg
set year=1997
gmt psbasemap -JX17T/15 -R%year%-01-01T/2023-08-31T/-12/12 -Bxa2Yf6O1+l"Duration Time(year)" -By0+l"CGPS." -BWeSN -K -P -V > %ps%

rem Meinong EQ
echo 2016.09836 12 > tmp
echo 2016.09836 -12 >> tmp
gmt psxy tmp -R -J -W1,black -K -O -V  >> %ps%

rem -畫出各站time duration-
gmt psxy HHLA_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y6.5    >> %ps% 
gmt psxy HOKN_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy HSR3_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy KAWN_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy LAN2_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy LIAN_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy LNCH_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy MLO1_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy MLON_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy NANK_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy NCKU_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy NEMN_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy S011_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy S012_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%




rem -站名-
echo 2022.5 0 HHLA | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y13 >> %ps%
echo 2022.5 0 HOKN | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 HSR3 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 KAWN | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 LAN2 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 LIAN | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 LNCH | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 MLO1 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 MLON | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 NANK | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 NCKU | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 NEMN | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 S011 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 S012 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%

gmt psxy -R -J -T -O >> %ps%

del tmp*
psconvert %ps% -Tj -A 
%name%