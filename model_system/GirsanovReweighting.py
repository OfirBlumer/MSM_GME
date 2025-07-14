import scipy.sparse
from msmbuilder.msm.core import _solve_msm_eigensystem
import numpy as np

macro_traj = np.load("biasedMacroTraj.npy")
lag = 100
array = np.loadtxt("ReweightingFactors.txt")
M = array[:,0]
g = array[:,1]+10
m = M.cumsum()
m[lag:] = m[lag:] - m[:len(m)-lag]
m = m[(lag):]
m = np.exp(-m)
data = g[0:-lag]*m
T = scipy.sparse.coo_matrix((data, (macro_traj[0][:-lag], macro_traj[0][lag:])), shape=(4,4)).toarray()
for i in range(4):
    if T[i, :].sum() > 0:
        T[i, :] /= T[i, :].sum()
u, lv, rv = _solve_msm_eigensystem(T,4)
with np.errstate(invalid='ignore', divide='ignore'):
    print(- lag / np.log(u[1:]))
