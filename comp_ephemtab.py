import numpy as np
from casatools import table
#testddxxxx
objectname='Neptune'
mjdstr='59214-62866dUTC'
#mjdstr='55197-59214dUTC'
# for Sun
#mjdstr='58849-62866dUTC'
#ephemdir='/home/casa/data/trunk/ephemerides/JPL-Horizons/'
ephemdir='/Users/ttsutsum/SWDevel/casa-data/ephemerides/JPL-Horizons/'
tabname = objectname+'_'+mjdstr+'_J2000.tab'
reftab=ephemdir+tabname

tb2 = table()

intab = objectname+'_'+mjdstr+'_new.tab'
dcolkeys = {}
refcolkeys = {}

tb.open(intab)
tbkeys = tb.getkeywords()
datacolnames = tb.colnames()
for dc in datacolnames:
    dcolkeys[dc] = tb.getcolkeywords(dc)
tb.done()

tb.open(reftab)
reftbkeys = tb.getkeywords()
refdatacolnames = tb.colnames()
for rc in refdatacolnames:
    refcolkeys[rc] = tb.getcolkeywords(rc)
tb.done()
print("reftbkeys=",reftbkeys)

# check main keywords
if tbkeys == reftbkeys:
   print("table keywords are identical")
else:
    for ky in tbkeys:
        if ky in reftbkeys:
            if type(tbkeys[ky])==dict: 
                if 'value' in tbkeys[ky]:
                    if type(tbkeys[ky]['value'])==np.ndarray:
                        if not np.array_equal(tbkeys[ky]['value'], reftbkeys[ky]['value']):
                            print("keyword: {}, this tb:{}, ref:{}".format(ky, tbkeys[ky], reftbkeys[ky]))
                    else:
                        if tbkeys[ky]['value'] != reftbkeys[ky]['value']:
                            print("keyword: {}, this tb:{}, ref:{}".format(ky, \
                                                                           tbkeys[ky]['value'], reftbkeys[ky]['value']))
            elif tbkeys[ky] != reftbkeys[ky]:
                print("keyword: {}, this tb:{}, ref:{}".format(ky, tbkeys[ky], reftbkeys[ky]))
            else:
                pass
        else:
            print("keyword= {} is missing in ref tb".format(ky))
    missingkeys = [k for k in reftbkeys if not k in tbkeys]
    if missingkeys != []:
        print("keywords in ref missing in  this: ", missingkeys)
# check col keywords(units)           
if dcolkeys == refcolkeys:
    print("data col keywords are identical")
else:
    for ky in dcolkeys:
        if ky in refcolkeys:
            if type(dcolkeys[ky])==dict:
                if 'QuantumUnits' in dcolkeys[ky]:
                    if type(dcolkeys[ky]['QuantumUnits'])==np.ndarray:
                       if not np.array_equal(dcolkeys[ky]['QuantumUnits'], refcolkeys[ky]['QuantumUnits']):
                           print("colkeyword: {}, this tb:{}, ref:{}".format(ky, dcolkeys[ky], refcolkeys[ky]))
            elif dcolkeys[ky] != refcolkeys[ky]:
                print("colkeyword: {}, this tb:{}, ref:{}".format(ky, dcolkeys[ky], refcolkeys[ky])) 
        else:
            print("col keywoord= {} is missing in ref tb".format(ky))

tb.open(intab)
tb2.open(reftab)
 
for dcol in datacolnames:
    data = tb.getcol(dcol)
    refdata = tb2.getcol(dcol)
    print("----------\n")
    if np.array_equal(data,refdata): 
        print("{} matches exactly".format(dcol))
    elif np.allclose(data,refdata):
        print("{} matches within a tolerance".format(dcol))
    else:
        print("{} mismatch".format(dcol))
        print("shape: this = {}, ref = {}".format(data.shape, refdata.shape))
        print("this =", data)
        print("ref =", refdata)
        diffabs = abs(data-refdata)
        diffmaxindex = np.argmax(diffabs)
        diffmax = diffabs[diffmaxindex]
        print("max diff(abs(data-refdata)={}, frac. diff={}".format(diffmax, abs(diffmax/refdata[diffmaxindex])))
tb.done()
tb2.done()
