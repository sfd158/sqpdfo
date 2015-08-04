# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 15:21:20 2014
%
% [lm,info] = sqplab_lsmult (x,lb,ub,info,options,values);
%
% This procedure computes an exact 
% least-squares multiplier 'lm'. It solves in lm the
% quadratic optimization problem:
%
%   min || g+A'*lm ||^2
%   subject to possible bounds on lm,
%
% where g = info.g, lm = lm(1:n+mi+me) and A' = [ones(n) info.ai'
% info.ae']. 
%
% A multiplier associated with an inequality constraint having 
% - infinite lower and upper bounds vanishes,
% - infinite lower bound and finite upper bound is nonnegative,
% - finite lower bound and infinite upper bound is nonpositive,
% - finite lower bound and finite upper bound can have any sign.
% A lower (resp. upper) bound is considered as infinite if its value is
% empty or <= -options.inf (resp. empty or >= options.inf).
%
% On entry:
%   info.ci = ci(x)
%   lb: (optional or (n+mi) x 1) lower bounds on the n variables and mi
%       inequality constraints, is considered as empty if not present
%   ub: (optional or (n+mi) x 1) upper bounds on the n variables and mi
%       inequality constraints, is considered as empty if not present
%
% On return:
%   lm: computed least-squares multiplier, more precisely
%       lm(1:n): multiplier associated with the bounds on the variables
%       lm(n+1:n+mi): multiplier associated with the mi inequality
%           constraints
%       lm(n_mi+1:n+mi+me): multiplier associated with the me equality
%           constraints

%-----------------------------------------------------------------------
%
% Author: Jean Charles Gilbert, INRIA, and Anke Troeltzsch, DLR.
%
% Copyright 2008, 2009, INRIA.
%
% SQPlab is distributed under the terms of the Q Public License version
% 1.0.
%
% This program is distributed in the hope that it will be useful, but
% WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Q Public
% License version 1.0 for more details.
%
% You should have received a copy of the Q Public License version 1.0
% along with this program.  If not, see
% <http://doc.trolltech.com/3.0/license.html>.
%
%-----------------------------------------------------------------------

