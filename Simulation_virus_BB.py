"""
    Bigger scale simulation of a virus spread in a city.
    This would have been the better opt for the project, as it uses geospatial visualisation (which is not in this code)
    and data gathered from a a ride share, a specific city, their population, and their public transport data.

    I still don't understand how geospatial visualisation works (I think I will look more into it in the holidays)
    The simulation uses mathematical equations on how a virus would spread and includes its recovery rates.

    Technically this code works (I think)...
    It is just missing it's data and its visuals
"""

import numpy as np
from collections import namedtuple

Param = namedtuple('Param', 'R0 DE DI I0 HopitalisationRate HospitalIters')
# I0 is the distribution of infected people at time t=0, if None then randomly choose inf number of people

# flow is a 3D matrix of dimentions r x n x n (i.e., 84 x 549 x 549),
# flow[t mod r] is the desired OD matrix at time t.

def seir(par, distr, flow, alpha, iterations, inf):

    r = flow.shape[0]
    n = flow.shape[1]
    N = distr[0].sum() #total population, we assume that N = sum(flow)
    Svec = distr[0].copy()
    Evec = np.zeros(n)
    Ivec = np.zeros(n)
    Rvec = np.zeros(n)

    if par.I0 is None:
        initial = np.zeros(n)
        # randomly choose inf infections
        for i in range(inf):
            loc = np.random.randint(n)
            if (Svec[loc] > initial[loc]):
                initial[loc] += 1.0

    else:
        initial = par.I0
    assert ((Svec < initial).sum() == 0)

    Svec -= initial
    Ivec += initial
    
    res = np.zeros((iterations, 5))
    res[0,:] = [Svec.sum(), Evec.sum(), Ivec.sum(), Rvec.sum(), 0]

    realflow = flow.copy()

    realflow = realflow / realflow.sum(axis=2)[:,:, np.newaxis]
    realflow = alpha * realflow

    history = np.zeros((iterations, 5, n))
    history[0,0,:] = Svec
    history[0,1,:] = Evec
    history[0,2,:] = Ivec
    history[0,3,:] = Rvec

    eachIter = np.zeros(iterations + 1)

    # run simulation
    for iter in range(0, iterations - 1):
        realOD = realflow[iter % r]

        d = distr[iter % r] + 1

        if ((d>N+1).any()):
            print("Houston, we have a problem!")
            return res, history
        # N = S + E + I + R

        newE = Svec * Ivec / d * (par.R0 / par.DI)
        newI = Evec / par.DE
        newR = Ivec / par.DI

        Svec -= newE
        Svec = (Svec + np.matmul(Svec.reshape(1,n), realOD) - Svec * realOD.sum(axis=1))
        Evec = Evec + newE - newI
        Evec = (Evec + np.matmul(Evec.reshape(1,n), realOD) - Evec * realOD.sum(axis=1))
        Ivec = Ivec + newI - newR
        Ivec = (Ivec + np.matmul(Ivec.reshape(1,n), realOD) - Ivec * realOD.sum(axis=1))
        Rvec += newR
        Rvec = (Rvec + np.matmul(Rvec.reshape(1,n), realOD) - Rvec * realOD.sum(axis=1))

        res[iter + 1,:] = [Svec.sum(), Evec.sum(), Ivec.sum(), Rvec.sum(), 0]
        eachIter[iter + 1] = newI.sum()
        res[iter + 1, 4] = eachIter[max(0, iter - par.HospitalIters) : iter].sum() * par.HospitalisationRate

        history[iter + 1,0,:] = Svec
        history[iter + 1,1,:] = Evec
        history[iter + 1,2,:] = Ivec
        history[iter + 1,3,:] = Rvec


    return res, history