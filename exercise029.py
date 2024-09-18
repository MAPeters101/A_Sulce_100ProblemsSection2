import math

def calc_vol_in_sphere(height, radius=10):
    cap_height = 2*radius - height
    cap_height_vol = (math.pi * cap_height**2 * (3*radius - cap_height)) / 3
    volume = (4 * math.pi * radius**3)/3 - cap_height_vol
    return volume

print(calc_vol_in_sphere(2))