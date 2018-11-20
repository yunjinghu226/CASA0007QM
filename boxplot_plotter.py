# This program creates a boxplot from data stored in a csv file and saves it as a png image.

# The data file must be one column of numbers - no column labels, etc.
# It must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
# It must be saved in the same folder as this program.
# See the file sample_boxplot_data.csv for reference.

# In the next line, replace sample_boxplot_data.csv with the filename of your data:
data_filename = 'sample_boxplot_data.csv'

# In the next line, replace boxplot with the filename you wish to save as:
output_filename = 'boxplot.png'

# Use the next line to set figure height and width (experiment to check the scale):
figure_width, figure_height = 4,10

# You can ignore these two lines:
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(data_filename)

# If there are errors importing the data, you can also copy the data in as a list.
# e.g. data = [1.95878982, 2.59203983, 1.22704688, ...]

# This line creates the figure. 
plt.figure(figsize=(figure_width,figure_height))

# Uncomment the next three lines to set the axis limits (otherwise they will be set automatically):
#axis_min = 0.95
#axis_max = 4.05
#plt.ylim([axis_min,axis_max])

# The next lines create and save the plot:
plt.xlim([0.75,1.25])
plt.xticks([])
plt.boxplot(data,manage_xticks=False)
plt.savefig(output_filename)