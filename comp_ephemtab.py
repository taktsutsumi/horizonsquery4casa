import numpy as np
objectname='Mars'
mjdstr='59214-62866dUTC'
ephemdir='/home/casa/data/trunk/ephemerides/JPL-Horizons/'
tabname = objectname+'_'+mjdstr+'_J2000.tab'
reftab=ephemdir+tabname


intab = objectname+'_'+mjdstr+'_new.tab'

tb.open(intab)
tbkeys = tb.getkeywords()
datacolnames = tb.colnames()
tb.done()

tb.open(reftab)
reftbkeys = tb.getkeywords()
refdatacolnames = tb.colnames()
tb.done()
print("reftbkeys=",reftbkeys)
if tbkeys == reftbkeys:
   print("table keywords is identical")
else:
   for ky in tbkeys:
       if ky in reftbkeys:
           if type(tbkeys[ky])==dict: 
               if 'value' in tbkeys[ky]:
                  if type(tbkeys[ky]['value'])==np.ndarray:
                      if not np.array_equal(tbkeys[ky]['value'], reftbkeys[ky]['value']):
                          print("keyword: {}, this tb:{}, ref {}".format(ky, tbkeys[ky], reftbkeys[ky]))
           elif tbkeys[ky] != reftbkeys[ky]:
               print("keyword: {}, this tb:{}, ref {}".format(ky, tbkeys[ky], reftbkeys[ky]))
           else:
               pass
       else:
           print("keyword= {} is missing in ref tb".format(ky))
           

