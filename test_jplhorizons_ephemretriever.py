# script to test jplhorizons_query.py
from casatools import quanta
import jplhorizons_query

objn = 'MARS'
_qa = quanta()
# starttime='2010/01/01'
# mjd 59214
starttime = '2020/12/31'
stoptime = '2030/12/31'
step = '1d'
startmjd = int(_qa.totime(starttime)['value'])
endmjd = int(_qa.totime(stoptime)['value'])
outtable = objn.capitalize()+'_'+str(startmjd)+'-'+str(endmjd)+'dUTC_new.tab'
jplhorizons_query.getjplephem(objn, starttime, stoptime, step, outtable)
