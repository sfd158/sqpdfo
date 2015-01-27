# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 11:47:43 2014
INPUT VALUES

simul = 

    @evalfgh


x =

  -0.003054026564966
                   0
   0.315521468125839


null_step =

     0


constrained_pbl =

     2


lm =

                   0
  -0.999999999499998
                   0
  -0.000000000375002
   0.000000000083334


M =

     1     0     0
     0     1     0
     0     0     1


n =

     3


me =

     2


mi =

     0


s =

  -0.503054026564966
  -1.000000000000000
  -0.184478531874161


gx =

  -0.009783923878659
   1.000000000000000
                   0


gci =

     []


gce =

   1.000000000000000   0.999999999999999   1.000000000000000
   1.000000000000000   1.999999999999999   3.000000000000000


info = 

         g: [3x1 double]
        ai: []
        ae: [2x3 double]
        hl: []
     niter: 1
      flag: 0
    nsimul: [0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        ci: []
        ce: [2x1 double]
         f: 0.099563123926544
      glag: [3x1 double]
     glagn: 0.666666666736111
     feasn: 3
     compl: 0



K>> info.g

ans =

     0
     1
     0

K>> info.ae

ans =

     1     1     1
     1     2     3

K>> info.ce

ans =

   0.312467441560872
  -0.056489622187450

K>> info.glag

ans =

  -0.333333333013890
   0.666666666736111
  -0.333333333513889


options = 

           algo_method: 101
    algo_globalization: 112
           hess_approx: 131
          bfgs_restart: 0
          algo_descent: 120
                   tol: [1.000000000000000e-05 1.000000000000000e-05 1.000000000000000e-05]
                 dxmin: 1.000000000000000e-06
                 miter: 500
                msimul: 500
               verbose: 2
                  fout: 1
                   inf: Inf
                   df1: 0


values = 

                       success: 0
              fail_on_argument: 1
               fail_on_problem: 2
                 fail_on_simul: 3
                 stop_on_simul: 4
              stop_on_max_iter: 5
             stop_on_max_simul: 6
                 stop_on_dxmin: 7
          fail_on_non_decrease: 8
            fail_on_ascent_dir: 9
           fail_on_max_ls_iter: 10
              fail_on_ill_cond: 11
    stop_on_small_trust_region: 15
             fail_on_null_step: 20
         fail_on_infeasible_QP: 21
          fail_on_unbounded_QP: 22
                  fail_strange: 99
                    nsimultype: 16
                max_null_steps: 1
                        newton: 100
                  quasi_newton: 101
            cheap_quasi_newton: 102
                 unit_stepsize: 110
                    linesearch: 111
                 trust_regions: 112
                        powell: 120
                         wolfe: 121
                          bfgs: 130
                         model: 131
                         dline: '--------------------------------------------------------------------------------------'
                         eline: '======================================================================================'
                         sline: '**************************************************************************************'


fcmodel =

   0.099563123926544  -0.013550429460611   1.384968815034240                   0   6.144976749236061
   0.312467441560872   1.384968815034241   1.384968815034240   1.384968815034241   0.000000000000006
  -0.056489622187450   1.384968815034241   2.769937630068480   4.154906445102721   0.000000000000014


Y =

  -0.003054026564966  -0.500000000000000   0.500000000000000   0.500000000000000   0.500000000000000
                   0   1.000000000000000                   0   1.000000000000000   1.000000000000000
   0.315521468125839   0.500000000000000   0.500000000000000  -0.500000000000000   0.500000000000000


fY =

   0.099563123926544   1.500000000000000   0.500000000000000   1.500000000000000   1.500000000000000


ciY =

     []


ceY =

   0.312467441560872   1.000000000000000   1.000000000000000   1.000000000000000   2.000000000000000
  -0.056489622187450   2.000000000000000   1.000000000000000                   0   3.000000000000000


sigma =

     1


scale =

   1.000000000000000
   0.722037918214987
   0.722037918214987
   0.722037918214987
   0.521338755340232


shift_Y =

     1


QZ =

   1.000000000000000                   0                   0                   0                   0
                   0  -0.437717028004984  -0.826365739060244   0.329535025867438  -0.130115853870500
                   0   0.880814115424577  -0.315023389192614   0.329471408091712  -0.127966204837389
                   0   0.162491294867564  -0.418566952172131  -0.884320607054428  -0.127966204837389
                   0   0.078529462977709  -0.206595343893201  -0.028849989870035   0.974843149132506


RZ =

   1.000000000000000   1.000000000000000   1.000000000000000   1.000000000000000   1.000000000000000
                   0   0.819739267991799  -0.132165180682231   0.386491133279071   0.503816009553305
                   0                   0  -0.369537503265736  -0.294775124607443  -0.596996335387400
                   0                   0                   0   0.876403859762092   0.237890849609900
                   0                   0                   0                   0  -0.092396452142661


whichmodel =

     0


ind_Y =

     5     2     3     4     1


i_xbest =

     5


m =

     5
					
OUPUT VALUES:

K>> M,pc,info

M =

   2.620301230585867                   0                   0
                   0                   0                   0
                   0                   0                   0


pc =

     1


info = 

         g: [3x1 double]
        ai: []
        ae: [2x3 double]
        hl: []
     niter: 1
      flag: 0
    nsimul: [0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        ci: []
        ce: [2x1 double]
         f: 0.099563123926544
      glag: [3x1 double]
     glagn: 0.666666666736111
     feasn: 3
     compl: 0

K>> info.g

ans =

  -0.009783923878659
   1.000000000000000
                   0

K>> info.ae

ans =

   1.000000000000000   0.999999999999999   1.000000000000000
   1.000000000000000   1.999999999999999   3.000000000000000

K>> info.ce

ans =

   0.312467441560872
  -0.056489622187450

K>> info.glag

ans =

  -0.333333333013890
   0.666666666736111
  -0.333333333513889					
@author: jaco_da
"""

import unittest
from ecdfo_computeHessian import *
from evalfgh import *
#import numpy as np
import helper

class dummyInfo():
	def __init__(self):
		self.g  = matlabarray([ 0, 1, 0]).T
		self.ai = matlabarray( [])
		self.ae = matlabarray([[1,     1,     1],[1,     2,     3]])
		self.hl = matlabarray( [])
		self.niter = 1
		self.flag = 0
		self.nsimul = matlabarray( [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		self.ci = matlabarray( [])
		self.ce = matlabarray([0.312467441560872, -0.056489622187450]).T
		self.f = 0.099563123926544
		self.glag = matlabarray([-0.333333333013890, 0.666666666736111,-0.333333333513889]).T
		self.glagn =  0.666666666736111
		self.feasn = 3
		self.compl = 0
		
class Test_ecdfo_computeHessian(unittest.TestCase):

	def setUp(self):
		self.simul = evalfgh_
		self.x = matlabarray([-0.003054026564966, 0, 0.315521468125839]).T
		self.null_step = 0
		self.constrained_pbl = 2
		self.lm = matlabarray([0, -0.999999999499998, 0,-0.000000000375002, 0.000000000083334]).T
		self.M = matlabarray([[1,     0,     0],[0,     1,     0],[0,     0,     1]])
		self.n = 3
		self.me = 2
		self.mi =0
		self.s =matlabarray([  -0.503054026564966,-1.000000000000000,-0.184478531874161]).T
		self.gx = matlabarray([-0.009783923878659, 1.000000000000000, 0]).T
		self.gci =matlabarray( [])
		self.gce = matlabarray([[1.000000000000000,   0.999999999999999,   1.000000000000000], [1.000000000000000 ,  1.999999999999999,   3.000000000000000]])

		self.info = dummyInfo()
		self.options = helper.dummyOptions()
		self.values = helper.dummyValues()
		
		self.fcmodel = matlabarray([[0.099563123926544,  -0.013550429460611,   1.384968815034240,  0,   6.144976749236061],
						[0.312467441560872,   1.384968815034241,   1.384968815034240,   1.384968815034241,   0.000000000000006],
						  [-0.056489622187450,   1.384968815034241,   2.769937630068480 ,  4.154906445102721,   0.000000000000014]])


		self.Y = matlabarray([
			[  -0.003054026564966,  -0.500000000000000,   0.500000000000000,   0.500000000000000,   0.500000000000000],
		    [               0,   1.000000000000000,                   0,   1.000000000000000,   1.000000000000000],
		   [0.315521468125839,   0.500000000000000,   0.500000000000000,  -0.500000000000000,   0.500000000000000]])
		self.fY = matlabarray([   0.099563123926544,   1.500000000000000,   0.500000000000000,   1.500000000000000,   1.500000000000000])
		self.ciY = matlabarray(  [])
		self.ceY = matlabarray([ 
		[  0.312467441560872,   1.000000000000000 ,  1.000000000000000,   1.000000000000000 ,  2.000000000000000],
		[  -0.056489622187450,   2.000000000000000,   1.000000000000000,                   0,   3.000000000000000]])
		self.sigma = matlabarray([1])
		self.scale = matlabarray([   1.000000000000000, 0.722037918214987, 0.722037918214987, 0.722037918214987, 0.521338755340232]).T
		self.shift_Y = 1
		self.QZ = matlabarray([
			   [1.000000000000000,                   0,                   0,                   0,                   0],
			    [               0,  -0.437717028004984,  -0.826365739060244,   0.329535025867438,  -0.130115853870500],
			    [               0,   0.880814115424577,  -0.315023389192614,   0.329471408091712,  -0.127966204837389],
			    [              0 ,  0.162491294867564 , -0.418566952172131 , -0.884320607054428 , -0.127966204837389],
			    [               0,   0.078529462977709,  -0.206595343893201,  -0.028849989870035,   0.974843149132506]])
		self.RZ = matlabarray([
			   [1.000000000000000,   1.000000000000000,   1.000000000000000,   1.000000000000000,   1.000000000000000],
		   		[               0,   0.819739267991799,  -0.132165180682231,   0.386491133279071,   0.503816009553305],
			    [               0,                   0,  -0.369537503265736,  -0.294775124607443,  -0.596996335387400],
				[               0,                   0,                   0,   0.876403859762092,   0.237890849609900],
			    [               0,                   0,                   0,                   0,  -0.092396452142661]])
		self.whichmodel = 0
		self.ind_Y = matlabarray([  5,     2,     3,     4,     1])
		self.i_xbest = 5
		self.m = 5

	def test_ecdfo_computeHessian(self):
		M,pc,info = ecdfo_computeHessian_(simul=self.simul,x=self.x,null_step=self.null_step,constrained_pbl=self.constrained_pbl,
			lm=self.lm,M=self.M,n=self.n,me=self.me,mi=self.mi,s=self.s,gx=self.gx,gci=self.gci,gce=self.gce,info=self.info,
			options=self.options,values=self.values,fcmodel=self.fcmodel,Y=self.Y,fY=self.fY,ciY=self.ciY,ceY=self.ceY,
			sigma=self.sigma,scale=self.scale,shift_Y=self.shift_Y,QZ=self.QZ,RZ=self.RZ,whichmodel=self.whichmodel,
			ind_Y=self.ind_Y,i_xbest=self.i_xbest,m=self.m)
			
		#print "M:\n", M, "\npc:\n", pc, "\ninfo.g:\n", info.g
			
		correctM = matlabarray([

[   2.620301230585867,                   0,                   0],
 [                  0,                   0,                   0],
  [                 0,                   0,                   0]])


		correctpc = 1
		correctinfog = matlabarray([
  [-0.009783923878659],
  [ 1.000000000000000],
                   [0]])
		
		self.assertEqual(pc, correctpc)
		self.assertTrue((abs(M - correctM) < 1e-8).all())
		self.assertTrue((abs(correctinfog - info.g) < 1e-8).all())
		


if __name__ == '__main__':
	unittest.main()