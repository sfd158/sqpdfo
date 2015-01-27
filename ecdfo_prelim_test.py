# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 15:02:21 2014
INPUT VALUES
K>> func,x0,lm0,Delta0,lb,ub,scaleX,scalefacX,cur_degree,...
   rep_degree,plin,pdiag,pquad,c,initial_Y,kappa_ill,whichmodel,factor_FPR,...
   Lambda_FP,Lambda_CP,eps_L,lSolver,hardcons,stratLam,xstatus,sstatus,dstatus,options

func = 

    @evalfgh


x0 =

                   0
                   0
   0.500000000000000


lm0 =

   Empty matrix: 0-by-1


Delta0 =

     1


lb =

  -0.500000000000000
                   0
                -Inf


ub =

   Inf
   Inf
   Inf


scaleX =

     0


scalefacX =

     1     1     1


cur_degree =

     4


rep_degree =

     4


plin =

     4


pdiag =

     7


pquad =

    10


c = 

           free: 0
          fixed: 1
    alwaysfixed: 2
             in: 1
            out: 0
         unused: 0
            inY: 1
          dummy: 1
        nodummy: 0


initial_Y =

simplx


kappa_ill =

     1.000000000000000e+15


whichmodel =

     0


factor_FPR =

    10


Lambda_FP =

     1.000000000000000e-10


Lambda_CP =

   1.200000000000000


eps_L =

     1.000000000000000e-03


lSolver =

     1


hardcons =

     0


stratLam =

     1


xstatus =

     []


sstatus =

     []


dstatus =

     []


options = 

           algo_method: 'quasi-Newton'
    algo_globalization: 'trust regions'
           hess_approx: 'model'
          bfgs_restart: 0
          algo_descent: 'Powell'
                   tol: [1.000000000000000e-05 1.000000000000000e-05 1.000000000000000e-05]
                 dxmin: 1.000000000000000e-06
                 miter: 500
                msimul: 500
               verbose: 2


OUTPUT VALUES

K>> n,nb,mi,me,x,lm,lb,ub,scalefacX,Delta,nfix,indfix,xfix,vstatus,xstatus,...
      sstatus,dstatus,QZ,RZ,scale,poised,Y_radius,poised_model,X,fX,Y,fY,...
      ciX,ciY,ceX,ceY,poisedness_known,m,gx,normgx,fcmodel,ind_Y,i_xbest,...
      cur_degree,rep_degree,plin,pdiag,pquad,indfree,info,options,values

n =

     3


nb =

     2


mi =

     0


me =

     2


x =

   0.500000000000000
   1.000000000000000
   0.500000000000000


lm =

                   0
                   0
                   0
  -0.333333332763891
  -0.000000000249999


lb =

  -0.500000000000000
                   0
                -Inf


ub =

   Inf
   Inf
   Inf


scalefacX =

     1     1     1


Delta =

     1


nfix =

     0


indfix =

     []


xfix =

     0
     0
     0


vstatus =

     0
     0
     0


xstatus =

     1
     1
     1
     1


sstatus =

     1     1     1     1


dstatus =

     0
     0
     0
     0


QZ =

     1     0     0     0
     0     1     0     0
     0     0     1     0
     0     0     0     1


RZ =

     1     1     1     1
     0    -1     0     0
     0     0    -1     0
     0     0     0    -1


scale =

     1
     1
     1
     1


poised =

     1


Y_radius =

     1


poised_model =

     1


X =

   0.500000000000000  -0.500000000000000   0.500000000000000   0.500000000000000
   1.000000000000000   1.000000000000000                   0   1.000000000000000
   0.500000000000000   0.500000000000000   0.500000000000000  -0.500000000000000


fX =

   1.500000000000000   1.500000000000000   0.500000000000000   1.500000000000000


Y =

   0.500000000000000  -0.500000000000000   0.500000000000000   0.500000000000000
   1.000000000000000   1.000000000000000                   0   1.000000000000000
   0.500000000000000   0.500000000000000   0.500000000000000  -0.500000000000000


fY =

   1.500000000000000   1.500000000000000   0.500000000000000   1.500000000000000


ciX =

     []


ciY =

     []


ceX =

     2     1     1     1
     3     2     1     0


ceY =

     2     1     1     1
     3     2     1     0


poisedness_known =

     1


m =

     4


gx =

     0
     1
     0


normgx =

     1


