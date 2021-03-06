# -*- coding: utf-8 -*-

from sqpdfo.runtime import *
from copy import copy
from numpy import *
from sqpdfo.bcdfo_solve_TR_MS import bcdfo_solve_TR_MS_


def bcdfo_solve_TR_MS_bc_(g=None,H=None,lb=None,ub=None,Delta=None,eps_D=None,stratLam=None,options=None,*args,**kwargs):
    """
#
#  An implementation of exact trust-region minimization based on the
#  More-Sorensen algorithm subject to bound constraints.
#
#  INPUT:
#
#  g        : the model's gradient
#  H        : the model's Hessian
#  lb       : lower bounds on the step
#  ub       : upper bounds on the step
#  Delta    : the trust-region's radius
#  eps_D    : the accuracy required on the equation ||s|| = Delta for a
#             boundary solution
#  stratLam : the strategy to adjust lamb to find an active bound
#             (1 - Newtons method, 0 - bisection method)
#
#  OUTPUT:
#
#  s        : the trust-region step
#  lamb   : the Lagrange multiplier corresponding to the trust-region constraint
#  norms    : the norm of s
#  value    : the value of the model at the optimal solution
#  gplus    : the value of the model's gradient at the optimal solution
#  nfact    : the number of Cholesky factorization required
#  neigd    : the number of eifenvalue decompositions required
#  msg      : an information message
#
#  DEPENDENCIES: bcdfo_solve_TR_MS
#
#  PROGRAMMING: A. Troeltzsch, S. Gratton, July 2009.
#              ( This version 14 VI 2018 )
#
#  TEST:
#
#  bcdfo_solve_TR_MS_bc( [2; 3], [4 6; 6 5], [-10; -10], [10; 10], 1.0, 0.001, 1 )
#  should give
#    0.5153
#   -0.8575
#
#  bcdfo_solve_TR_MS_bc( [2; 3], [4 6; 6 5], [-0.1; -0.1], [10; 10], 1.0, 0.001, 1 )
#  should give
#   -0.1
#   -0.1
#
#  bcdfo_solve_TR_MS_bc( [2; 3], [4 6; 6 5], [-10; -10], [0; 0], 1.0, 0.001, 1 )
#  should give
#    0
#   -0.6
#
#  CONDITIONS OF USE: Use at your own risk! No guarantee of any kind given.
#
    """    

    lambda_save = []
    norms_b_save = []
    verbose = 0;                    # default : 0 (silent)
    if options.verbose == 2:
        verbose = 1
    elif options.verbose > 2:
        verbose = 2                 # 2 for debug
    theta      = 1.0e-13;          # accuracy of the interval on lambda
    eps_bound  = 1.0e-5;           # the max distance | bound - x | < eps_bound for 
                               # a boundary solution
                                 
    # initialization 

    msg        = 'no free variables'
    _lambda     = 0                # initial lambda
    value      = 0                # initial model value
    nfact      = 0                # initialize in case of error
    neigd      = 0                # initialize in case of error
    Delta0     = copy(Delta)
    g0         = copy(g)           # copy initial gradient
    gplus      = copy(g)           # initialize gplus
    s          = zeros_(size_(g))  # initial zero step
    norms      = 0
    n          = length_(g)        # space dimension
    I          = eye_(n)           # identity matrix used for projection
    ind_active = array([])         # indeces of active bounds
    ind_free   = arange(0,n)       # indeces of inactive bounds
    nfree      = copy(n)           # nbr of inactive indeces
    
    if (verbose > 1):
        disp_('bcdfo_solve_TR_MS_bc: enter')
    if (not isempty_(find_(isnan(H)))):
        if (verbose):
            disp_('Error in bcdfo_solve_TR_MS_bc: H contains NaNs!')
        msg='error1'
        if (verbose > 1):
            disp_('bcdfo_solve_TR_MS_bc: exit!')
        return s,_lambda,norms,value,gplus,nfact,neigd,msg
    if (not isempty_(find_(~ isreal(H)))):
        if (verbose):
            disp_('Error in bcdfo_solve_TR_MS_bc: H contains imaginary parts!')
        msg='error2'
        if (verbose > 1):
            disp_('bcdfo_solve_TR_MS_bc: exit!')
        return s,_lambda,norms,value,gplus,nfact,neigd,msg
    if (not isempty_(find_(isinf(H)))):
        if (verbose):
            disp_('Error in bcdfo_solve_TR_MS_bc: H contains infinite elements!')
        msg='error3'
        if (verbose > 1):
            disp_('bcdfo_solve_TR_MS_bc: exit!')
        return s,_lambda,norms,value,gplus,nfact,neigd,msg
