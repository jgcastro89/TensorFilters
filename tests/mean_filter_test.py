import numpy as np
from ImageFilter import MeanFilter

img = np.random.rand(768, 1024)
av_filter = MeanFilter(img, kernel=4, stride=4, padding=0)
print(av_filter.smoothCriminal.shape)
