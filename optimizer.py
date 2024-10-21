import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# Given data
x = np.array([REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT])
y = np.array([REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT, REDACTED_DATA_POINT])

# Create an interpolation function
interp_func = interp1d(x, y, kind='cubic', fill_value="extrapolate")

# Define a function to maximize
def negative_function(x_val):
    return -interp_func(x_val)

# Use minimize_scalar to find the maximum
result = minimize_scalar(negative_function, bounds=(min(x), max(x)), method='bounded')

# Get the maximum value and the corresponding x
max_y = -result.fun
max_x = result.x

# We know that xs (the price sums) are 7p + 59, where p is the fri-sun room price
rp3 = (max_x - 59)/7 # fri-sun room price
rp1 = (rp3 + 17) # mon-wed room price
rp2 = (rp3 + 8) # thu room price

# Print the results
print(f"The maximum value of y is: {max_y} at x = {max_x}")
print(f"Optimal room prices:\nMonday: {rp1}\nTuesday: {rp1}\nWednesday: {rp1}\nThursday: {rp2}\nFriday: {rp3}\nSaturday: {rp3}\nSunday: {rp3}\n")
