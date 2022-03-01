# A script to test jplhorizons_query.py 
# This script assumes jplhorizons_query.py is located in the current working directory)
from casatools import quanta
import sys
sys.path.append('.')
import jplhorizons_query

_qa = quanta()

# === modify here ===
# object name reconginzed by JPL-Horizons 
# Can be check with the web app (https://ssd.jpl.nasa.gov/horizons/app.html#/)
objname = 'C/2012 F6'
# time range 
starttime = '2013/05/10'
stoptime = '2013/05/12'
# increment
step = '1m'
#output ephemeris table
prefix = 'Lemmon'
startmjd = int(_qa.totime(starttime)['value'])
endmjd = int(_qa.totime(stoptime)['value'])
outtable = prefix+'_'+str(startmjd)+'-'+str(endmjd)+'dUTC_new.tab'
# === end  ===

# Do query using the JPL-Horizons api and returns ephemeris data in CASA table format
#
# For a quick ckeck the generated table is readable by CASA, do
#   me.framecomet('the_table_generated')
#
# Use asis=True for non-standard objects
# savetofile = True, saves direct returned ephemeris data in the text file ('jplhorizons.ephem') for 
# cross checking
jplhorizons_query.gethorizonsephem(obj, starttime, stoptime, step, outtable, asis=True, savetofile=True)
