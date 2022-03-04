import numpy as np
from FilterBase import filterBase

class mean_filter(filterBase):
    def __init__(self, img, kernel:int, stride:int, padding:int) -> None:
        self._input_checks(kernel, stride, padding)

        self.img = img

        self._set_output_dims(kernel, stride, padding) 

        self.kernel = kernel
        self.stride = stride
        self.padding = padding
        
        if padding > 0:
            self._pad_image()
        
        self.smoothCriminal = []
        
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
                    self.smoothCriminal.append(np.mean(temp))

img = np.random.rand(768,1024)                    
av_filter = mean_filter(img, kernel=4, stride=4, padding=0)
print(av_filter.smoothCriminal.shape)