# script to test jplhorizons_query.py
from casatools import quanta
import sys
sys.path.append('.')
import jplhorizons_query

#objlist = ['Callisto',
#           'Ceres',
#           'Europa',
#           'Ganymede',
#          'Io',
objlist = ['Juno',
           'Jupiter',
           'Lutetia',
           'Mercury',
#           'Moon',
           'Neptune',
           'Pallas',
           'Pluto',
           'Saturn',
           'Sun',
           'Titan',
           'Uranus',
           'Venus',
           'Vesta']
objlist = ['Ceres']
#objn = 'MARS'
custom_step_list={'Io':'6h',
                  'Moon':'1h'}
_qa = quanta()
# starttime='2010/01/01'
# mjd 59214
starttime = '2020/12/31'
stoptime = '2030/12/31'
step = '1d'

startmjd = int(_qa.totime(starttime)['value'])
endmjd = int(_qa.totime(stoptime)['value'])

for obj in objlist:
    print("obj = ", obj)
    if obj in custom_step_list:
        step = custom_step_list[obj]
    outtable = obj.capitalize()+'_'+str(startmjd)+'-'+str(endmjd)+'dUTC_new.tab'
    jplhorizons_query.getjplephem(obj, starttime, stoptime, step, outtable, savetofile=True)
