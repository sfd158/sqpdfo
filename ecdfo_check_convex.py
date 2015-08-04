# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 11:24:27 2014
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% checks whether matrix A is convex.
% if A is not convex, matrix is convexified by perturbing small
% eigenvalues.
%
% the bigger the value EPS, the more different the matrix gets.
%
% programming: A. Troeltzsch, 2014
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@author: jaco_da
"""
# Autogenerated with SMOP version 
# c:\Users\jaco_da\AppData\Local\Continuum\Anaconda\Scripts\smop-script.py ecdfo_check_convex.m

from __future__ import division
#try:
from runtime import *
#print "type eig", type(eig_)
#except ImportError:
#    from smop.runtime import *

def ecdfo_check_convex_(A_=None,options=None,*args,**kwargs):
#    varargin = cellarray(args)
#    nargin = 2-[A,options].count(None)+len(args)

    A=copy_(A_)

    ev=eig_(A)
    evneg=ev[ev < 0]
    if not isempty_(evneg):
        ZERO=matlabarray([[1e-10]])
        EPS=matlabarray([[1e-09]])
        v,d=eig_(A,nargout=2)
        d=diag_(d)
        d[d < ZERO]=EPS
        d=diag_(d)
        A=v * d * v.T
        if not isempty_(find_(~ isreal_(A),1)):
            if options.verbose >= 3:
                disp_('### ecdfo_check_convex: matrix is non symmetric. Resetting A.')
            A=0.5*(A + A.T)
            
    return A

#def ecdfo_check_convex_(A=None,options=None,*args,**kwargs):
#    #varargin = cellarray(args)
#    #nargin = 2-[A,options].count(None)+len(args)
#
#    ev=eig_(A)
#    evneg=ev[ev < 0]
#    if not isempty_(evneg):
#        ZERO=1e-10
#        EPS=1e-09
#        d,v=eig_(A,nargout=2)
#        d[d < ZERO]=EPS
#        d=diag_(d)
#        A=v * d * v.T
#        #print "not is real:", ~isreal_(A)
#        if True in np.iscomplex(A):#not isempty_(find_(~isreal_(A),True)):
#            if options.verbose >= 3:
#                disp_(char('### ecdfo_check_convex: matrix is non symmetric. Resetting A.'))
#            A=(A + A.T) * 0.5
#    return A


