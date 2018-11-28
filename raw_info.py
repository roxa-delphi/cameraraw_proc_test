import rawpy

raw = rawpy.imread('IMGP0243.PEF')

print(raw.black_level_per_channel)
print(raw.camera_whitebalance)
print(raw.color_desc)
print(raw.color_matrix)
print(raw.daylight_whitebalance)
print(raw.num_colors)
print(raw.raw_colors)
print(raw.raw_image_visible)
print(raw.raw_pattern)
print(raw.raw_type)
print(raw.rgb_xyz_matrix)
print(raw.sizes)
print(raw.tone_curve)



