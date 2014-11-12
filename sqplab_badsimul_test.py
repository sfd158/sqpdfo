# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 15:17:32 2014

@author: jaco_da
"""

import unittest
from sqplab_badsimul import *
#import numpy as np
import helper

class dummyInfo():
	def __init__(self):
		self.flag = False

class Test_sqplab_badsimul(unittest.TestCase):

	def setUp(self):
		self.dummyOptions = helper.dummyOptions()
		self.dummyInfo = dummyInfo()
		self.dummyValues = helper.dummyValues()

	def test_sqplab_bad_simul1(self):
		self.dummyValues.stop_on_simul = True
		self.dummyInfo = sqplab_badsimul_(outdic=2,info=self.dummyInfo,options=self.dummyOptions,values=self.dummyValues)
		
		print self.dummyInfo.flag
		self.assertTrue(self.dummyInfo.flag)
	
	def test_sqplab_bad_simul2(self):
		self.dummyValues.fail_on_simul = True
		self.dummyInfo = sqplab_badsimul_(outdic=3,info=self.dummyInfo,options=self.dummyOptions,values=self.dummyValues)
		
		print self.dummyInfo.flag
		self.assertTrue(self.dummyInfo.flag)


if __name__ == '__main__':
	unittest.main()