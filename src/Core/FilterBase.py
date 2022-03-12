import FilterABC
import numpy as np


class filterBase(FilterABC.FilterABC):
    def __init__(self, img, kernel: int, stride: int, padding: int) -> None:
        self.img = img
        self.kernel = kernel
        self.stride = stride
        self.padding = padding
        self.smoothCriminal = []
        self.outputDims = None

        self._input_checks()
        self._set_output_dims()

        if self.padding > 0:
            self._pad_image()

    def _input_checks(self):
        assert type(self.kernel) is int
        assert type(self.stride) is int
        assert type(self.padding) is int

        if self.kernel < 1 or self.stride < 1 or self.padding < 0:
            print("kernel/stride must be >= 0: padding must be >= 0")
            raise ValueError

    def _convert_to_numpy_array(self):
        # O(n)
        self.smoothCriminal = np.array(self.smoothCriminal)

    def _reshape_numpy_array(self):
        self.smoothCriminal = self.smoothCriminal.reshape(
            self.outputDims[0], self.outputDims[1]
        )

    def _pad_image(self):
        self.img = np.pad(self.img, pad_width=self.padding, mode="constant")

    def _set_output_dims(self):
        self.outputDims = [
            int((v - self.kernel + 2 * self.padding) / (self.stride)) + 1
            for v in self.img.shape
        ]
