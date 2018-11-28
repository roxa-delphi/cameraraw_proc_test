import rawpy
import numpy as np
import imageio

raw = rawpy.imread('IMGP0243.PEF')

h,w = raw.sizes.raw_height, raw.sizes.raw_width
raw_image = raw.raw_image.copy()
raw_array = np.array(raw_image).reshape((h,w)).astype('float')


outimg = raw_array
outimg[outimg < 0] = 0
outimg = outimg * 255
imageio.imwrite("try1.png", outimg.astype('uint8'))