fcmodel =

   1.500000000000000                   0   1.000000000000000                   0
   2.000000000000000   1.000000000000000   1.000000000000000   1.000000000000000
   3.000000000000000   1.000000000000000   2.000000000000000   3.000000000000000


ind_Y =

     1     2     3     4


i_xbest =

     1


cur_degree =

     4


rep_degree =

     4


plin =

     4


pdiag =

     7


pquad =

    10


indfree =

     1     2     3


info = 

         g: [3x1 double]
        ai: []
        ae: [2x3 double]
        hl: []
     niter: 0
      flag: 0
    nsimul: [0 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        ci: []
        ce: [2x1 double]
         f: 1.500000000000000
      glag: [3x1 double]


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

     2
     3

K>> info.glag

ans =

  -0.333333333013890
   0.666666666736111
  -0.333333333513889

@author: jaco_da
"""

import unittest
from ecdfo_prelim import *
from evalfgh import *
import numpy as np
import helper

class myDummyOptions():
	def __init__(self):
		self.algo_method = char('quasi newton')#char('quasi newton')
		self.algo_globalization = char('trust regions')
		self.hess_approx = char('model')
		self.bfgs_restart = 0
		self.algo_descent = char('powell')
		self.tol = matlabarray([1.000000000000000e-05, 1.000000000000000e-05, 1.000000000000000e-05])
		self.dxmin = 1.000000000000000e-06
		self.miter = 500
		self.msimul = 500
		self.verbose = 2
		
class Test_ecdfo_prelim(unittest.TestCase):

	def setUp(self):
		
		self.func = evalfgh_
		self.x0 = matlabarray([0, 0, 0.500000000000000]).T
		self.lm0 =matlabarray([])#   Empty matrix: 0-by-1
		self.Delta0 = 1
		self.lb = matlabarray([-0.500000000000000, 0, -np.Inf]).T
		self.ub = matlabarray([np.Inf,np.Inf,np.Inf]).T
		self.scaleX = 0
		self.scalefacX = matlabarray([ 1,     1,     1])
		self.cur_degree =  4
		self.rep_degree =  4
		self.plin = 4
		self.pdiag = 7
		self.pquad = 10
		
		self.c = helper.dummyUnionStruct()
		self.c.free = 0
		self.c.fixed = 1
		self.c.alwaysfixed = 2
		self.c.in_ = 1
		self.c.out = 0
		self.c.unused = 0
		self.c.inY = 1
		self.c.dummy = 1
		self.c.nodummy = 0

		self.initial_Y = char('simplx')
		self.kappa_ill = 1.000000000000000e+15
		self.whichmodel =  0
		self.factor_FPR = 10
		self.Lambda_FP = 1.000000000000000e-10
		self.Lambda_CP = 1.200000000000000
		self.eps_L = 1.000000000000000e-03
		self.lSolver = 1
		self.hardcons = 0
		self.stratLam = 1
		self.xstatus = matlabarray([])
		self.sstatus = matlabarray([])
		self.dstatus = matlabarray([])
		
		self.options = myDummyOptions()
		set_prob(3)
		#self.values = helper.dummyValues()

	def test_ecdfo_prelim(self):
		#self.options.algo_method = 'quasi newton'
		#print "################-----STARTING TEST!!!-----#########################"
		n,nb,mi,me,x,lm,lb,ub,scalefacX,Delta,nfix,indfix,xfix,vstatus,xstatus,sstatus,dstatus,QZ,RZ,scale,poised,Y_radius,poised_model,X,fX,Y,fY,ciX,ciY,ceX,ceY,poisedness_known,m,gx,normgx,fcmodel,ind_Y,i_xbest,cur_degree,rep_degree,plin,pdiag,pquad,indfree,info,options,values = ecdfo_prelim_(func=self.func,x0=self.x0,lm0=self.lm0,Delta0=self.Delta0,
		lb=self.lb,ub=self.ub,scaleX=self.scaleX,scalefacX=self.scalefacX,cur_degree=self.cur_degree,rep_degree=self.rep_degree,
		plin=self.plin,pdiag=self.pdiag,pquad=self.pquad,c=self.c,initial_Y=self.initial_Y,kappa_ill=self.kappa_ill,
		whichmodel=self.whichmodel,factor_FPR=self.factor_FPR,Lambda_FP=self.Lambda_FP,Lambda_CP=self.Lambda_CP,
		eps_L=self.eps_L,lSolver=self.lSolver,hardcons=self.hardcons,stratLam=self.stratLam,xstatus=self.xstatus,
		sstatus=self.sstatus,dstatus=self.dstatus,options=self.options)
		
		
		correctn = 3
		correctnb = 2
		correctmi =  0
		correctme =  2
		correctx = matlabarray([0.500000000000000, 1.000000000000000, 0.500000000000000]).T
		correctlm = matlabarray([  0,  0, 0,-0.333333332763891,-0.000000000249999]).T
		correctlb = matlabarray([-0.500000000000000, 0, -np.Inf]).T
		correctub = matlabarray([np.Inf, np.Inf, np.Inf]).T
		correctscalefacX = matlabarray([  1,     1,     1])
		correctDelta = 1
		correctnfix = 0
		correctindfix = matlabarray( [])
		correctxfix = matlabarray([ 0, 0, 0]).T
		correctvstatus = matlabarray([0, 0, 0]).T
		correctxstatus = matlabarray([ 1, 1, 1, 1]).T
		correctsstatus = matlabarray([ 1,     1,     1,     1])
		correctdstatus = matlabarray([0, 0, 0, 0]).T
		correctQZ = matlabarray([
					     [1,     0,     0,     0],
					     [0,     1,     0,     0],
					     [0,     0,     1,     0],
					     [0,     0,     0,     1]])
		correctRZ = matlabarray([
					     [1,     1,     1,     1],
					     [0,    -1,     0,     0],
					     [0,     0,    -1,     0],
					     [0,     0,     0,    -1]])
		correctscale = matlabarray([1, 1, 1, 1]).T
		correctpoised =  1
		correctY_radius =  1
		correctpoised_model =  1
		correctX = matlabarray([
					   [0.500000000000000,  -0.500000000000000,   0.500000000000000,   0.500000000000000],
					   [1.000000000000000,   1.000000000000000,                   0,   1.000000000000000],
					   [0.500000000000000,   0.500000000000000,   0.500000000000000,  -0.500000000000000]])
		correctfX = matlabarray([ 1.500000000000000,   1.500000000000000,   0.500000000000000,   1.500000000000000])
		correctY = matlabarray([
					[0.500000000000000,  -0.500000000000000,   0.500000000000000,   0.500000000000000],
					[1.000000000000000,   1.000000000000000,                   0,   1.000000000000000],
					[0.500000000000000,   0.500000000000000,   0.500000000000000,  -0.500000000000000]])
		correctfY = matlabarray([ 1.500000000000000,   1.500000000000000,   0.500000000000000,   1.500000000000000])
		correctciX = matlabarray(  [])
		correctciY = matlabarray([])
		correctceX = matlabarray([
					     [2,     1,     1,     1],
					     [3,     2,     1,     0]])
		correctceY = matlabarray([
					     [2,     1,     1,     1],
					     [3,     2,     1 ,    0]])
		correctpoisedness_known =  1
		correctm = 4
		correctgx = matlabarray([  0,  1,  0]).T
		correctnormgx =  1
		correctfcmodel = matlabarray([
		[1.500000000000000,                   0,   1.000000000000000,                   0],
		   [2.000000000000000,   1.000000000000000,   1.000000000000000,   1.000000000000000],
		   [3.000000000000000,   1.000000000000000,   2.000000000000000,   3.000000000000000]])
		correctind_Y = matlabarray([ 1,     2,     3,     4])
		correcti_xbest = 1
		correctcur_degree = 4
		correctrep_degree = 4
		correctplin = 4
		correctpdiag = 7
		correctpquad = 10
		correctindfree = matlabarray([  1,     2,     3])
		
		#print "ecdfo_prelim outputs"
		#print n,nb,mi,me,x,lm,lb,ub,scalefacX,Delta,nfix,indfix,xfix,vstatus,xstatus,sstatus,dstatus,QZ,RZ,scale,poised,Y_radius,poised_model,X,fX,Y,fY,ciX,ciY,ceX,ceY,poisedness_known,m,gx,normgx,fcmodel,ind_Y,i_xbest,cur_degree,rep_degree,plin,pdiag,pquad,indfree,info,options,values
		
		self.assertEqual(n, correctn)
		self.assertEqual(int(nb), correctnb)
		self.assertEqual(mi, correctmi)
		#print "me", me
		#print "correctme", correctme
		self.assertEqual(me, correctme)
		
		

if __name__ == '__main__':
	unittest.main()