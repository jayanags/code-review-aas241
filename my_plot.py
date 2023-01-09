import numpy as np
import matplotlib.pyplot as pyplot
import os
from astropy.io import fits
import glob
data = fits.getdata('../M100.mom0.fits')
print(np.shape(data))
xlen,ylen = np.shape(data)[0], np.shape(data)[1]
col1 = data[xlen-1, :]
col2 = data[ylen-1, :]
col3 = data[ylen-1, :]
pyplot.figure()
pyplot.plot(np.arange(67), col1)
mean = np.mean(col1)
pyplot.axhline(mean)
pyplot.legend(['Column 20', 'Mean'])
pyplot.title('Plot of Column 20 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.figure()
pyplot.plot(np.arange(67), col2)
mean = np.mean(col2)
pyplot.axhline(mean)
pyplot.legend(['Column 200', 'Mean'])
pyplot.title('Plot of Column 200 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.figure()
pyplot.plot(np.arange(67), col3)
mean = np.mean(col3)
pyplot.axhline(mean)
pyplot.legend(['Column 800', 'Mean'])
pyplot.title('Plot of Column 800 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.show()
