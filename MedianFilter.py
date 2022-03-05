import numpy as np
from FilterBase import filterBase

class median_filter(filterBase):
    def __init__(self, img, kernel:int, stride:int, padding:int) -> None:
        super().__init__(img, kernel, stride, padding)

        self._execute()
        self._convert_to_numpy_array()
        self._reshape_numpy_array()
            
    def _execute(self):
        # O(n*m)
        for i in range(0, self.img.shape[0], self.stride):
            for j in range(0, self.img.shape[1], self.stride):
                temp = self.img[i:i+self.kernel, j:j+self.kernel]
                if temp.size == self.kernel**2:
                    # O(1)
                    self.smoothCriminal.append(np.median(temp))