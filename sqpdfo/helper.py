# -*- coding: utf-8 -*-

import numpy as np


class dummyUnionStruct():
      """
      Creates an empty object which can for instance later be used options, info in the SQPDFO algorithm
      """
      pass


class dummyOptions():
      """
      Those are some basics options for the SQPDFO algorithm : they are used for the SQPDFO tests
      """
      def __init__(self):
        self.hess_approx = 131
        self.bfgs_restart = 0
        self.algo_descent = 120
        self.tol_grad = 1.0e-05
        self.tol_feas = 1.0e-05
        self.tol_bnds = 1.0e-05
        self.dxmin = 1.0e-16
        self.miter = 500
        self.msimul = 500
        self.verbose = 0
        self.fout = 1
        self.inf = np.infty
        self.df1 = 0
        self.whichmodel = 0
        self.final_degree = 142

class dummyValues():
      """
      Those are some basics options for the SQPDFO algorithm : they are used for the SQPDFO tests
      """
      def __init__(self):
           # Define SQPDFO constant values
        
           self.success                =   0 # solution found
           self.fail_on_argument       =   1 # an argument is wrong
           self.fail_on_problem        =   2 # unaccepted problem structure
           self.fail_on_simul          =   3 # error on a simulation
           self.stop_on_simul          =   4 # stop required by the simulator
           self.stop_on_max_iter       =   5 # max iterations
           self.stop_on_max_simul      =   6 # max simulations
           self.stop_on_dxmin          =   7 # stop on dxmin
           self.fail_on_non_decrease   =   8 # the merit function no longer decrease
           self.fail_on_ill_cond       =  11 # ill-conditioning
           self.stop_on_small_trust_region = 15 # trust-region radius too small
           self.fail_on_null_step      =  20 # null step d is solution of 'values.max_null_steps' QPs
           self.fail_on_infeasible_QP  =  21 # infeasible QP
           self.fail_on_unbounded_QP   =  22 # unbounded QP
           self.fail_unexpected        =  30 # should not have happened
         
           self.nsimultype             =   4 # nb of simulation types
           self.max_null_steps         =   1 # maximum nbr of null QP steps

           self.powell = 120
           self.wolfe = 121
           self.bfgs = 130
           self.model = 131
           self.linear = 140
           self.diagonal = 141
           self.quadratic = 142
           self.subbasis = 0
           self.frobnorm = 1
           self.l2norm = 2
           self.regression = 3
           self.dline = '--------------------------------------------------------------------------------------'
           self.eline = '======================================================================================'
           self.sline = '**************************************************************************************'
