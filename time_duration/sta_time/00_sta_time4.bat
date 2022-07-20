echo off
gmtset FORMAT_DATE_MAP  yyyy-mm 
set ps=00_data_duration4.ps
set name=00_data_duration4.jpg
set year=1997
gmt psbasemap -JX17T/15 -R%year%-01-01T/2023-08-31T/-12/12 -Bxa2Yf6O1+l"Duration Time(year)" -By0+l"CGPS." -BWeSN -K -P -V > %ps%

rem Meinong EQ
echo 2016.09836 12 > tmp
echo 2016.09836 -12 >> tmp
gmt psxy tmp -R -J -W1,black -K -O -V  >> %ps%

rem -畫出各站time duration-
gmt psxy S092_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y5    >> %ps% 
gmt psxy S106_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy S169_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy SHWA_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy TSHO_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy WANC_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy WHE2_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy WHES_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy WUST_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy YJLO_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy YSAN_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%
gmt psxy ZEND_time.dat -JX17/15  -R%year%.0027/2023.66575/-12/12 -Ss0.1 -Gred -K -O -V -Y-1 >> %ps%

rem -站名-
echo 2022.5 0 S092 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y11 >> %ps%
echo 2022.5 0 S106 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 S169 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 SHWA | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 TSHO | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 WANC | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 WHE2 | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 WHES | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 WUST | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 YJLO | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 YSAN | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%
echo 2022.5 0 ZEND | gmt pstext -JX -R -N  -F+f10p,0  -W1,255/0/0 -K -O  -P -V -Y-1 >> %ps%

gmt psxy -R -J -T -O >> %ps%

del tmp*
psconvert %ps% -Tj -A 
%name%