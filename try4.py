import rawpy
import numpy as np
import imageio

print("...reading")
raw = rawpy.imread('IMGP0243.PEF')

h,w = raw.sizes.raw_height, raw.sizes.raw_width
raw_image = raw.raw_image.copy()
raw_array = np.array(raw_image).reshape((h,w)).astype('float')

print("...black_level")
bayer_pattern = raw.raw_pattern
blc = raw.black_level_per_channel
blc_raw = raw_array.copy()
for y in range(0, h, 2):
  for x in range(0, w, 2):
    blc_raw[y+0, x+0] -= blc[bayer_pattern[0,0]]
    blc_raw[y+0, x+1] -= blc[bayer_pattern[0,1]]
    blc_raw[y+1, x+0] -= blc[bayer_pattern[1,0]]
    blc_raw[y+1, x+1] -= blc[bayer_pattern[1,1]]
 
print("...demosaic")
dms_img = np.zeros((h//2, w//2, 3))
for y in range(0, h, 2):
  for x in range(0, w, 2):
    colors = [0, 0, 0, 0]
    colors[bayer_pattern[0,0]] += blc_raw[y+0, x+0]
    colors[bayer_pattern[0,1]] += blc_raw[y+0, x+1]
    colors[bayer_pattern[1,0]] += blc_raw[y+1, x+0]
    colors[bayer_pattern[1,1]] += blc_raw[y+1, x+1]
    dms_img[y // 2, x // 2, 0] = colors[0]
    dms_img[y // 2, x // 2, 1] = (colors[1] + colors[3]) / 2
    dms_img[y // 2, x // 2, 2] = colors[2]

print("...wthitebalance")
wb = np.array(raw.camera_whitebalance)
img_wb = dms_img.copy().flatten().reshape((-1,3))
for index, pixel in enumerate(img_wb):
  pixel = pixel * wb[:3] / max(wb)
  img_wb[index] = pixel

print("...output")
#outimg = dms_img
outimg = img_wb.copy().reshape((h // 2, w // 2, 3))
outimg[outimg < 0] = 0
outimg = outimg / outimg.max()
outimg = outimg * 255
imageio.imwrite("try4.png", outimg.astype('uint8'))

