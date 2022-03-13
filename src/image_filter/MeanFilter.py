import numpy as np
from filter_core.FilterBase import FilterBase


class MeanFilter(FilterBase):
    """_summary_

    Args:
        FilterBase (_type_): _description_
    """

    def __init__(self, img: np.array, kernel: int, stride: int, padding: int) -> None:
        """_summary_

        Args:
            img (np.array): _description_
            kernel (int): _description_
            stride (int): _description_
            padding (int): _description_
        """
        super().__init__(img=img, kernel=kernel, stride=stride, padding=padding)

        self._execute()
        self._convert_to_numpy_array()
        self._reshape_numpy_array()

    def _execute(self):
        # O(n*m)
        for i in range(0, self.img.shape[0], self.stride):
            for j in range(0, self.img.shape[1], self.stride):
                temp = self.img[i : i + self.kernel, j : j + self.kernel]
                if temp.size == self.kernel ** 2:
                    # O(1)
                    self.smoothCriminal.append(np.mean(temp))
