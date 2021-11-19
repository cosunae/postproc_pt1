from dataset import open_datasets
import xarray as xr

dss = open_datasets('/code/grib_files/cosmo-eu/lfff00000000_2014010400.gb2',
                    backend_kwargs={'filter_by_keys': {'typeOfLevel': 'generalVerticalLayer'}})
t = dss[0]['t']
q = dss[0]['q']
QI = dss[0]['QI']

u = dss[1]['u']

ll = t+q
k = t
if xr.DataArray.all(k == ll):
    print("EQUAL")
else:
    print("NOT EQUAL")
