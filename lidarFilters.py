#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Title: Range and Temporal filter for LIDAR generated scans
Created on Tue Feb  28 17:42:55 2020
@author: Saiteja Padakandla, saitejapadakandla2011@gmail.com
"""

import statistics


def lengthCheck(scan):
	""" Length Filter: Validate the length of the first value if it satisfies the necessary conditions"""
	return exit() if (len(scan[0]) < 3 or len(scan[0]) > 10) else scan


def rangeFilter(scans,minimum,maximum):
	"""	MinMax Filter- If values are less than Minimum , replace the values with the Minimum and the same way for maximum"""
	return [[min(max(value, minimum), maximum) for value in scan] for scan in scans]#List Comprehension


def tempMedianFilter(scans, d):
	""" Temporal Median Filter-Median of the elements by comparing it to the previous d scans"""
	result = []
	for current in range(len(scans)):
		medians = []
		try:
			for previousIndex in range(len(scans[current])):
				medians.append(statistics.median([scan[previousIndex]
					for scan in scans[max(-1, current - d) + 1: current + 1]]))
		except IndexError as err:#	ERROR HANDLING: try catch used if varied number of values are entered in scan
			print(err)
			exit()  # comment this line if u still want the values with varied scans
		result.append(medians)
	return result

def main():
    """Execution steps : 
    . Set the values of min max
	. Pass the values of scans and d
	. Print the output"""
    
    minimum, maximum = 0.03, 5  # assign max and min values - Step 1 accomplished.
    
    # inputs and filter size
    d, big = 3, [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
    
    # calling functions and error handling for varied scan lengths
    filter1Value = rangeFilter(big, minimum, maximum)
    filter2Value = list(tempMedianFilter(filter1Value, d+1))
    
    # print the values and error handling
    print("input", big, "\n""after_MixMax_filter", filter1Value, "\n""After_temp_median:", filter2Value)


if __name__ == '__main__':
    main()
	