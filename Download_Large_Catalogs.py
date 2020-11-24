import datetime as dt
from obspy.clients.fdsn import Client
client = Client(" ")
from obspy import UTCDateTime

minlat = 
maxlat = 
minlon = 
maxlon = 
starttime = UTCDateTime(" ")
endtime = UTCDateTime(" ")
minmag = 

temp_starttime = starttime
temp_endtime = starttime+dt.timedelta(weeks=4)
Catalog = client.get_events(minlatitude=minlat, maxlatitude=maxlat, minlongitude=minlon, maxlongitude=maxlon,
                                    minmagnitude=minmag, starttime=temp_starttime, endtime=temp_endtime, orderby="time-asc")
while 1:
    temp_Catalog = client.get_events(minlatitude=minlat, maxlatitude=maxlat, minlongitude=minlon, maxlongitude=maxlon,
                                    minmagnitude=minmag, starttime=temp_starttime, endtime=temp_endtime, orderby="time-asc")
    Catalog.__iadd__(temp_Catalog)
    temp_starttime += dt.timedelta(weeks=4)
    temp_endtime += dt.timedelta(weeks=4)
    if temp_endtime > endtime:
        Catalog.__iadd__(client.get_events(minlatitude=minlat, maxlatitude=maxlat, minlongitude=minlon, maxlongitude=maxlon,
                                minmagnitude=minmag, starttime=temp_starttime, endtime=endtime, orderby="time-asc"))
        break


Catalog.write('obspy_cat.txt', format='ZMAP')
