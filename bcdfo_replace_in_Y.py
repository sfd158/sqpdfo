# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:32:32 2015

@author: lien_ol
"""
from __future__ import division
try:
    from runtime import *
except ImportError:
    from smop.runtime import *

def bcdfo_replace_in_Y_(QZ=None,RZ=None,ynew=None,Y=None,j=None,xbase=None,whichmodel=None,scale=None,shift_Y=None,Delta=None,normgx=None,kappa_ill=None,*args,**kwargs):
#    varargin = cellarray(args)
#    nargin = 12-[QZ,RZ,ynew,Y,j,xbase,whichmodel,scale,shift_Y,Delta,normgx,kappa_ill].count(None)+len(args)

    Y[:,j]=ynew
    QZ,RZ,xbase,scale=bcdfo_build_QR_of_Y_(Y,whichmodel,shift_Y,Delta,normgx,kappa_ill,nargout=4)
    return QZ,RZ,Y,xbase,scale