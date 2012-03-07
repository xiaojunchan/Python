#	This program reads in the 

import sys
from numpy import NaN, Inf, arange, isscalar, asarray

if __name__=="__main__":
    series = [0,0,0,2,0,0,0,-2,0,0,0,2,0,0,0,-2,0]
    print peakdet(series,1)