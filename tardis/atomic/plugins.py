from abc import ABCMeta, abstractmethod, abstractproperty
import pandas as pd


class BaseAtomicDataType(object):
    __metaclass__ = ABCMeta

    _value = None

    @abstractproperty
    def hdf_name(self):
        raise NotImplementedError


    @abstractmethod
    def load_hdf(self, hdf_store):
        self._value = self.hdf_name[self.hdf_name]

    @property
    def value(self):
        if self._value is None:
            raise ValueError('{0} is not available please load first'.format(
                self.__class__.__name__))
        else:
            return self._value

    def save_hdf(self, hdf_store):
        hdf_store.put(self.hdf_name, self._value, format='table',
                      data_columns=True)


    @property
    def name(self):
        return getattr(self, '_name', self.hdf_name)


class Atoms(BaseAtomicDataType):
    hdf_name = 'atoms'


class Ions(BaseAtomicDataType):
    hdf_name = 'ions'

class Levels(BaseAtomicDataType):
    hdf_name = 'levels'

class Lines(BaseAtomicDataType):
    hdf_name = 'lines'