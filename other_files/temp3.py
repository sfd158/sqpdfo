# -*- coding: utf-8 -*-

from runtime import matlabarray
import numpy as np

A = np.array([[1,2,3]]).T#,[4,5,6],[7,8,9]])
print "A\n", A
B = np.array([[10, 11, 12]]).T#,[13, 14, 15], [16, 17, 18]])
print "B\n", B

#ilb = np.array([[True, False, True]]).T#,[False, False, False],[False, False, False]])
ilb = np.array([[True, False, True]]).T

indfree = np.array([[0,1,2]]).T

print "A[ilb]\n", A[ilb]
print "A[indfree[ilb]]\n", A[indfree[ilb]]
print "A[indfree[ilb]].T\n", A[indfree[ilb]].T
B[ilb] = A[ilb]
print "B after\n", B

#lbounds = np.array([[-np.inf, 0.0, -np.inf]]).T
#lb = np.array([[-0.5, 0.0, -np.inf]]).T
#ilb = np.array([[False, True, False]]).T
#indfree = np.array([[1, 2, 3]]).T - 1
#print "lbounds\n", lbounds
#print "lb\n", lb
#print "ilb\n", ilb
#print "indfree\n", indfree
#print "lb[indfree[ilb]]\n", lb[indfree[ilb]]
#lbounds[ilb] = lb[indfree[ilb]]
#print "l------------------------bounds after\n", lbounds


#lbounds = matlabarray([-np.inf, 0.0, -np.inf]).T
#lb = matlabarray([-0.5, 0.0, -np.inf]).T
#ilb = matlabarray([False, True, False]).T
#indfree = matlabarray([1, 2, 3]).T

#print "lbounds\n", lbounds
#print "lb\n", lb
#print "ilb\n", ilb
#print "indfree\n", indfree
#print "lb[indfree[ilb]]\n", lb[indfree[ilb]]
#print "ndenumerate:"

#for index,value in np.ndenumerate(ilb):
#	print "index = ", index
#	print "value = ", value
#	if value == True:
		
	#do_something( value )
	#self.cells[index] = new_value

#np.asarray(lbounds).__setitem__(ilb - 1, lb[indfree[ilb] - 1])
#print "Here we go!:"
#lbounds[ilb] = lb[indfree[ilb]]

#print "lbounds\n", lbounds
#print "lbounds after\n", lbounds


#A = np.array([[1,np.nan],[np.nan,4]])
#B = matlabarray(A)

#print "A is zero\n", np.isnan(A)

#print "A is not zero:\n", A[~np.isnan(A)]

#ret = B[~np.isnan(B)]
#print "B is not zero:\n", ret

#print "np array func result:\n", np.ndarray.__getitem__(B, ~np.isnan(B))

#print "A == 0", A == 0