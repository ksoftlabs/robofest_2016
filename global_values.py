import numpy as np

# Hue ranges
red_lower1 = 0
red_upper1 = 10
red_lower2 = 170
red_upper2 = 180
green_lower = 80
green_upper = 160
blue_lower = 160
blue_upper = 260

# Saturation ranges
lower_saturation = 50
upper_saturation = 255

# Value (brightness) ranges
lower_value = 50
upper_value = 255

# Masks
# Red 1
lower_red1 = np.array([red_lower1, lower_saturation, lower_value])
upper_red1 = np.array([red_upper1, upper_saturation, upper_value])
# Red 2
lower_red2 = np.array([red_lower2, lower_saturation, lower_value])
upper_red2 = np.array([red_upper2, upper_saturation, upper_value])
# Green
lower_green = np.array([green_lower, lower_saturation, lower_value])
upper_green = np.array([green_upper, upper_saturation, upper_value])
# Blue
lower_blue = np.array([blue_lower, lower_saturation, lower_value])
upper_blue = np.array([blue_upper, upper_saturation, upper_value])




