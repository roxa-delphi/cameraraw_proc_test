import rawpy

raw = rawpy.imread('IMGP0243.PEF')

print("black_level_per_channel")
print(raw.black_level_per_channel)

print("camera_whitebalance")
print(raw.camera_whitebalance)

print("color_desc")
print(raw.color_desc)

print("color_matrix")
print(raw.color_matrix)

print("daylight_whitebalance")
print(raw.daylight_whitebalance)

print("num_colors")
print(raw.num_colors)

print("raw_colors")
print(raw.raw_colors)

print("raw_image_visible")
print(raw.raw_image_visible)

print("raw_pattern")
print(raw.raw_pattern)

print("raw_type")
print(raw.raw_type)

print("rgb_xyz_matrix")
print(raw.rgb_xyz_matrix)

print("sizes")
print(raw.sizes)

print("tone_curve")
print(raw.tone_curve)



