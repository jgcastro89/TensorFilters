from abc import ABC
from abc import abstractmethod


class FilterABC(ABC):
    @abstractmethod
    def _input_checks(self):
        pass

    @abstractmethod
    def _convert_to_numpy_array(self):
        pass

    @abstractmethod
    def _reshape_numpy_array(self):
        pass

    @abstractmethod
    def _pad_image(self):
        pass

    @abstractmethod
    def _execute(self):
        pass
