#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Title: Testing Range and Temporal filter for LIDAR generated scans
Source File: lidarFilters.py
Created on February 29th 2020
@author: SaitejaPadakandla,saitejapadakandla2011@gmail.com
"""

import unittest
from lidarFilters import tempMedianFilter,rangeFilter,main



class TestProgram(unittest.TestCase):
	def test_lidar_filter(self):
		"""TEST ENTIRE PROGRAM-
		Running through both filter- Minimum,Maximum and Median"""
		# the input and output given in the question
		min, max = 0, 10
		d = 3
		values = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]]
		self.assertEqual(tempMedianFilter(rangeFilter(values, min, max), d),[[0.0, 1.0, 2.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0], [1.0, 3.0, 4.0, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 3.0], [3.0, 3.0, 4.0, 1.0, 0.0]])


class TestFilter(unittest.TestCase):
	def test_min_max(self):
		"""TEST MIN-MAX FILTER-
		Running through min max filter and replacing with min max values"""
		min = 0.03
		max = 5
		values = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
		self.assertEqual(rangeFilter(values,min,max),[[0.03, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 5, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 0.03], [3.0, 3.0, 3.0, 1.0, 3.0], [5, 2.0, 4.0, 0.03, 0.03]])

	def test_temporal_median_filter(self):
		"""TEST MEDIAN FILTER 2-
		Running through temp median filter and finding the median with the previous scans with respect to d criteria"""
		values = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
		self.assertEqual(tempMedianFilter(values, 3), [[0.0, 1.0, 2.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0], [1.0, 3.0, 4.0, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 3.0], [3.0, 3.0, 4.0, 1.0, 0.0]])


class TestErrorValue(unittest.TestCase):
	def test_varied_scans(self):
		"""TEST ERROR VALUES-
		Enter values with different length of scans"""
		min, max = 0, 10
		values = [[0., 1., 2.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3.],
				[10., 2., 4., 0., 0.]]
		self.assertRaises(TypeError,(rangeFilter(values, min, max)))


if __name__ == '__main__':
	main()
	unittest.main(exit=False, verbosity=2)

