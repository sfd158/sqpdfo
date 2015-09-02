# -*- coding: utf-8 -*-
from __future__ import division
#try:
from runtime import *
#except ImportError:
    #from smop.runtime import *

def ecdfo_iter_printout_(info=None,old_delta=None,norms=None,pc=None,itype=None,values=None,nb=None,mi=None,options=None,constrained_pbl=None,merit=None,*args,**kwargs):
    """
#  iteration printout
#
    
    """

#    varargin = cellarray(args)
#    nargin = 11-[info,old_delta,norms,pc,itype,values,nb,mi,options,constrained_pbl,merit].count(None)+len(args)

    if options.verbose < 4:
        fprintf_(options.fout,'%4i  %4i'%(info.niter,info.nsimul[1] + info.nsimul[3]))
        fprintf_(options.fout,'  %+14.8e  %+14.8e  '%(info.f,merit))
        if constrained_pbl:
            fprintf_(options.fout,'%10.4e  %14.8e'%(info.glagn,info.feasn))
        else:
            fprintf_(options.fout,'%10.4e'%(info.glagn))
        if info.niter > 1:
            fprintf_(options.fout,'  %8.2e'%(old_delta))
            fprintf_(options.fout,'  %8.2e'%(norms))
            fprintf_(options.fout,'  %4.2f'%(pc))
            fprintf_(options.fout,'  %5s\n'%(itype))
        else:
            fprintf_(options.fout,'  \n')
    if options.verbose >= 4:
        fprintf_(options.fout,'%s\n'%(values.dline))
        fprintf_(options.fout,'iter %i,'%(info.niter))
        fprintf_(options.fout,'  cost %12.5e'%(info.f))
        if constrained_pbl:
            fprintf_(options.fout,',  glagn %11.5e,  feas %11.5e'%(info.glagn,info.feasn))
            if (nb + mi > 0):
                fprintf_(options.fout,',  compl %11.5e'%(info.compl))
        else:
            fprintf_(options.fout,',  grad %11.5e'%(info.glagn))
        if info.niter > 1:
            fprintf_(options.fout,'  %4.2f\n'%(pc))
        else:
            fprintf_(options.fout,'  \n')
    return