#  Fix active components

    ind_g_crit=find_(logical_or(logical_and(g[ind_free]>0, abs(lb[ind_free]) <= 1e-10), logical_and(g[ind_free] < 0, ub[ind_free] <= 1e-10)))

    if (not isempty_(ind_g_crit)):
        ind_active=ind_free[ind_g_crit].T
        ind_free=setdiff_(ind_free,ind_active)
        nfree=length_(ind_free)
#  Loop until no free variables anymore

    j=0
    while nfree > 0:
   #  Loop until all active variables are detected and fixed

        new_call_to_MS=1
        while (new_call_to_MS == 1):
      #  Minimize system in the (possibly) reduced subspace

            j=j + 1
            if (verbose > 1):
                disp_('(',str(j),') ---- minimizing in the (sub)space of ',str(length_(ind_free)),' variable(s)')
            g_reduced=g[ind_free]
            H_reduced=H[ix_(ind_free,ind_free)]
      #  Call unconstrained MS in (possibly) reduced subspace
 
            s_deltaMS,_lambda,norms_deltaMS,value_red,gplus_red,nfact_r,neigd_r,msg,hardcase=bcdfo_solve_TR_MS_(g_reduced,H_reduced,Delta,eps_D,nargout=9)
            nfact=nfact + nfact_r
            neigd=neigd + neigd_r
            gplus[ind_free]=gplus[ind_free] + gplus_red
            s_after_reduced_ms=s + I[:,ind_free] .dot( s_deltaMS )
      #  Compute critical components which became active during the last MS iteration
            ind_u_crit=find_(logical_and(ub[ind_free] - s_after_reduced_ms[ind_free] <= eps_bound, ub[ind_free] <= 1e-10))
            ind_l_crit=find_(logical_and(s_after_reduced_ms[ind_free] - lb[ind_free] <= eps_bound, lb[ind_free] >= -1e-10))
      #  Fix these new active components

            if (length_(ind_u_crit) + length_(ind_l_crit) != 0):
                ind_active=concatenate_([ind_active,ind_free[ind_u_crit].T,ind_free[ind_l_crit].T],axis=1)
                ind_free=setdiff_(list(range(0,n)),ind_active)
                nfree=length_(ind_free)
                if (verbose > 1):
                    disp_('fixed one or more variables')
                #  If no inactive variables anymore --> exit

                if (nfree == 0):
                    norms=norm_(s)
                    value=0.5 * s.T.dot( H.dot( s )) + s.T .dot( g0 )
                    if (verbose > 1):
                        disp_('no inactive variables anymore - return')
                        disp_('bcdfo_solve_TR_MS_bc: exit!')
                    return s,_lambda,norms,value,gplus,nfact,neigd,msg
            else:
                new_call_to_MS=0
   #  Check if step is outside the bounds

        if (verbose > 1):
            disp_('check if step inside bounds')
        out_of_ubound=find_((ub[ind_free] - s_after_reduced_ms[ind_free]) < 0.0)
        out_of_lbound=find_((s_after_reduced_ms[ind_free] - lb[ind_free]) < 0.0)
        out_of_ubound_init=copy(out_of_ubound)
        out_of_lbound_init=copy(out_of_lbound)
        if (length_(out_of_ubound) + length_(out_of_lbound) != 0):
            back_inside=0
            lambda0=copy(_lambda)
            if (verbose > 1):
                disp_('step outside bounds!')
                print(out_of_ubound)
                print(out_of_lbound)
                disp_('lambda_0=',str(lambda0))
      #  Set lower bound on lambda.
  
            lower=copy(_lambda)
      #  New lambda for bisection method

            if (stratLam == 0):
                _lambda=max_(2.0,2 * _lambda)
      #  Compute upper bound on lambda (using the closest bound out of the hit bounds) 
 
            gnorm=norm_(g)
            if (length_(out_of_ubound) > 0):
                delta_b=min_(abs(ub[ind_free[out_of_ubound]] - s[ind_free[out_of_ubound]]))
            if (length_(out_of_lbound) > 0):
                delta_b=min_(abs(lb[ind_free[out_of_lbound]] - s[ind_free[out_of_lbound]]))
                if (length_(out_of_ubound) > 0):
                    delta_b=min_(min_(abs(ub[ind_free[out_of_ubound]] - s[ind_free[out_of_ubound]])),delta_b)
            goverD=gnorm / delta_b
            Hnorminf=norm_(H,inf)
            if (Hnorminf > 0):  # because Octave generates a NaN for null matrices.
                HnormF=norm_(H,'fro')
            else:
                HnormF=0
            upper=max_(0,goverD + min_(Hnorminf,HnormF))
      #  Compute active components

            ind_u_active=find_(abs(ub[ind_free] - s_after_reduced_ms[ind_free]) <= eps_bound)
            ind_l_active=find_(abs(s_after_reduced_ms[ind_free] - lb[ind_free]) <= eps_bound)
      #  Loop on successive trial values for lambda.
 
            i=0
            while (((length_(ind_u_active) + length_(ind_l_active)) == 0) or (length_(out_of_lbound) + length_(out_of_ubound) != 0)):

                i=i + 1
               #  Print lambda value
                old_lambda=copy(_lambda)
                new_lambda=- 1
                if (verbose > 1):
                    disp_(' bcdfo_solve_TR_MS_bc (',str(i),'): lower = ',str(lower),' lambda = ',str(_lambda),' upper = ',str(upper))
            #  Factorize H + lambda * I.
 
                R,p=chol_(H[ix_(ind_free,ind_free)] + _lambda * eye_(nfree),nargout=2)
                if (not isempty_(find_(isnan(R)))):
                    if verbose:
                        print("H="+str(H))
                        print("Lambda ="+str(_lambda))
                        print("norm(g)="+str(norm_(g)))
                        print("R="+R)
                        print("p="+p)
                        disp_('Error in bcdfo_solve_TR_MS_bc: NaNs in Cholesky factorization')
                    msg='error4'
                    if (verbose > 1):
                        disp_('bcdfo_solve_TR_MS_bc: exit!')
                    return s,_lambda,norms,value,gplus,nfact,neigd,msg
                nfact=nfact + 1
             #  Successful factorization 
 
                if (p == 0 and hardcase == 0):
                    s_deltaH=np.linalg.solve(- R,(np.linalg.solve(R.T,g[ind_free])))
                    s_duringH=s + I[:,ind_free].dot( s_deltaH )
                 #  Find components which are at its bound and became active
                    ind_u_crit=find_(logical_and(ub[ind_free] - s_duringH[ind_free] <= eps_bound, ub[ind_free] <= 1e-10))
                    ind_l_crit=find_(logical_and(s_duringH[ind_free] - lb[ind_free] <= eps_bound, lb[ind_free] >= -1e-10))
                 #  Set these new active components to zero for one iteration

                    if (length_(ind_u_crit) != 0):
                        s_deltaH[ind_u_crit]=0.0
                        s_duringH[ind_free[ind_u_crit]]=0.0
                    if (length_(ind_l_crit) != 0):
                        s_deltaH[ind_l_crit]=0.0
                        s_duringH[ind_free[ind_l_crit]]=0.0
                    out_of_ubound=find_((ub[ind_free] - s_duringH[ind_free]) < 0.0)
                    out_of_lbound=find_((s_duringH[ind_free] - lb[ind_free]) < 0.0)
                    # find an appropriate bound for the next homotopy-step when using Newton's method

                    if (stratLam == 1 or verbose > 1):
                        if ((length_(out_of_ubound) != 0) or (length_(out_of_lbound) != 0)):
                         #  OUTSIDE the bounds: find the furthest step component 

                            outside=1
                            if (length_(out_of_ubound) != 0):
                                diff_b_u,ind_b_u=max_(abs(ub[ind_free[out_of_ubound]] - s_duringH[ind_free[out_of_ubound]]),nargout=2)
                                norms_b=abs(s_deltaH[out_of_ubound[ind_b_u]])
                                delta_b=abs(ub[ind_free[out_of_ubound[ind_b_u]]] - s[ind_free[out_of_ubound[ind_b_u]]])
                                ind_b=out_of_ubound[ind_b_u]
                                sign_b=sign_(ub[ind_free[out_of_ubound[ind_b_u]]] - s[ind_free[out_of_ubound[ind_b_u]]])
                                out_of_ubound_init=concatenate_([out_of_ubound_init,out_of_ubound],axis=0)
                            if (length_(out_of_lbound) != 0):
                                diff_b_l,ind_b_l=max_(abs(s_duringH[ind_free[out_of_lbound]] - lb[ind_free[out_of_lbound]]),nargout=2)
                                norms_b=abs(s_deltaH[out_of_lbound[ind_b_l]])
                                delta_b=abs(lb[ind_free[out_of_lbound[ind_b_l]]] - s[ind_free[out_of_lbound[ind_b_l]]])
                                ind_b=out_of_lbound[ind_b_l]
                                sign_b=sign_(lb[ind_free[out_of_lbound[ind_b_l]]] - s[ind_free[out_of_lbound[ind_b_l]]])
                                out_of_lbound_init=concatenate_([out_of_lbound_init,out_of_lbound],axis=0)
                            if ((length_(out_of_ubound) != 0) and (length_(out_of_lbound) != 0)):
                                if (diff_b_u > diff_b_l):
                                    norms_b=abs(s_deltaH[out_of_ubound[ind_b_u]])
                                    delta_b=abs(ub[ind_free[out_of_ubound[ind_b_u]]] - s[ind_free[out_of_ubound[ind_b_u]]])
                                    ind_b=out_of_ubound[ind_b_u]
                                    sign_b=sign_(ub[ind_free[out_of_ubound[ind_b_u]]] - s[ind_free[out_of_ubound[ind_b_u]]])
                                else:
                                    norms_b=abs(s_deltaH[out_of_lbound[ind_b_l]])
                                    delta_b=abs(lb[ind_free[out_of_lbound[ind_b_l]]] - s[ind_free[out_of_lbound[ind_b_l]]])
                                    ind_b=out_of_lbound[ind_b_l]
                                    sign_b=sign_(lb[ind_free[out_of_lbound[ind_b_l]]] - s[ind_free[out_of_lbound[ind_b_l]]])
                        else:
                            #  INSIDE the bounds but no step component active:
                            #  find the closest components to its bound from the
                            #  set of components which were initially outside
                            outside=0
                            if (length_(out_of_ubound_init) != 0):
                                diff_b_u,ind_b_u=min_(abs(ub[ind_free[out_of_ubound_init]] - s_duringH[ind_free[out_of_ubound_init]]),nargout=2)
                                norms_b=abs(s_deltaH[out_of_ubound_init[ind_b_u]])
                                delta_b=abs(ub[ind_free[out_of_ubound_init[ind_b_u]]] - s[ind_free[out_of_ubound_init[ind_b_u]]])
                                ind_b=out_of_ubound_init[ind_b_u]
                                sign_b=sign_(ub[ind_free[out_of_ubound_init[ind_b_u]]] - s[ind_free[out_of_ubound_init[ind_b_u]]])
                            if (length_(out_of_lbound_init) != 0):
                                diff_b_l,ind_b_l=min_(abs(s_duringH[ind_free[out_of_lbound_init]] - lb[ind_free[out_of_lbound_init]]),nargout=2)
                                norms_b=abs(s_deltaH[out_of_lbound_init[ind_b_l]])
                                delta_b=abs(lb[ind_free[out_of_lbound_init[ind_b_l]]] - s[ind_free[out_of_lbound_init[ind_b_l]]])
                                ind_b=out_of_lbound_init[ind_b_l]
                                sign_b=sign_(lb[ind_free[out_of_lbound_init[ind_b_l]]] - s[ind_free[out_of_lbound_init[ind_b_l]]])
                            if ((length_(out_of_ubound_init) != 0) and (length_(out_of_lbound_init) != 0)):
                                if (diff_b_u < diff_b_l):
                                    norms_b=abs(s_deltaH[out_of_ubound_init[ind_b_u]])
                                    delta_b=abs(ub[ind_free[out_of_ubound_init[ind_b_u]]] - s[ind_free[out_of_ubound_init[ind_b_u]]])
                                    ind_b=out_of_ubound_init[ind_b_u]
                                    sign_b=sign_(ub[ind_free[out_of_ubound_init[ind_b_u]]] - s[ind_free[out_of_ubound_init[ind_b_u]]])
                                else:
                                    norms_b=abs(s_deltaH[out_of_lbound_init[ind_b_l]])
                                    delta_b=abs(lb[ind_free[out_of_lbound_init[ind_b_l]]] - s[ind_free[out_of_lbound_init[ind_b_l]]])
                                    ind_b=out_of_lbound_init[ind_b_l]
                                    sign_b=sign_(lb[ind_free[out_of_lbound_init[ind_b_l]]] - s[ind_free[out_of_lbound_init[ind_b_l]]])
                    if (verbose > 1):
                        #  Iteration printout

                        lambda_save.append(_lambda)
                        norms_b_save.append(norms_b)
                        if (outside == 0):
                            fprintf_('%s%d%s %12.8e %s %12.8e %s\n' % (' bcdfo_solve_TR_MS_bc (',i,'): |s_i| = ',norms_b,'  |bound_i| = ',delta_b,'   s < bounds'))
                        else:
                            fprintf_('%s%d%s %12.8e %s %12.8e\n' % (' bcdfo_solve_TR_MS_bc (',i,'): |s_i| = ',norms_b,'  |bound_i| = ',delta_b))
                    #  Test if step inside bounds +/- eps_bound

                    out_of_uEpsbound=find_((ub[ind_free] - s_duringH[ind_free]) < - eps_bound)
                    out_of_lEpsbound=find_((s_duringH[ind_free] - lb[ind_free]) < - eps_bound)
                    if (isempty_(out_of_uEpsbound) and isempty_(out_of_lEpsbound)):
                        if (verbose > 1):
                            disp_('all components inside the bounds + eps_bound')
                        back_inside=1
                      # check if at least one component active

                        ind_u_active=find_(abs(ub[ind_free] - s_duringH[ind_free]) <= eps_bound)
                        ind_l_active=find_(abs(s_duringH[ind_free] - lb[ind_free]) <= eps_bound)
                        if ((length_(ind_u_active) + length_(ind_l_active)) != 0):
                            if (verbose > 1):
                                disp_('all components inside the bounds + eps_bound, ',str(length_(ind_u_active) + length_(ind_l_active)),' component/s close to one of its bounds')
                            #  Compute the current step after the homotopy-step

                            s_afterH=s + I[:,ind_free] .dot( s_deltaH )
                           #  Move active components to their bounds

                            if (length_(ind_u_active) > 0):
                                s_afterH[ind_free[ind_u_active]]=ub[ind_free[ind_u_active]]
                            if (length_(ind_l_active) > 0):
                                s_afterH[ind_free[ind_l_active]]=lb[ind_free[ind_l_active]]
                          #  Define information message.

                            msg='boundary solution'
                            break
                  #  Compute new lambda
 
                    if (stratLam == 0): #  Using bisection method
                        if (back_inside == 0):
                            _lambda=2 * _lambda
                            if (upper < _lambda):
                                upper=2 * _lambda
                        else:
                            if (isempty_(out_of_ubound) and isempty_(out_of_lbound)):
                                upper=copy(_lambda)
                            else:
                                lower=copy(_lambda)
                            new_lambda=(_lambda + old_lambda) / 2
                            theta_range=theta * (upper - lower)
                            if (new_lambda > lower + theta_range and new_lambda < upper - theta_range):
                                _lambda=copy(new_lambda)
                            else:
                                _lambda=max_(sqrt_(lower * upper),lower + theta_range)
                    else:  #  Using  Newton's iteration on the modified secular equation
                       #  Reset bounds on lambda
                        if (isempty_(out_of_ubound) and isempty_(out_of_lbound)):
                            upper=copy(_lambda)
                        else:
                            lower=copy(_lambda)
                     #  check the sign of the chosen step component
 
                        unitvec=zeros_(nfree,1)
                        unitvec[ind_b]=1
                        es=unitvec.T .dot( s_deltaH )
                        if (sign_(es) != sign_b):
                           #  if step component has the wrong sign
                           #  (other than the active bound): one bisection step
                            new_lambda=(lower + upper) / 2
                        else:
                           #  Newton step
                            w1=np.linalg.solve(R.T,unitvec)
                            w2=np.linalg.solve(R.T,s_deltaH)
                            new_lambda=_lambda + ((norms_b - delta_b) / delta_b) * (norms_b ** 2 / (es .dot( (w1.T .dot( w2)))))
                            if (back_inside == 0 and upper <= new_lambda):
                                upper=2 * new_lambda
                       #  Check new value of lambda wrt its bounds
 
                        theta_range=theta * (upper - lower)
                        if (new_lambda > lower + theta_range and new_lambda <= upper - theta_range):
                            _lambda=copy(new_lambda)
                        else:
                            _lambda=real_(max_(sqrt_(lower * upper),lower + theta_range))
                else:  #  Unsuccessful factorization: compute new lambda
                    if (verbose > 1):
                        disp_('unsuccessful factorization')
                    hardcase=0
                    lower=copy(_lambda)
                    t=0.5
                    _lambda=(1 - t) * lower + t * upper
                if (i >= 100):          #  Return with error message after 100 iterations

                    s[0:n]=0.0
                    norms=0
                    msg='limit in bc-MS exceeded'
                    if (verbose):
                        disp_('Error in bcdfo_solve_TR_MS_bc: iteration limit in bc-MS exceeded!')
                    if verbose > 1:
                        disp_('bcdfo_solve_TR_MS_bc: exit!')
                    return s,_lambda,norms,value,gplus,nfact,neigd,msg
          # end of while-loop
        else:
          # MS was successful inside the bounds
            if (verbose > 1):
                disp_('step inside bounds!')
          #  Define information message.
            msg='(partly) interior solution'
          #  update the step and model value
            s=copy(s_after_reduced_ms)
            norms=norm_(s)
            value=0.5 * s.T.dot( H .dot( s )) + s.T .dot( g0 )
            if (verbose > 1):
                disp_('bcdfo_solve_TR_MS_bc: exit!')
            return s,_lambda,norms,value,gplus,nfact,neigd,msg
       #  update the step and model value
        s=copy(s_afterH)
        norms=norm_(s)
        value=0.5 * s.T .dot( H .dot( s )) + s.T .dot( g0 )
       #  update trust-region radius
        Delta=Delta0 - norms
        if (Delta < - eps_bound):
            if verbose:
                disp_('Error in bcdfo_solve_TR_MS_bc: delta smaller than zero !!!!!!')
            msg='error7'
            if (verbose > 1):
                disp_('bcdfo_solve_TR_MS_bc: exit!')
            return s,_lambda,norms,value,gplus,nfact,neigd,msg
        else:
            if (Delta < 0):
                if (verbose > 1):
                    disp_('bcdfo_solve_TR_MS_bc: exit!')
                return s,_lambda,norms,value,gplus,nfact,neigd,msg
      #  update gradient 
        g=g0 + H .dot( s )
        ind_active=find_(logical_or((ub - s) <= eps_bound, (s - lb) <= eps_bound))
        ind_active=ind_active.T
        ind_free=setdiff_(list(range(0,n)),ind_active)
        nfree=length_(ind_free)
        if (nfree > 0):
          #  check first-order criticality

            ng_reduced=norm_(g[ind_free],inf)
            if (ng_reduced <= 1e-05):
                if (verbose > 1):
                    disp_('point first order critical - return')
                    print(ng_reduced)
                if (verbose > 1):
                    disp_('bcdfo_solve_TR_MS_bc: exit!')
                return s,_lambda,norms,value,gplus,nfact,neigd,msg
          #  Fix components which became active
            ind_g_crit=find_(logical_or(logical_and(abs(lb[ind_free]) <= 1e-10, g[ind_free] > 0), logical_and(ub[ind_free] <= 1e-10, g[ind_free] < 0)))
            if (not isempty_(ind_g_crit)):
                ind_active=concatenate_([ind_active,ind_free[ind_g_crit].T],axis=1)
                ind_free=setdiff_(ind_free,ind_active)
                nfree=length_(ind_free)

    return s,_lambda,norms,value,gplus,nfact,neigd,msg
