import rawpy
import numpy as np
import imageio
import math

print("reading...")
raw = rawpy.imread('IMGP0243.PEF')

h,w = raw.sizes.raw_height, raw.sizes.raw_width
raw_image = raw.raw_image.copy()
raw_array = np.array(raw_image).reshape((h,w)).astype('float')

print("black_level...")
bayer_pattern = raw.raw_pattern
blc = raw.black_level_per_channel
blc_raw = raw_array.copy()
for y in range(0, h, 2):
  for x in range(0, w, 2):
    blc_raw[y+0, x+0] -= blc[bayer_pattern[0,0]]
    blc_raw[y+0, x+1] -= blc[bayer_pattern[0,1]]
    blc_raw[y+1, x+0] -= blc[bayer_pattern[1,0]]
    blc_raw[y+1, x+1] -= blc[bayer_pattern[1,1]]
 
print("demosaic...")
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

print("wthitebalance...")
wb = np.array(raw.camera_whitebalance)
#img_wb = dms_img.copy().flatten().reshape((-1,3))
#for index, pixel in enumerate(img_wb):
#  #pixel = pixel * wb[:3] / max(wb)
#  pixel = pixel * wb[:3] / wb[3]
#  img_wb[index] = pixel
#img_wb = img_wb.copy().reshape((h // 2, w // 2, 3))
ratio_r = wb[0] / wb[3]
ratio_g = wb[1] / wb[3]
ratio_b = wb[2] / wb[3]
img_wb = dms_img.copy()
for y in range(0, h // 2):
  for x in range(0, w // 2):
    img_wb[y, x, 0] *= ratio_r
    img_wb[y, x, 1] *= ratio_g
    img_wb[y, x, 2] *= ratio_b

print("color_matrix...")
color_matrix = raw.rgb_xyz_matrix[:3][0:3]
img_ccm = img_wb.copy().reshape((-1,3))
for index, pixel in enumerate(img_ccm):
  pixel = np.dot(color_matrix, pixel)
  img_ccm[index] = pixel

print("gamma...")
#img_gamma = img_wb.copy().flatten()
img_gamma = img_ccm.copy().flatten()
img_gamma[img_gamma < 0] = 0
img_gamma = img_gamma / img_gamma.max()
for index, val in enumerate(img_gamma):
  img_gamma[index] = math.pow(val, 1/2.2)
img_gamma = img_gamma = img_gamma.reshape((h//2, w//2, 3))

print("output...")
#outimg = dms_img
#outimg = img_wb
outimg = img_gamma
outimg[outimg < 0] = 0
outimg = outimg / outimg.max()
outimg = outimg * 255
imageio.imwrite("try6.png", outimg.astype('uint8'))

