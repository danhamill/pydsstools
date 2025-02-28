'''
Write regular time-series data to example.dss
'''
import numpy as np
from datetime import datetime
from pydsstools.heclib.dss import HecDss
from pydsstools.core import TimeSeriesContainer

dss_file = "example.dss"

tsc = TimeSeriesContainer()
tsc.granularity_value = 60 #seconds i.e. minute granularity
tsc.numberValues = 10
tsc.startDateTime=datetime.now().strftime('%d %b %Y %H:00')
tsc.pathname = "/REGULAR/TIMESERIES/FLOW//1HOUR/WRITE2/"
tsc.units = "cfs"
tsc.type = "INST"
tsc.interval = 1
#must a +ve integer for regular time-series
#actual interval implied from E part of pathname
tsc.values =np.array(range(10),dtype=np.float32)
#values may be list,array, numpy array

fid = HecDss.Open(dss_file)
fid.deletePathname(tsc.pathname)
status = fid.put(tsc)
fid.close()