% Initialization
@author: jaco_da
"""

# Autogenerated with SMOP version 
# c:\Users\jaco_da\AppData\Local\Continuum\Anaconda\Scripts\smop-script.py sqplab_lsmult.m

from __future__ import division
#try:
from runtime import *
from ecdfo_check_convex import *
from ecdfo_check_cond import *
from blls import *
from copy import copy

#except ImportError:
#    from smop.runtime import *

def sqplab_lsmult_(x=None,lb_=None,ub_=None,info_=None,options=None,values=None,*args,**kwargs):
#    varargin = cellarray(args)
    info=copy(info_)
    lb=copy_(lb_)
    ub=copy_(ub_)

    nargin = 6-[x,lb,ub,info,options,values].count(None)+len(args)
    
    lm=matlabarray([])
    info.flag=values.success
    badcond=0
    n=length_(info.g)
    me=0
    if (nargin >= 3):
        me=size_(info.ae,1)
    if (nargin < 4) or isempty_(lb):
        lb=- options.inf * ones_(n,1)
    else:
        lb=lb[:]
        if any_(size_(lb) != [n,1]):
            fprintf_('\n### sqplab_lsmult: incorrect size of lb\n\n')
            info.flag=values.fail_strange
            return lm,info
    if (nargin < 5) or isempty_(ub):
        ub=options.inf * ones_(n,1)
    else:
        ub=ub[:]
        if any_(size_(ub) != [n,1]):
            fprintf_('\n### sqplab_lsmult: incorrect size of ub\n\n')
            info.flag=values.fail_strange
            return lm,info
    A=concatenate_([eye_(n),info.ae])
    lo=- inf * ones_(n + me,1)
    up=inf * ones_(n + me,1)
    for i in arange_(1,n).reshape(-1):
        if (lb[i] <= - options.inf):
            lo[i]=0
        if (ub[i] >= options.inf):
            up[i]=0
        if (lb[i] > - options.inf) and (abs_(x[i] - lb[i]) < options.dxmin):
            up[i]=0
        if (ub[i] < options.inf) and (abs_(x[i] - ub[i]) < options.dxmin):
            lo[i]=0
    AA=A * A.T
    check_condition=0
    if check_condition:
        cthreshold=1e+17
        AA,badcond=ecdfo_check_cond_(AA,cthreshold,options,nargout=2)
    check_convex=1
    if check_convex:
        AA=ecdfo_check_convex_(AA,options)
    Ag=A * info.g
    AAn=copy_(AA)
    Agn=copy_(Ag)
    lon=copy_(lo)
    upn=copy_(up)
    ifree=ones_(size_(lo))
    k=1
    for i in arange_(1,length_(lo)).reshape(-1):
        if lo[i] == up[i]:
#            AAn[k,:]=[]
#            AAn[:,k]=[]
#            Agn[k]=[]
#            lon[k]=[]
#            upn[k]=[]
            AAn=np.delete(AAn, k-1, 0)
            AAn=np.delete(AAn, k-1, 1)
            Agn=np.delete(Agn, k-1, 0)
            lon=np.delete(lon, k-1, 0)
            upn=np.delete(upn, k-1, 0)
            ifree[i]=0
        else:
            k=k + 1
    if not isempty_(ifree[ifree > 0]):
        sn,rn,op,exitc=blls_(AAn,- Agn,lon,upn,nargout=4)
        I=eye_(length_(lo))
        lm=np.delete(I, find_(ifree<=0)-1, 1)*sn
    else:
        lm=zeros_(size_(lo))
    return lm,info

#def sqplab_lsmult_(x=None,lb=None,ub=None,info=None,options=None,values=None,*args,**kwargs):
#    #varargin = cellarray(args)
#    nargin = 6-[x,lb,ub,info,options,values].count(None)+len(args)
#
#    lm=matlabarray([])
#    info.flag=values.success
#    badcond=0
#    n=length_(info.g)
#    me=0
#    if (nargin >= 3):
#        me=size_(info.ae,1)
#    if (nargin < 4) or isempty_(lb):
#        lb=- options.inf * ones_(n,1)
#    else:
#        lb=lb[:]
#        if any_(size_(lb) != [n,1]):
#            fprintf_(char('\\n### sqplab_lsmult: incorrect size of lb\\n\\n'))
#            info.flag=values.fail_strange
#            return lm,info
#    if (nargin < 5) or isempty_(ub):
#        ub=options.inf * ones_(n,1)
#    else:
#        ub=ub[:]
#        if any_(size_(ub) != [n,1]):
#            fprintf_(char('\\n### sqplab_lsmult: incorrect size of ub\\n\\n'))
#            info.flag=values.fail_strange
#            return lm,info
#    A=concatenate_((eye_(n),info.ae))#matlabarray([[eye_(n)],[info.ae]])
#    lo=- inf * ones_(n + me,1)
#    up=inf * ones_(n + me,1)
#    for i in arange_(1,n).reshape(-1):
#        #print "i", i					
#        #print "lb", lb[1]
#        if (lb[i] <= - options.inf):
#            lo[i]=0
#        if (ub[i] >= options.inf):
#            up[i]=0
#        if (lb[i] > - options.inf) and (abs_(x[i] - lb[i]) < options.dxmin):
#            up[i]=0
#        if (ub[i] < options.inf) and (abs_(x[i] - ub[i]) < options.dxmin):
#            lo[i]=0
#    #print A	
#    #print A.T											
#    AA=A * A.T
#    check_condition=0
#    if check_condition:
#        cthreshold=1e+17
#        AA,badcond=ecdfo_check_cond_(AA,cthreshold,options,nargout=2)
#    check_convex=1
#    if check_convex:
#        AA=ecdfo_check_convex_(AA,options)
#    Ag=A * info.g
#    AAn=copy_(AA)
#    Agn=copy_(Ag)
#    lon=copy_(lo)
#    upn=copy_(up)
#    #print "size lo", size_(lo)#.obj
#    #ifree=ones_(size_(lo))
#    #print "[ gnlph list expression]", [gnlph for gnlph in size_(lo)]
#    ifree=ones_(*lo.shape)#[gnlph for gnlph in size_(lo)])
#    k=0#1
#    for i in arange_(1,length_(lo)).reshape(-1):
#        if lo[i] == up[i]:
#            #k-te Zeile löschen									
#            #AAn[k,:]=[]
#            #k-te spalte löschen								
#            #AAn[:,k]=[]
#            #k-ten eintrag löschen								
#            #Agn[k]=[]
#            #lon[k]=[]
#            #upn[k]=[]
#            #print "-----"								
#            #print "k = ", k								
#            #print "AAn before\n", AAn								
#            #AAn = np.delete(AAn, AAn[k,:])#=[]
#            AAn = np.delete(AAn, k, 0)#=[]
#            #print "AAn after\n", AAn												
#            #print "AAn before 2\n", AAn												
#            AAn = np.delete(AAn, k, 1)#=[]
#            #print "AAn 2 after\n", AAn
#            #print "Agn before\n", Agn												
#            Agn = np.delete(Agn, k, 0)#=[]
#            #print "Agn after\n", Agn
#            #print "lon before\n", lon												
#            lon = np.delete(lon, k, 0)#=[]
#            #print "lon after\n", lon
#            #print "upn before\n", upn												
#            upn = np.delete(upn, k, 0)#=[]
#            #print "upn after\n", upn												
#            ifree[i]=0
#            #print "-----"																				
#        else:
#            k=k + 1
#    if not isempty_(ifree[ifree > 0]):
#        sn,rn,op,exitc=blls_(AAn,- Agn,lon,upn,nargout=4)
#        I=eye_(length_(lo))
#        #print "ifree:", ifree
#        gnlphy = []								
#        for gnlphi in range(len(ifree)):
#            if ifree[gnlphi+1] < 1:									
#                gnlphy.append(gnlphi)									
#        #print "[ifree]", gnlphy								
#        #print "I[:,ifree > 0]:\n", I[:,ifree > 0]								
#        #print "sn:\n", sn								
#        #print "np.delete(I, ifree < 1, 1):\n", np.delete(I, gnlphy, 1)								
#        #lm=I[:,ifree > 0] * sn
#        lm=np.delete(I, gnlphy, 1) * sn								
#    else:
#        lm=zeros_(size_(lo))
#    return lm,info
