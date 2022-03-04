import FilterABC
import numpy as np

class filterBase(FilterABC.FilterABC):
    def __init__(self) -> None:
        self.img = None
        self.padding = None
        self.outputDims = None
        self.smoothCriminal = None
        
    def _input_checks(self, kernel, stride, padding):
        assert type(kernel) is int
        assert type(stride) is int
        assert type(padding) is int

        if kernel < 1 or stride < 1 or padding < 0:
            print("kernel/stride must be >= 0: padding must be > 0")
            raise ValueError
    
    def _convert_to_numpy_array(self):
        # O(n)
        self.smoothCriminal = np.array(self.smoothCriminal)
    
    def _reshape_numpy_array(self):
        self.smoothCriminal = self.smoothCriminal.reshape(self.outputDims[0], self.outputDims[1])
        
    def _pad_image(self):
        self.img = np.pad(self.img, pad_width=self.padding, mode='constant')
        
    def _set_output_dims(self, kernel, stride, padding):
        self.outputDims =[int((v - kernel + 2*padding)/(stride)) + 1 for v in self.img.shape]