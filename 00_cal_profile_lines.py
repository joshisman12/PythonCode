import math

def cal_pro(lon1,lat1,lon2,lat2,wid):
    lon1,lat1,lon2,lat2=float(lon1),float(lat1),float(lon2),float(lat2)
    latdt=111.325
    londt=math.cos(lon1*math.pi/180)*latdt
    arr=((lon2-lon1)*londt,(lat2-lat1)*latdt)
    leng=math.sqrt(arr[0]**2+arr[1]**2)
    
    
    arr1=((lat2-lat1)/leng*wid,-(lon2-lon1)/leng*wid)
    arr2=(-(lat2-lat1)/leng*wid,(lon2-lon1)/leng*wid)
    lin1ax=lon1+arr1[0]
    lin1ay=lat1+arr1[1]
    lin1bx=lon1+arr2[0]
    lin1by=lat1+arr2[1]
    lin2ax=lon2+arr1[0]
    lin2ay=lat2+arr1[1]
    lin2bx=lon2+arr2[0]
    lin2by=lat2+arr2[1]
    
    out=open(r'.\profile.gmt','w')
    out.write(f'>\n')
    out.write(f'{lon1:8.4f}  {lat1:8.4f}\n')
    out.write(f'{lon2:8.4f}  {lat2:8.4f}\n')
    out.write(f'>\n')
    out.write(f'{lin1ax:8.4f}  {lin1ay:8.4f}\n')
    out.write(f'{lin2ax:8.4f}  {lin2ay:8.4f}\n')
    out.write(f'{lin2bx:8.4f}  {lin2by:8.4f}\n')
    out.write(f'{lin1bx:8.4f}  {lin1by:8.4f}\n')
    
    
    out.close()

lon1=120.2666
lat1=23.0481
lon2=120.3294
lat2=23.0088
wid=0.4


cal_pro(lon1,lat1,lon2,lat2,wid)

