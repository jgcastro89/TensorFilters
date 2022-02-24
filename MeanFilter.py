import numpy as np
from FilterBase import FilterBase

class mean_filter(filterBase):
    def __init__(self, img, kernel:int, stride:int, padding:int) -> None:
        self._input_checks(kernel, stride, padding)
        self._set_output_dims(kernel, stride, padding) 

        self.img = img
        self.kernel = kernel
        self.stride = stride
        self.padding = padding
        
        if padding > 0:
            self._pad_image()
        
        self.smoothCriminal = []
        
        self._mean()
        self._convert_to_numpy_array()
        self._reshape_numpy_array()
            
    def _mean(self):
        # O(n*m)
        for i in range(0, self.img.shape[0], self.stride):
            for j in range(0, self.img.shape[1], self.stride):
                temp = self.img[i:i+self.kernel, j:j+self.kernel]
                if temp.size == self.kernel**2:
                    # O(1)
                    self.smoothCriminal.append(np.mean(temp))