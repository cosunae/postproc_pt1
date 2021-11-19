
import cfgrib
import xarray as xr
from pint import UnitRegistry


class DataArray(xr.DataArray):
    __slots__ = []

    def check(self, other):
        if self.units != other.units:
            raise RuntimeError(
                "dimensions for {selfname}: {unitself} and {othername}: {unitother} are not compatible".format(
                    selfname=self.name, unitself=self.units, othername=other.name, unitother=other.units))

    def __add__(self, other):
        self.check(other)
        return super().__add__(other)

    def __sub__(self, other):
        self.check(other)
        return super().__sub__(other)


class Dataset(xr.Dataset):
    __slots__ = []

    def __getitem__(self, key):
        obj = super().__getitem__(key)
        obj.__class__ = DataArray
        return obj


def open_datasets(path, backend_kwargs={}, **kwargs):

    ureg = UnitRegistry()
    dss = cfgrib.open_datasets(path, backend_kwargs=backend_kwargs, **kwargs)
    for ds in dss:
        for v, vv in ds.items():
            vv.attrs['units'] = vv.units.replace('kg-1', 'kg**-1')
            vv.attrs['units'] = ureg(vv.units)

    for a in dss:
        a.__class__ = Dataset
    return dss
