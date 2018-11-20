# This program creates a histogram from data stored in a csv file and saves it as a png image.

# The data file must be one column of numbers - no column labels, etc.
# It must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
# It must be saved in the same folder as this program.
# See the file sample_histogram_data.csv for reference.

# In the next line, replace sample_histogram_data.csv with the filename of your data:
data_filename = 'sample_histogram_data.csv'

# In the next line, replace histogram with the filename you wish to save as:
output_filename = 'histogram.png'

# Use the next line to set figure height and width (experiment to check the scale):
figure_width, figure_height = 7,7

# These two lines import modules of additional python functions that will be necessary:
import matplotlib.pyplot as plt
import numpy as np

# This line imports the data:
data = np.genfromtxt(data_filename)

# If there are errors importing the data, you can also copy the data in as a list.
# e.g. data = [1.95878982, 2.59203983, 1.22704688, ...]

# This line creates the figure. 
plt.figure(figsize=(figure_width,figure_height))

# Uncomment the next four lines to set the axis limits (otherwise they will be set automatically):
# x_axis_min, x_axis_max = 0.95,4.05
# y_axis_min, y_axis_max = 4.05
# plt.xlim([x_axis_min,x_axis_max])
# plt.ylim([y_axis_min,y_axis_max])

# This next parameter controls how the data is binned.
# Either set it as a particular value (e.g. bin_info = 6)...
# ... for Python to create a number of evenly spaced bins (from the min to the max data points)...
# Or set a list of bin endpoints (e.g. bin_info = [1.0,1.5,2.0,2.5,3.0,3.5,4.0])...
# Or set bin_info = None for Python to set the bins however it thinks best.
bin_info = [1.0,1.5,2.0,2.5,3.0,3.5,4.0]

# The next lines create and save the plot:
plt.hist(data,bins=bin_info)
plt.savefig(output_filename)