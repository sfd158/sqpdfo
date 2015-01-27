# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 11:22:07 2014

@author: jaco_da
"""

import unittest
from sqplab_bfgs import *
import numpy as np
import helper

class dummyInfo():
	def __init__(self):
		self.g = matlabarray([  -0.009783923878659,  1.000000000000000, 0.0]).T
		self.ai = matlabarray([])
		self.ae = matlabarray([[1.000000000000000,   0.999999999999999,   1.000000000000000],
   [1.000000000000000,   1.999999999999999,   3.000000000000000]])
		self.hl = matlabarray([])
		self.niter = 1
		self.flag = 0
		self.nsimul = matlabarray([0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		self.ci = matlabarray([])
		self.ce = matlabarray([0.312467441560872, -0.056489622187450]).T
		self.f = 0.099563123926544
		self.glag = matlabarray([-0.333333333013890,  0.666666666736111, -0.333333333513889]).T
		self.glagn = 0.666666666736111
		self.feasn = 3
		self.compl = 0

class Test_sqplab_bfgs(unittest.TestCase):

	def setUp(self):
		self.M = matlabarray(np.eye(3))
		self.y = matlabarray([-0.009783923878659,  -0.0, 0.0]).T
		self.s = matlabarray([-0.503054026564966,  -1.0, -0.184478531874161]).T
		self.first = 1
		
		self.info = dummyInfo()
		self.options = helper.dummyOptions()
		#set hessian approximation to bfgs
		self.options.hess_approx = 130
		self.values = helper.dummyValues()
		

	def test_sqplab_bfgs_null_step(self):
		self.s = matlabarray(np.zeros(3))
		_, _, info, values = sqplab_bfgs_(self.M,self.y,self.s,first=self.first,info=self.info,options=self.options,values=self.values)
		
		self.assertEqual(info.flag, values.fail_strange)
		
	def test_sqplab_bfgs_negative_definite(self):
		#self.M = matlabarray([[1,2,3],[2,1,2],[3,2,1]])
		self.M = matlabarray(-np.eye(3))
		#print "M", self.M
		#self.s = matlabarray([1.0,1.0])
		_, _, info, values = sqplab_bfgs_(self.M,self.y,self.s,first=self.first,info=self.info,options=self.options,values=self.values)
				
		self.assertEqual(info.flag, values.fail_strange)
	
	def test_sqplab_bfgs_test(self):
		M, _, info, values = sqplab_bfgs_(self.M,self.y,self.s,first=self.first,info=self.info,options=self.options,values=self.values)
		#print "M:\n", M
		correctM = matlabarray([[0.205243860649550,   0.003553460424288,   0.000655537162145],
   [0.003553460424288,   0.195307727402361,  -0.000901167227317],
   [0.000655537162145,  -0.000901167227317,   0.200026425015353]])
			
		#print "correctM:\n",correctM
		#print "-:\n", 
		#self.assertEqual(M, correctM)
		self.assertTrue((abs(correctM - M) < 1e-15).all())
if __name__ == '__main__':
	unittest.main()